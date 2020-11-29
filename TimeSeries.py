# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:45:54 2020

@author: vakni
"""
import pandas as pd
from Feature import Feature



class TimeSeries:    
    def __init__(self,csvFileName):
        self.csvFileName = csvFileName
        self.table = []
        df = pd.read_csv(csvFileName)
        t_flag = 1
        index= []
        for i in range(1,len(df)+1):
            index.append(i)
        for col in df.columns:
            if df[col].dtype == "float64" or df[col].dtype == "int64":
                f = Feature(col,df[col].values)
                self.table.append(f)
                b = f.getSampels() == index
                if b.all():
                    t_flag = 0            
        if t_flag:
            f = Feature("TimeStamp",index)
            self.table.append(f)
        
            
    def getTable(self):
        return self.table
    
    def getFeatureByName(self,name):
        for f in self.table:
            if f.getName() == name:
                return f
        return 0
    
            
            
            
        
        
        
        
        
        
    
    
    
    
    























