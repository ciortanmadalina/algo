import random
import sys
import os

print("5**2 = ", 5**2)
print("5//2 = ", 5//2)
'''
complicated comment
** exponential
// division and discard the remainder
'''

multi_line_quote = '''miu
rrr
miau'''
print("this %s %s" %( 'is', multi_line_quote))
print('\n'*2)
print("I don't like newlines ", end = "")
print("this")

my_list = ['rr', "uu"]
print("first item ", my_list[0])
print(my_list[1:2])
my_list2 = ['rr2', "uu2"]
my_list3 = [my_list, my_list2]
print(my_list3)
pi_tuple =(1,2,3)
pi_list = list(pi_tuple)
print(len(pi_tuple))

maps = {'a' : 'b', 'c':'e'}
print(maps['a'], maps.keys())


for x in range(0,10):
    print(x, ' ', end ="")

random_num = random.randrange(0,100)
print(random_num)
i=0;
while(i<=10):
    if(i==7):
        break
    else:
        i+=1

#name = sys.stdin.readline()
#print('hello ', name)
long_string = '''miau
kjdkhdfdf
kjlkjljl'''
print(long_string[0:3], long_string[-3:-1])

class Animal:
    __name = "" #private field
    __height = 0

    def __init__(self, heigth, name):
        self.__height = heigth
        self.__name = name

    def toString(self):
        return "it is {}".format(self.__name)

    def set_name(self, value):
        self.__name = value

cat = Animal(33, 'miau')
print(cat.toString())

class Dog(Animal):
    __owner = ""

    def __init__(self, owner):
        self.__owner = owner