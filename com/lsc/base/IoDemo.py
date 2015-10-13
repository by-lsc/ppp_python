#!/usr/bin/env python3
# -*- coding: utf-8 -*
'''
Created on 2015年10月13日

@author: lsc
'''
import os


def copyTxtFile(s,d,m):
    try:
        f = open(s,m);
        #print(f.read())
        w = open(d,'wb+')
        w.write(f.read())
        print(".......................\n",w.read())
    except Exception as e:
        print(e)
    finally:
        f.close()
        w.close()

    
#copyTxtFile("IOdemo.txt","dist.txt","r")
copyTxtFile("pic.jpg","pic1.jpg","rb") 
print(os.name)  
#os.rename('dist.txt', '111.txt')
#os.remove('111.txt')




