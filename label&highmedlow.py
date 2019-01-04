# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 15:09:04 2018

@author: imart
"""

import pandas as pd

data = pd.read_csv("o.out",header = None)

datalist = list(data[0])

newlist =[]

newdf = pd.DataFrame(columns = ['PMCAT','Keyword','match','Probability'])


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
    
def RepresentsFloat(s):
    try: 
        float(s)
        return True
    except ValueError:
        return False

c =0 
row=0
for i in range(1,len(datalist)):
    if RepresentsInt(datalist[i]) == True:
        j = i
        newlist.append(datalist[c:j])
        c= i



for a in newlist:
    labellist =[]
    problist =[]
    count = 0
    for b in range(2,len(a)):

        if (a[b].find("__label")!=-1):
            count +=a[b].count("__label")
            
        x = a[b].split(' ')
        for y in x:
            if RepresentsFloat(y) == True or RepresentsInt(y) == True:
                problist.append(y)
                
            else:
                labellist.append(y)
    #num1 =-1
    #num2 = -1            
    for d in range(count):
        #num1 +=1
        #num2+=1
        newdf.set_value(row,'PMCAT',a[0])
        newdf.set_value(row,'Keyword',a[1])
        newdf.set_value(row,'match',labellist[d])
        newdf.set_value(row,'Probability',problist[d])
        row+=1
        
         
newdf['match'] = newdf['match'].str.replace('__label__','')