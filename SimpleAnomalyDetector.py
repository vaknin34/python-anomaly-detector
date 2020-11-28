# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 21:06:52 2020

@author: vakni
"""

from StatLib import StatLib 
from CorrelatedFeatures import CorrelatedFeatures
from AnomalyReport import AnomalyReport
class SimpleAnomalyDetector:

    
    def __init__(self):
        self.cofeatures = []
    

    def isContain(self,cof):
        for s_cof in self.cofeatures:
            if s_cof.feature1 == cof.feature2 and  s_cof.feature2 == cof.feature1:
                return True
        return False

    def learnNormal(self,ts):
        max_corrlation = 0
        p_sub_feature = -1
        pearson_res = 0
        for i in range(len(ts.table)):
            mf = ts.table[i]
            for j in range(len(ts.table)):
                sf = ts.table[j]
                if mf.getName() != sf.getName():
                    x = mf.getSampels()
                    y = sf.getSampels()
                    pearson_res = abs(StatLib.pearson(StatLib,x,y))
                    if pearson_res > max_corrlation:
                        max_corrlation = pearson_res
                        p_sub_feature = j
            if p_sub_feature != -1:
                sf = ts.table[p_sub_feature]
                points_arr = StatLib.point_gen(mf.getSampels(),sf.getSampels())
                lrg = StatLib.linear_reg(StatLib,points_arr)
                threshold = 0
                for p in points_arr:
                    dev = StatLib.dev(lrg,p)
                    if dev > threshold:
                        threshold = dev
                cof = CorrelatedFeatures(mf.getName(),sf.getName(),max_corrlation,lrg,threshold*1.1)
                if not(self.isContain(cof)):
                    self.cofeatures.append(cof)
            max_corrlation = 0
            p_sub_feature = -1
            
    def detect(self,ts):
        arl = []
        for cf in self.cofeatures:
            discription = cf.feature1 + '-' + cf.feature2
            mf = ts.getFeatureByName(cf.feature1)
            sf = ts.getFeatureByName(cf.feature2)
            points_arr = StatLib.point_gen(mf.getSampels(),sf.getSampels())
            raw_index = 1
            for p in points_arr:
                dev = StatLib.dev(cf.lin_reg,p)
                if dev > cf.threshold:
                    ar = AnomalyReport(discription,raw_index)
                    arl.append(ar)
                raw_index += 1
        return arl
    
    
    def getNormalModel(self):
        return self.cofeatures
    
    
    def getCof(self,report):
        f_names = report.discription.split('-')
        for cof in self.cofeatures:
            if cof.feature1 == f_names[0] and cof.feature2 == f_names[1]:
                return cof
        return 0
            
    
    
    
    
        
            
            
            
        
         
        
                        
                
            
                        
                        
                        
                    
                    
                    
                    
        









