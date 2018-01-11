# -*- coding:utf-8 -*-
import logging#logging不会抛出错误，而且可以输出到文件

#logging.basicConfig(level=logging.info)

l=[1,2,3]
dicts={'a':'VA',
     'b':'VB',
     'c':'VC'}

def dictUse():
    for dict in dicts.keys():
        print("the dict is %s" % dict.title())#不是dict.value（）
    for dict1 in dicts.items():
        print("%s"% dicts)
dictUse()

def f(x):
    return x*x

def cal():
    print("this is dem map:")
    print(list(map(f,l)))

#cal()


#exception using
def bar(s):
    assert s!='0','s is zero'
    return 10/int(s)

def main():
    try:
        print("this is main")
        bar('0')
    except Exception as e:
        logging.exception(e)
    finally:
        print("exe finally func")
#main()