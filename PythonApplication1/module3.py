#-*- coding:utf-8 -*-
class Student():
    #__slots__ =('name','score')#限制实例属性只有name和score，对子类不起作用
    pass

def test():
    s=Student()
    s.name='michale'
    s.age=10
    print("this is module 3",s.name)

#test()

class Student1():
    
    def __init__(self,value):
        self._value=value

    def __str__(self):
        return 'this is a comment'
    
    def __getitem__(self,n):
        return n+1


    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if (value<0):
            print("value is below 0")
        else:
            self._score=value
def func2():
    s=Student1(10)
    s.score=90
    print(s.score)
    s.score=-20
    print(s.score)

    print(s)#可直观返回对象的描述
    print(s[3])#输出为：4
func2()



