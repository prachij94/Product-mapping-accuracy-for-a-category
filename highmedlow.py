# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 15:49:12 2018

@author: IMART
"""

l=0
import unicodecsv
import csv
import os

path = "C:\\Users\\IMART\\Desktop\\Keywords"
b=[]
b.append(['ProductName','McatId','McatName','McatAccuracyLevel'])
count = 0
files = os.listdir(path)[:-2]
for filename in files:
    a = []
    str1 = "./Keywords/"+str(filename)
    #str1 = "./KeywordsExample/data_1530179304.csv"
    f = open(str1)
    
    csv_f = csv.reader(f)
     
    count+=1
    
    for row in csv_f:
      a.append(row)
    
    numofrows = len(a)
    
    
    

    
    
    
    longestrow = max(a,key=len)
    longestrowlength = len(longestrow)
        
    #to find and delete blank rows in data 
    
    a = [x for x in a if x != []]
    
    #cleaning the data as required  
    
      
    numofrows = len(a) 
    #num1=1
    for num1 in range(1,numofrows): 
            
        
        #replace %20 with space in the Product name
        if(a[num1][0].find('%20')!=-1 ):
            a[num1][0] = a[num1][0].replace('%20',' ')
        
        
            
            
        
        
        numofrows = len(a)
    #removing the unrequired extra columns from the data
    #num=1
    for num in range(0,numofrows):  
        
        del(a[num][3:5])    
    numofrows = len(a)   
        
    #l=longestrowlength
    
    
    fh = open("C:/Users/IMART/Desktop/finaloutput.csv","wb")
    csv_out = unicodecsv.writer(fh, encoding='utf-8')
    
    cttr=1#row no counter
    
    while cttr< len(a):
        ctr=0 
        
        # this tells how many mcats in one row
        #iterates over rows
        l=len(a[cttr])
        for i in range(1,l,3):
            
            if a[cttr][i]=='':
                break
            else :
                ctr+=1
        
        #appends data to the final list
        for i in range(ctr):
            b.append(['']*4)
            # print(len(b))
            b[len(b)-1][0]=a[cttr][0] #prints the product name, no of times =  no. of mcats
            b[len(b)-1][1:4]=a[cttr][3*i+1:3*i+4] 
        cttr+=1
        # print(1)
        
    # except:pass
    for k in b:
        csv_out.writerow(k)
    f.close()
    fh.close()