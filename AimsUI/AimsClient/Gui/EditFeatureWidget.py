
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.gui import *

from Ui_EditFeatureDialog import Ui_EditFeatureDialog
from AIMSDataManager.FeatureFactory import FeatureFactory
from UiUtility import UiUtility 
from AIMSDataManager.AimsUtility import FEEDS, FeedType
from AIMSDataManager.Address import Position

import time

class EditFeatureWidget( Ui_EditFeatureDialog, QWidget ):
    """
    UI Form for the user to edit AIMS Feature information 
    """

    def __init__(self, controller = None):
        """
        Make form button and input field connections
        
        @param controller: instance of the plugins controller
        @type  controller: AimsUI.AimsClient.Gui.Controller
        """
        
        QWidget.__init__( self )
        self.setupUi(self)
        
        getRclIcon = QIcon()
        getRclIcon.addPixmap(QPixmap(":/plugins/QGIS-AIMS-Plugin/resources/selectrcl.png"), QIcon.Normal, QIcon.On)
        self.uGetRclToolButton.setIcon(getRclIcon)
        
        self.setController( controller )
        self._iface = self._controller.iface
        self._layerManager = self._controller._layerManager
        self.highlight = self._controller.highlighter
        self.coords = None
        self.feature = None
        
#         # Val Ref, Cert Title and App have been temp taken out of scope
        hide = (self.uExternalObjectId, self.uExtObjectIdScheme, 
                 self.lExtObjectIdScheme,  self.lExternalObjectId)
        for uiElement in hide:
            uiElement.hide()
            
        self.wAddObj.hide()
        
        # Make connections
        self.uAddressType.currentIndexChanged.connect(self.setEditability)
        self.buttonAO.clicked.connect(self.showAddObj)
        # connect dynamic address splitter components 
        self.uFullNum.textEdited.connect(self.fullNumChanged)
        
        partComponents = (self.uPrefix,self.uUnit, self.uBase, 
                          self.uBase, self.uHigh, self.uAlpha )
        
        for com in partComponents:
            com.textEdited.connect(self.partNumChanged)
         
        self.uSubmitAddressButton.clicked.connect(self.submitAddress)
        self.uAbort.clicked.connect(self.closeDlg)
        self.uGetRclToolButton.clicked.connect(self.getRcl)
        self.af = {ft:FeatureFactory.getInstance(FEEDS['AC']) for ft in FeedType.reverse}  
         
        # limit user inputs
        UiUtility.formMask(self)
        # set combo box defaults
        UiUtility.setFormCombos(self)
        # set addressType to trigger currentIndexChanged
        self.uAddressType.setCurrentIndex(QComboBox.findText(self.uAddressType,'Road'))
        
    def setController(self, controller):
        """  
        Access and assign the single instance of the Controller 
        
        @param controller: instance of the plugins controller
        @type  controller: AimsUI.AimsClient.Gui.Controller
        """
        
        import Controller
        if not controller:
            controller = Controller.instance()
        self._controller = controller
    
    def setFeature(self, parent, addInstance, coords = None):
        """
        Load the AIMS Feature to UI form
        
        @param parent: The tool that enable the form 
        @type  parent: string
        @param addInstance: The AIMS Address instance
        @type  addInstance: AIMSDataManager.Address
        @param coords: AIMS Feature's associated point
        @type  coords: QgsPoint
        """
        
        self.parent = parent
        self.feature = addInstance
        self.coords = coords
        self.uFullNum.setFocus()
        if parent == 'update':
            self.feature = self.af[FeedType.CHANGEFEED].cast(self.feature)
            UiUtility.featureToUi(self, parent) 
        elif parent == 'add' and self._controller._queues.uEditFeatureTab.uPersistRcl.isChecked():
            self._controller._rcltool.fillform()
    
    def hideMarker(self):
        """
        Remove highligthing of the AIMS feature
        """
        
        self.highlight.hideAddress()
        self.highlight.hideNewAddress()
        self.highlight.hideRcl()
     
    def setEditability(self):
        """
        Set the editability of each user input field embedded with the feature 
        form based on the user supplied address class
        """
        
        UiUtility.setEditability(self, self.parent)
            
    def getRcl(self):
        """
        enable the RCL Tool to allow the user to click and populate 
        the road information in the form
        """
        
        self._controller.startRclTool(self)
      
    def closeDlg (self):
        """ 
        Close form 
        """
         
        # revert back to NewAddTool
        self._controller.setPreviousMapTool()
        # revert back to review tab 
        self._controller._queues.tabWidget.setCurrentIndex(1)
        self.hideMarker()
    
    def showAddObj(self):
        if self.wAddObj.isVisible():
            self.wAddObj.hide()
        else:
            self.wAddObj.show()
                    
      
    def setPosition(self):
        """
        Set the feature position information
        """
        
        coords = [self.coords.x(), self.coords.y()]
        pos = {"position":{
                    "type":'Point',
                    "coordinates":coords,
                    "crs":{
                         "type":'name',
                         "properties":{
                            "name":'urn:ogc:def:crs:EPSG::4167'
                         }
                    }
                },
                "positionType":'Unknown', # <-- need to add PT to form
                "primary":True
                }
        
        position = Position.getInstance(pos)
        self.feature.setAddressPositions(position)
                   
    def submitAddress(self):
        """ 
        Submit the user inputed information to DataManager
        """
        if not UiUtility.formCompleteness(self.parent, self, self._iface ):
            return
        
        respId = int(time.time())

        if self.parent == 'add': 
            self.setPosition()   
            UiUtility.formToObj(self)
            self._controller.uidm.addAddress(self.feature, respId)
        
        elif self.parent == 'update': 
            UiUtility.formToObj(self)
            self.feature = self.af[FeedType.CHANGEFEED].cast(self.feature)            
            self._controller.uidm.updateAddress(self.feature, respId)
        
        # check the response 
        self._controller.RespHandler.handleResp(respId, FEEDS['AC'])
        # revert back to review tab 
        self._controller._queues.tabWidget.setCurrentIndex(1)
        self.hideMarker()
        
    def fullNumChanged(self, newnumber):
        """
        When the full number input is modified, split it into and
        update its individual components 
        
        @param newnumber: user input to uFullNum
        @type  newnumber: string
        """
        
        UiUtility.fullNumChanged(self, newnumber)
        
    def partNumChanged(self):
        """ 
        When an individual component is modified, concatenate all components and 
        update the 'full number'
        """
        
        if self.uUnit.text(): unit = self.uUnit.text()+'/' 
        else: unit = ''
        
        if self.uHigh.text(): high = '-'+self.uHigh.text()
        else: high = ''
        
        self.uFullNum.setText(self.uPrefix.text().upper()+unit+self.uBase.text()+high+self.uAlpha.text().upper())
