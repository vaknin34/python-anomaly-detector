# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:32:08 2020

@author: vakni
"""
import TimeSeries
import SimpleAnomalyDetector
import Visual
class UI():
    def greetingUser(self):
        print('Hello User and Welcome to Csv Anomaly Detector')
    
    def trainingUpload(self):
        x = input("enter File Path ")
        self.ts = TimeSeries.TimeSeries(x)
        self.mainMenu()
        
    def learnData(self):
        self.ad =  SimpleAnomalyDetector.SimpleAnomalyDetector()
        self.ad.learnNormal(self.ts)
        self.mainMenu()
    
    def testUpload(self):
        x = input("enter File Path ")
        self.ts = TimeSeries.TimeSeries(x)
        self.mainMenu()
    
    def anomalyDetection(self):
        self.arl =  self.ad.detect(self.ts)
        self.mainMenu()
        
    def reportsPrint(self):
        for r in self.arl:
            print("columns : " + r.discription + " raw " + str(r.timestamp))
        self.mainMenu()
        
    def plotAnomaly(self):
        anomaly_size = len(self.arl) -1
        x = int(input("please choose anomaly number between 0 and " + str(anomaly_size)))
        while x < 0 or x > anomaly_size:
            print("Worng Number")
            x = int(input("please choose anomaly number between 0 and " + str(anomaly_size)))
        cof = self.ad.getCof(self.arl[x])
        vs = Visual.Visual(self.ts,cof)
        vs.printGraphAnomaly(self.arl[x].timestamp)
        self.mainMenu()
        
    def cofPrint(self):
        for cof in self.ad.cofeatures:
            cof.printCof()
        self.mainMenu()
    
    def mainMenu(self):
        print('choose 1 for trainng csv upload')
        print('choose 2 for learning the Data')
        print('choose 3 for correlated features')
        print('choose 4 for test csv upload')
        print('choose 5 for anomaly detection in test csv ')
        print('choose 6 for anomaly reports')
        print('choose 7 for ploting anomaly')
        print('choose 8 for exit')
        self.getUserInput()
    
    def getUserInput(self):
        x = int(input("plz choose Number "))
        while x < 1 or x > 8:
            print("Worng Number")
            x = int(input("plz choose Number "))
        if x == 1:
            self.trainingUpload()
        if x == 2:
            self.learnData()
        if x == 3:
            self.cofPrint()
        if x == 4:
            self.testUpload()
        if x == 5:
            self.anomalyDetection()
        if x == 6:
            self.reportsPrint()
        if x == 7:
            self.plotAnomaly()
        if x == 8:
            print("Thank you for use my program see you next time")
            
            
            
            
        
            
            
            
            
            
            