#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#默认参数 必选参数在前，默认参数在后
def fu1(name,age,sex,phn,addr='sz',L=[]):
    L.append('end')
    print(name,age,sex,phn,addr,L)
fu1("lsc",25,1,"137xxxxxxxx",'gx',[1,2,3])
'''for i in range(10):
    fu1("lsc",25,1,"137xxxxxxxx",'gx') #List默认应该用None
'''

#可变参数
def fu2(*arg):
    print(len(arg),arg)
fu2(1,2,'qq');
l = ["把","他","们","吹","飞"]
fu2(l)  #长度是1，直接打印是只有一个元素的tuple

#关键字参数
def fu3(**kw):
    kw["end"] = "e"
    if 'l' in kw:
        kw["l"].append("modify") #由此可见，**kw是浅复制
    print(kw)
fu3(name="n1",age='11')
extra = {'city': 'gx', 'job': 'whiteEat','l':l}
fu3(**extra)
print("after modifying the list -->",extra)
    