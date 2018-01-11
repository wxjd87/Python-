#-*- coding:utf-8 -*-
import json

number=[2,3,4,5,6]
filename='numbers.json'

def funWJson():
    print("the JSON func is executing。。。。。",end=' ')
    with open(filename,'w') as f_obj:
        json.dump(number,f_obj)

def funRJson():
    with open(filename,'r') as f_obj:
        numbers=json.load(filename)
    print(numbers)
