from math import *

from collections import defaultdict
my_dict = defaultdict(int)
print(my_dict)

a = my_dict["joe"]; a

print(a)
print(my_dict)



""" W11, Question 1"""
def triangle_legs(hyp, angle):
    angle1=angle
    angle2=90-angle1
    Opp1=hyp*sin(radians(angle1));Opp1
    Opp2=hyp*sin(radians(angle2));Opp2
    list1=sorted([Opp1,Opp2]); list1
    return tuple(list1)

"""W11, Question 3 """
initialvalue=input('Maximum number to factorise:')
initialvalue=int(initialvalue)
for number in range(1,initialvalue+1):
    list1=[]
    for element in range(1,number+1):
        if element==1 or element==number:
            list1.append('*')
        else:
            list1.append('-')

    for prevnumber in range(2,number):
        if number%prevnumber==0:
            list1[prevnumber-1]='*'
    output=' '.join(list1)
    output2= output+(' -'*(initialvalue-number))

    print(output2)
