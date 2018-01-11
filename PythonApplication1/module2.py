# -*-coding:utf-8 -*-
'a test module'

__author__='wang'
__version__='V1.0'


import sys

def _private_1(name):
    return 'hello,%s'%name
def _private_2(name):
    return 'Hi ,%s'%name

def test(name):
    '''
    This is a test Prog
    __doc__属性的使用

    %s的使用

    '''

    args=sys.argv
    if len(args)==1:
        print("Hello,world")
    elif len(args)==2:
        print("hello %s"%args[1])
    else:
        print("too many arguments")
    _private_1(name)
    _private_2(name)
#class use execerse1
class student(object):
    def __init__(self, name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))
bart=student('jack',100)
lisa=student('lasa',90)
bart.print_score()
lisa.print_score()

#class use execerse
class student1():
    def __init__(self, name,gender,score=100):
        self.__Name=name
        self.__Gender=gender
        self._Score=score
    def get_gender(self):
        return self.__Gender
    def set_gender(self,newGender):
        self.__Gender=newGender
def classUse():
    jack=student1('jack','male')
    lucy=student1('lucy','female')

    print("the original gender is %s"%jack.get_gender())
    jack.set_gender('female')
    print("the present gender is %s"%jack.get_gender())

#classUse()

#class descent use execerse
class animail():
    def eat(self):
        print("the animal can eat!")

class cat(animail):
    def eat(self):
        print("the cat can eat")
class dog(animail):
    def eat(self):
        print("the dog can eat")

def aniFunc():
    cat1=cat()
    dog1=dog()

    cat1.eat()#可以调用父类的函数
    dog1.eat()

#aniFunc()

def multSt(animail):
    print("the follow line is another use")
    animail.eat()
cat2=cat()
#multSt(cat2)


