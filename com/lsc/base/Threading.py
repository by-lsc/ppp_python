#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015年10月15日

@author: lsc
'''

import time, threading

# 新线程执行的代码:
def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 100:
        n = n + 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        #time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)

print("thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target=loop, name="FirstThread")
t1 = threading.Thread(target=loop, name="SecondThread")
t.start()
t1.start()
t.join()
t1.join()
print("thread %s ended." % threading.current_thread().name)