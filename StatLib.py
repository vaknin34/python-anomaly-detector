# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:03:05 2020

@author: vakni
"""
import math
from Line import Line
from Point import Point
class StatLib:
    
    # avg
    def avg(f_arr):
        sum = 0
        for f in f_arr:
            sum = sum + f
        return sum/len(f_arr)
    
    def var(self,f_arr):
        favg = self.avg(f_arr)
        sum = 0
        for f in f_arr:
            sum += (f-favg) * (f-favg)
        return sum / len(f_arr)

    def cov(self,x,y):
        avgx = self.avg(x)
        avgy = self.avg(y)
        sum = 0
        for i in range(len(x)):
            sum += (x[i] - avgx) * (y[i] - avgy)
        return sum / len(x)
    
    def pearson(self,x,y):
        covxy = self.cov(self,x,y)
        varx = self.var(self,x)
        vary = self.var(self,y)
        stdx = math.sqrt(varx)
        stdy = math.sqrt(vary)
        return covxy / (stdx * stdy)
    
    def linear_reg(self,points_arr):
        x = []
        y = []
        for p in points_arr:
            x.append(p.x)
            y.append(p.y)
        xavg = self.avg(x)
        yavg = self.avg(y)
        xvar = self.var(self,x)
        covxy = self.cov(self,x, y)
        a = covxy / xvar
        b  = yavg - (a * xavg)
        l = Line(a,b)
        return l
    
    def dev_1(self,p,point_arr):
        lrg = self.linear_reg(point_arr)
        return abs(lrg.f(p.x) - p.y)
    
    def dev(l, p):
        return abs(l.f(p.x) - p.y)
    
    def point_gen(x,y):
        point_arr = []
        for i in range(len(x)):
            point_arr.append(Point(x[i],y[i]))
        return point_arr
    
    
    
    
    
    
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    































