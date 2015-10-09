#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Animal(object):
    
    __name = ""
    def __init__(self):
        self.__name 
        
    def run(self):
        print(self.getName()," is running...")
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name
        
        
        
        
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        
a = Dog()
a.setName("dog")
print(a.getName());
a.run()
