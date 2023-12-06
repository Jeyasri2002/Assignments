# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 19:29:31 2023

@author: Dell
"""

def len_of_last_word(s):
    word=s.split()
    if not word:
        return 0
    return len(word[-1])

inp_str= len_of_last_word(input("enter: "))
print("length of last word is",inp_str)