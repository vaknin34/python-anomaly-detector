# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 18:58:56 2020

@author: vakni
"""
class Line:    
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def f(self,x):
        return self.a*x+self.b
    
    def printLine(self):
        print(str(self.a)+"*x"+str(self.b))
        
        


