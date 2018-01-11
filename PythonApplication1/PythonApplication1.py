#-*- coding:utf-8 -*-
import sys as sysLib
from collections import Iterable
from  module1 import resolve
from module1 import func2#不推荐这种导入方式易发生重名，推荐使用import或from...import *
from module2 import *#这种方式会导入全部公共名称，但不会导入__version__这种双划线起头的名称
import module3
import module4
import module5


#this is a comment

print("hello world")
a=True
if a ==True:
	print("the a is True")
elif a==2:
   pass
else:
	print("a is not True")
#list learning
classmate=['jame','luch','cick']
for number in classmate:
    print(number)
print("the classmate length is ",len(classmate))
a=classmate.pop()
print(a)
#tumple learning
#tumple ???????????????append/insert????è???è??ì???????????????
teacher=("wang","jack","davide")
t=()
t1=(1,)

#loop learn

#func learning
def abstest(c):
    print("the functiong is abstest")
    print(abs(c));
    pass
abstest(-2)

def func_use():#module的使用import

    [x1,x2]=resolve(1,6,9)
    print("*********")
    print(x1)
    print(x2)
    [x3,x4]=resolve()
    print(x3)
    print(x4)
    [x5,x6]=resolve(0,1,2)
    print(x5)
    print(x6)
    print("*********")

    #func2 ????????????è???
    lst=[1,2,3]
    print("single value is in")
    result=func2(1,2,3)
    print(result)
    print("list is in")
    result=func2(*lst)
    print(result)



def func_coding():
    str1='abc'
    str2='cde'
    biStream1=str1.encode('ascii')
    biStream2=str2.encode('utf-8')
    print(biStream1)#output is :b'abc'
    print(biStream2)#output is :b'cde'
    print(biStream1.decode('ascii'))#output is :abc
    print(biStream2.decode('utf-8'))#output is :abc
    print("中文正常显示，需要首行设置和文本保持设置均为utf-8")

    print("当前%s的成绩是%d"%('jame',100))#注意和C不同的是没有逗号
    print("这个例子只有一个参数：%s"%'AC')
    print("当前%s的成绩是%s"%('jame',100))#任意均采用%s

    print("the num is {0:2.2f}%,{1:.2f}%".format(200.0,300.0))

#func_coding()


#high level use
def funcSlice():
    l=list(range(100))
    print(l[:10])

    isinstance([1,2,3],Iterable)#判断是否可迭代

    L1=[X*X for X in range(1,11)]#列表生成式
    L2=[X*X for X in range(1,11) if X%2==0]
    L3=[M+N for M in 'abc' for N in 'xyz']
    L4=['HELLO','WORLD',18,'APPLE',None]
    L5=[]
    print(L1)
    print(L2)
    print(L3)

    for st in L4:
        if isinstance(st,Iterable)==True:
            L5.append(st.lower())
        else:
            L5.append(st)
    print(L5)

#funcSlice()
def gen():
    l=[x*x for x in range(10)]
    g=(x*x for x in range(10))#生成器
    print(l)
    print(next(g))
#gen()

def moduleUse():
    print(module2.__author__)#特色变量
    print(module2.__doc__)#特殊变量
moduleUse()

if __name__=='__main__':
    moduleUse()