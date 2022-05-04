#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
num = int(input())

def goodness(st):
    g = 0
    n = len(st)
    for i in range(0,math.floor(n/2)):
        if st[i]!=st[n-i-1]:
            g = g + 1
    return g        

for i in range(num):
    N,K  =  map(int,input().split())
    sample = input()

    score = goodness(sample)
    print(score)
    if score == K:
        minop = 0
        print('Case #'+ str(i+1)+ ' :', 0)
    elif score < K:
        minop = K-score
        print('Case #'+ str(i+1)+ ' :',(minop)) 
    else:
        minop = -K+score
        print('Case #'+ str(i+1)+ ' :',(minop))

