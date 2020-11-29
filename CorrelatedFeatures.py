# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:52:37 2020

@author: vakni
"""
class CorrelatedFeatures:
    def __init__(self,feature1,feature2,corrlation,lin_reg,threshold):
        self.feature1 = feature1
        self.feature2 = feature2
        self.corrlation = corrlation
        self.lin_reg = lin_reg
        self.threshold = threshold
        
    def printCof(self):
            print("corrleated Feature are " + self.feature1 + " " + self.feature2)
            print("corrleation Strength is " + str(self.corrlation))
            self.lin_reg.printLine()
            print("Max Eror is " + str(self.threshold))
    

            