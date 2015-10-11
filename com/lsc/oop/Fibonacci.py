#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import count
class Fibonacci(object):
    __result = [];
    
    def __init__(self):
        self.a = 0
        self.b = 1
        for x in range(30):
            result = self.count(x)
            if(result > 1000000):
                break;
            self.__result.append(result)
    
    def __str__(self):
        return "this is a class for fibonacci"
    __repr__ = __str__
    
    def __iter__(self):
        return self
    
    def __next__(self):
        #self.a, self.b = self.b, self.a + self.b
        sum = self.a + self.b
        self.a = self.b
        self.b = sum
        if(sum > 1000000):
            raise StopIteration()
        return self.a
    
    #直接计算好存放在一个数组里
    '''
    def __getitem__(self,n):
        if(n < len(self.__result)):
            return self.__result[n]
    '''        
    
    #每次计算一次
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
    
    def count(self,n):
        if(n == 1 or n == 0):
            return 1;
        return self.count(n-2) + self.count(n-1)

print("function toString..............................................")
f  = Fibonacci()
print(f)
print("Iteration......................................................")
for x in Fibonacci():
    print(x,end=" ")
print("\ngetItem by index...............................................")
for x in range(100):
    print(f[x],end=" ")


    