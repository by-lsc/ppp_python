'''
Created on 2015年10月12日

@author: lsc
'''
import logging


#!/usr/bin/env python3
# -*- coding: utf-8 -*
def divWithOutException(m,n):
    return m/n

def divWithException(m,n):
    try:
        m/n
    except Exception as e:
        logging.exception(e)

def nullException(l = None):
    try:
        l [10]
        print("...................try........................")
        return "in try"
    except BaseException as e:
        print("...................Except........................",e)
        return "in except"
    finally:
        print("...................finally........................")
        return "in finally"

print(nullException())
divWithException(1, 0)
print("continue......................")
divWithOutException(1, 0)
print("no continue..................")