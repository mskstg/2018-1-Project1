# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 11:34:40 2018

@author: HTG
"""

a = 'a.bc'




def acronym(word):
    a = 'true'
    if len(word)%2 == 0:
        a = 'fasle'
    else :    
        for i in range(1, int((len(word)-1)/2)) :
            if word[2*i-1]!='.':
                a = 'false'
    return a

print(acronym(a))


    