#!/usr/bin/python
# -*- coding: utf-8 -*-
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

#http://devassgeo01:8080/aims/api/address/features - properties

import re
from AimsUtility import FeatureType,ActionType,ApprovalType,FeedType
from AimsLogging import Logger


aimslog = None


class Feature(object):
    
    type = FeedType.FEATURES
    
    global aimslog
    aimslog = Logger.setup()
    
    def __init__(self, ref=None): 
        #aimslog.info('AdrRef.{}'.format(ref))
        self._ref = ref

    
    #generic validators
    @staticmethod
    def _vString(sval): return isinstance(sval,str) #alpha only filter?
    @staticmethod
    def _vInt(ival): return isinstance(ival, int) #range filter?
    @staticmethod
    def _vDate(date): return Feature._vString(date) and bool(re.match('^\d{4}-\d{2}-\d{2}$',date)) 
    

    #---------------------------------------------------
    
    def _setEntities(self,entities):
        self.setMeta()
        self.meta.entities = entities
 
    def _getEntities(self):
        return self.meta.entities
    
    def setMeta(self, meta = None):
        if not hasattr(self,'meta'): self.meta = meta if meta else FeatureMetaData()
        
    def getMeta(self): 
        return self.meta if hasattr(self, 'meta') else None    
    
    
    def compare(self,other):
        '''Equality comparator'''
        #return False if isinstance(self,other) else hash(self)==hash(other)
        #IMPORTANT. Attribute value compare only useful with distinct (deepcopy'd) instances
        return all((getattr(self,a)==getattr(other,a) for a in self.__dict__.keys()))
    
    
    #---------------------------------
    
    def setRequestId(self,requestId):
        self.setMeta()
        self.meta.requestId = requestId      
           
    def getRequestId(self):
        return self.meta.requestId if hasattr(self,'meta') else None
     
    def setErrors(self,errors):
        self.setMeta()
        self.meta.errors = errors      
           
    def getErrors(self):
        return self.meta.errors if hasattr(self,'meta') else None
    
class FeatureMetaData(object):
    '''Embedded container for address meta information eg warnings, errors and tracking'''
    def __init__(self):self._requestId,self._statusMessage,self._errors,self._entities = 0,'',[],[]
    
    @property
    def requestId(self): return self._requestId
    @requestId.setter
    def requestId(self, requestId): self._requestId = requestId if Feature._vInt(requestId) else None
    
    @property
    def entities(self): return self._entities  
    @entities.setter
    def entities(self,entities): self._entities = entities 
     
    @property
    def errors(self): return self._errors  
    @errors.setter
    def errors(self,errors): self._errors = errors
    