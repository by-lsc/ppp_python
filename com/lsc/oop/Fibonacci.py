#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Fibonacci(object):
    __result = [];
    
    def __init__(self):
        self.a = 0
        self.b = 1
    
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
        self.__result.append(sum)
        if(sum > 1000000):
            raise StopIteration()
        return self.a

    def __getItem__(self,n):
        pass
        #return self.__result[n]

    def count(self):
        pass

f  = Fibonacci()
print(f)
for x in Fibonacci():
    print(x)

    