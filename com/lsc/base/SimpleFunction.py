#!/usr/bin/env python3
from operator import itemgetter


#Java风格....
def bubbleSort(arr):
    if not isinstance(arr, list):
        pass
    l = len(arr)
    for x in range(l - 1):
        for y in range(l-1,x + 1,-1):
            if(arr[y] <= arr[y - 1]):
                l = arr[y]
                arr[y] = arr[y - 1] 
                arr[y - 1] = l
    for x in range(l):
        print(arr[x],'  ',end="")

arr = [1,2,4,12,52,53,13,25,97,6,44]
bubbleSort(arr)
#内置高阶函数
print()
arr1 = [7,22,9,32,20,51,98,15,8,61,10]
sorted(arr1)
print(sorted(arr1))

#习题 
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print("by_name:",sorted(L))
print("by_score:",sorted(L,key = itemgetter(1),reverse = True))
