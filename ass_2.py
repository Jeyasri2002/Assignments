# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:44:01 2023

@author: Dell
"""

def CountDigitOne(n):
    count=0
    i=1
    while i <= n:
        count += (n//(i*10))*i + min(max(n%(i*10)-i+1,0),i)
        i *= 10
    return count

n=int(input("enter"))
total_no=CountDigitOne(n)
print(f"total number of digits from 0 to {n} are ",total_no)
    
                                
                                  
    