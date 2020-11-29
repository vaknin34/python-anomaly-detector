# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:46:31 2020

@author: vakni
"""
import matplotlib.pyplot as plt
class Visual:
    def __init__(self,ts,cf):
        self.ts = ts
        self.cf = cf
    
    def printGraph(self):
        x = self.ts.getFeatureByName(self.cf.feature1).getSampels()
        y = self.ts.getFeatureByName(self.cf.feature2).getSampels()
        y_pred = []
        for sample in x:
            y_pred.append(self.cf.lin_reg.f(sample))
        upper_boundary = []
        lower_boundary = []
        for i in y_pred:
            upper_boundary.append(i+self.cf.threshold)
            lower_boundary.append(i-self.cf.threshold)
        plt.plot(x,y,color ='blue',marker="",label='Real Data')
        # plt.scatter(x,upper_boundary,color = 'red')
        # plt.scatter(x,lower_boundary,color = 'green')
        plt.plot(x,y_pred,color='red',marker="",label='Pred Data')
        plt.xlabel(self.cf.feature1)
        plt.ylabel(self.cf.feature2)
        plt.legend(loc='best')
        plt.show()
        
    def printGraphAnomaly(self,anomaly_raw):
        x = self.ts.getFeatureByName(self.cf.feature1).getSampels()
        y = self.ts.getFeatureByName(self.cf.feature2).getSampels()
        y_pred = []
        for sample in x:
            y_pred.append(self.cf.lin_reg.f(sample))
        upper_boundary = []
        lower_boundary = []
        for i in y_pred:
            upper_boundary.append(i+self.cf.threshold)
            lower_boundary.append(i-self.cf.threshold)
        lower_index = max(anomaly_raw-2,0)
        max_index = min(anomaly_raw+2,len(x))
        x = x[lower_index:max_index]
        y_pred = y_pred[lower_index:max_index]
        upper_boundary = upper_boundary[lower_index:max_index]
        lower_boundary = lower_boundary[lower_index:max_index]
        y = y[lower_index:max_index]
        plt.plot(x,y,color ='blue',marker="",label='Real Data')
        # plt.scatter(x,upper_boundary,color = 'red')
        # plt.scatter(x,lower_boundary,color = 'green')
        plt.plot(x,y_pred,color='red',label='Pred Data')
        plt.xlabel(self.cf.feature1)
        plt.ylabel(self.cf.feature2)
        plt.legend(loc='best')
        plt.show()
        
        
    def printGraphAnomalyReverse(self,anomaly_raw):
        x = self.ts.getFeatureByName(self.cf.feature1).getSampels()
        y = self.ts.getFeatureByName(self.cf.feature2).getSampels()
        y_pred = []
        for sample in x:
            y_pred.append(self.cf.lin_reg.f(sample))
        upper_boundary = []
        lower_boundary = []
        for i in y_pred:
            upper_boundary.append(i+self.cf.threshold)
            lower_boundary.append(i-self.cf.threshold)
        lower_index = max(anomaly_raw-2,0)
        max_index = min(anomaly_raw+2,len(x))
        x = x[lower_index:max_index]
        y_pred = y_pred[lower_index:max_index]
        upper_boundary = upper_boundary[lower_index:max_index]
        lower_boundary = lower_boundary[lower_index:max_index]
        y = y[lower_index:max_index]
        plt.plot(y,x,color ='blue',marker="",label='Real Data')
        # plt.scatter(x,upper_boundary,color = 'red')
        # plt.scatter(x,lower_boundary,color = 'green')
        plt.plot(y_pred,x,color='red',label='Pred Data')
        plt.xlabel(self.cf.feature2)
        plt.ylabel(self.cf.feature1)
        plt.legend(loc='best')
        plt.show()
        
            
        
        
