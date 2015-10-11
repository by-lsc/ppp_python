#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#闭包
def o_fun(*arg):
    def i_fun():
        s = 0
        for x in arg:
            s =s + x;
        return s
    return i_fun       
o_f = o_fun(1,2,3,4,5,6)
print(o_f.__name__)
result  = o_f()
print(result )