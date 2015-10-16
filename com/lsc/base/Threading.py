#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on 2015年10月15日

@author: lsc
'''

import time, threading

n = 0;
lock = threading.Lock()
# 新线程执行的代码:
def loop():
    print("thread %s is running..." % threading.current_thread().name)
    #n = 0
    global n
    while n < 100:
        n = n + 1
        n = n - 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        #time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)

def addLock():
    lock.acquire()
    loop()

'''
print("thread %s is running..." % threading.current_thread().name)
t = threading.Thread(target=loop, name="FirstThread")
t1 = threading.Thread(target=loop, name="SecondThread")
t2 = threading.Thread(target=loop, name="ThirdThread")
t.start()
t1.start()
t2.start()
t.join()
t1.join()
t2.join()
print("thread %s ended." % threading.current_thread().name)
'''
balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)