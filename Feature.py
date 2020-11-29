# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 20:19:51 2020

@author: vakni
"""
class Feature:    
        def __init__(self,name,samples):
            self.name = name
            self.samples = samples 
            
        def setName(self,name):
            self.name = name
        def setSamples(self,samples):
            self.samples = samples
        def getName(self):
            return self.name
        def getSampels(self):
            return self.samples
        def addSample(self,x):
            self.samples.append(x)