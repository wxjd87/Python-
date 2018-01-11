import math
def resolve(a=1,b=4,c=4):
    if a==0:
        print("there is only one resolve")
        return -c/b,None
    elif (b**2-4*a*c)<0:
        print("there is no ansower")
        return
    else:
        return (-b+math.sqrt((b**2-4*a*c)))/2/a,(-b-math.sqrt((b**2-4*a*c)))/2/a
 

def func2(*num):
    sum = 0
    for n in num:
        sum = sum+n*n
    return sum