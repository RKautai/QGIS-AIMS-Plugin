################################################################################
#
# Copyright 2015 Crown copyright (c)
# Land Information New Zealand and the New Zealand Government.
# All rights reserved
#
# This program is released under the terms of the 3 clause BSD license. See the 
# LICENSE file for more information.
#
################################################################################
import json
import httplib2

from Config import ConfigReader

class AimsApi( ):
    ''' make and receive all http requests / responses to AIMS API '''   
        
    def __init__(self):
        config = ConfigReader()
        self._url = config.configSectionMap('url')['api']
        self._user = config.configSectionMap('user')['name']
        self._password = config.configSectionMap('user')['pass']
        self._headers = {'content-type':'application/json', 'accept':'application/json'}
    
    @staticmethod #or do i want classmethod?    
    def handleErrors( content ):
        ''' Return the reason for any critical errors '''        
        criticalErrors = []
        for i in content['entities']:
            if i['properties']['severity'] == 'Reject':
                criticalErrors.append( '- '+i['properties']['description']+'\n' )
        return ''.join(criticalErrors)

    @staticmethod       
    def handleResponse(cls, resp, content ):
        ''' test http response'''
        if resp == 201: #to be more inclusive i.e. 200 ...
            return [] #i.e. no errors
        return cls.handleErrors( content )
    
    def changefeedAdd( self, payload ):
        ''' Add an address to the Change feed '''
        h = httplib2.Http(".cache")
        h.add_credentials(self._user, self._password)
        resp, content = h.request(self._url+'changefeed/add', "POST", json.dumps(payload), self._headers)
        return self.handleResponse(self, resp["status"], json.loads(content) )
        
    def changefeedUpdate( self, payload ):
        ''' Update an address on the Change feed '''
        pass 
       
    def changefeedDelete( self, payload ):
        ''' Delete a address via Change feed '''
        pass
