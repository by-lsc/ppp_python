#字符串
author = "lsc"
#输出
print("hello python..."+author);
#list & tuple
list1 = ["I","have","a","target","!"]  #
tuple1 = ("ready","to","word");  #final
print("list: ",list1)
print("tuple: ",tuple1)
#dict(map)
num = {"one":1,"two":2,"three":"3"};
print("dict: ",num)
num["one"] = 0
print("get by key 'one':",num["one"])

#input
birth = input("please input you age:")
age = int(birth)
#if..else
if(age <= 12):
    print("blue cat 3000 question")
elif(age <18):
    print("英语听力...")
else:
    print("you can you up,no can no bb")
 
#循环
for x in range(10):
    print(str(x)+"  ",end="")

