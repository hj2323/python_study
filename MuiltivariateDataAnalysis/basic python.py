# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 19:16:54 2022

@author: hjand
"""

"""
python basic
- import libraries
- comment
- pip
- if
- for
- Functions
- class
- Read text(excel) files
- Numpy
- Pandas
"""

#'generic import' of math module
import math
math.sqrt(25)

#import a function from math
from math import sqrt
sqrt(25)

#import multiple functions at once from math
from math import cos, floor
import os
os.getcwd() #in R, getwd()
os.chdir("C:\chj\python_study\MuiltivariateDataAnalysis") 
#in R, setwd("C:\chj\python_study\MuiltivariateDataAnalysis")
import pandas as pd
bmi = pd.read_csv("bmi.csv")


# comments in line 

"""
Comments in sentences
Brian Heinold, A Practical Introduction to Python Programming, 2012.
Edouard Duchesnay, Tommy Löfstedt. Statistics and Machine Learning in Python, 2018.
"""

#help:설치된 모듈 목록 보기
help("modules") 

#pip: python패키지를 설치하고 관리하는 프로그램 

# Number
10**3              # 1,000
10 / 4                 # 2.5
10 / float(4)     # 2.5
5 % 4                    # modulo 1 - remainder
10 // 4                  # floor division 2

# Boolean operations
# comparisons (these return True)
5 > 3
5 >= 3
5 != 3
5 == 5
# boolean operations (these return True)
5 > 3 and 6 > 3 5 > 3 or 5 < 3 not False

# determine the type of an object 
type(2)	             # returns 'int' 
type(2.0)	             # returns 'float' 
type('two')	# returns 'str' 
type(True)	# returns 'bool' 
type(None)	# returns 'NoneType'

# check if an object is of a given type 
isinstance(2.0, int)  	# returns False 
isinstance(2.0, (int, float)) # returns True

# convert an object to a given type 
float(2) 
int(2.9) 
str(2.9)
# zero, None, and empty containers are converted to False 
bool(0) 
bool(None)
bool('')	# empty string 
bool([])	# empty list 
bool({})	# empty dictionary


"""
The 3 basic data types in Python are: -Tuples -List - Dictionary
**Tuples**:Tuples ar eimmutable python objects which are enclosed with paranthesis.
Immutability implies that objects cannot be added or removed to tuples. Hence we cannot add or remove elements from tuples.
However a tuple can be removed using the del() commands
**List**:List are a sequence of disimilar objects enclosed within square brackets.
Objects can be added to lists using append() and deleted using remove()
**Dictionary**: Dictionaries are a name(key)-value pair enclosed within curly braces. The name- value
pairs are separated using a ':'. The keys must be unique in the dictionary
The length of tuples, lists and dictionaries can be obtained with the len()
"""
# Tuples are enclosed in paranthesis
mytuple=(1,3,7,6,"test")
print(mytuple)
# Lists are enclosed in square bracket
mylist = [1, 2, 7, 4, 12 ]
#Dictionary - These are similar to name-value pairs
mydict={'Name':'Ganesh','Age':54,'Occupation':'Engineer'}
print(mydict)
print(mydict['Age'])
# No of elements in tuples, lists and dictionaries can be got with len()
print("Length of tuple=",len(mytuple))
print("Length of list =", len(mylist))
print("Length of dictionary =",len(mydict))

######################################
##python에서는 INDEX 0부터 시작
##R에서는 index 1부터 시작
######################################

###List
# empty list 
empty = []    
# empty = list()
empty.append(23)
empty.append(45)
empty

# list slicing [start:end:stride] 
weekdays = ['mon','tues','wed','thurs','fri'] 
weekdays[0]   # element 0 
weekdays[0:3] # elements 0, 1, 2 
weekdays[:3]  # elements 0, 1, 2 
weekdays[3:]  # elements 3, 4 
weekdays[-1]  # last element (element 4) 
weekdays[::2]  # every 2nd element (0, 2, 4) 
weekdays[::-1] # backwards (4, 3, 2, 1, 0)

# sort a list 
simpsons.sort() 
simpsons.sort(reverse=True) # sort in reverse 
simpsons.sort(key=len)       # sort by a key

# conatenate +, replicate * 
[1, 2, 3] + [4, 5, 6]
["a"] * 2 + ["b"] * 3

###Tuples
# create a tuple 
digits = (0, 1, 'two') # create a tuple directly 
digits = tuple([0, 1, 'two']) # create a tuple from a list 

# examine a tuple 
digits[2]               # returns 'two' 
len(digits)            # returns 3 
digits.count(0)  # counts the number of instances of that value (1) 
digits.index(1)  # returns the index of the first instance of that value (1)


###Dictionaries
# create a dictionary (two ways) 
family = {'dad':'homer', 'mom':'marge', 'size':6} 
family = dict(dad='homer', mom='marge', size=6)

# examine a dictionary 
family['dad']  # returns 'homer' 
len(family)      # returns 3 
family.keys()   # returns list: ['dad', 'mom', 'size'] 
family.values() # returns list: ['homer', 'marge', 6] 
family.items()  # returns list of tuples: 
                               # [('dad', 'homer'), ('mom', 'marge'), ('size', 6)] 
'mom' in family # returns True 
'marge' in family # returns False (only checks keys)

#######################################
###Conditinal Statements
#######################################
x=3
#if statement
if x>0:
    print('positive')

#if/else statement
if x>0:
    print('positive')
else:
    print('zero or negative')
    
#if/elif/else statement
if x>0:
    print('positive')
elif x == 0:
    print('zero')
else:
    print('negative')
    
#############################################    
### Loops
###########################################
#range returns a list of integers
range(0, 3) # returns [0, 1, 2]: includes first value but excludes second value 
range(0, 5, 2) # returns [0, 2, 4]: third argument specifies the 'stride'

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit.upper())

for fruit in fruits:
    if fruit == 'banana':
        print("Found the banana!")
        break # exit the loop and skip the 'else' block
    else:
        # this block executes ONLY if the for loop completes without hitting 'break'
        print("Can't find the banana")
        
count=0
while count < 5:
    print("This will print 5 times")
    count += 1 #equivalent to 'count = count +1'
    

#############################################
###Functions
#############################################

# define a function with no arguments and no return values
def print_text():
    print('this is text')
    
# call the function
print(text)

# define a function with one argument and no return values
def print_this(x):
    print(x)
    
# call the function
print_this(3)   # print 3
n = print_this(3)   # print 3, but doesn't assign 3 to n

# define a function with one argument and one return value
def square_this(x):
    return x**2

# call the function
square_this(3) # print 9
var = square_this(3) # assign 9 to var, but does not print 9
    
# default arguments 
def power_this(x, power=2): 
    return x ** power

power_this(2) # 4 
power_this(2, 3) # 8

# return two values from a single function 
def min_max(nums): 
    return min(nums), max(nums)

# return values can be assigned to a single variable as a tuple 
nums = [1, 2, 3] 
min_max_num = min_max(nums) # min_max_num = (1, 3)
min_max_num[0]
min_max_num[1]

min_num, max_num = min_max(nums) 
min_num
max_num

# Create a lambda function to add 2 numbers 
add_fct = lambda x,y:x+y

add_fct(a,b)
Out[12]: [5, 2, 3, 1, 7, 1, 5, 4, 6, 8]


#############################################
###Object oriented programming(OOP)
#############################################
import math
# Inheritance + Encapsulation
class Square():
    def__init__(self, width):
        self.width = width
        
    def area(self):
        return self.width **2
    
class Disk():
    def__init__(self,radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
shapes = [Square(2), Disk(3)]

# Polymorphism
print([s.area() for s in shapes])

#############################################
###Read text file using pandas
#############################################
import os
import pandas as pd
import matplotlib.pyplot as plt
# Set the current working directory 
os.chdir("c:/data/pydata")
os.getcwd()     # 'c:\\data\\pydata'
# data = pd_read.csv("c:/data/pydata/bmi.csv")
data = pd.read_csv("bmi.csv")
data.head()

weig = data['weight']
heig = data['height']
bmi = weig/(heig/100)**2
plt.scatter(heig, weig)
plt.show()


#############################################
###Read Excel file using pandas
#############################################
import os
import pandas as pd
import matplotlib.pyplot as plt
# Set the current working directory 
os.chdir("c:/data/pydata")
os.getcwd()     # 'c:\\data\\pydata'
beer = pd.read_excel("beer.xlsx", sheet_name='Beer')
beer.head()
beer['cost']   # beer.cost

"""
Numpy is one of the most fundamental package for scientific computing with Python.
Numpy includes the support for handling large, multi-dimensional arrays and matrices,
along with a large collection of high-level mathematical fucntions to operate on these arrays.
"""

import numpy as np
# Create 1d numpy array
data1 = [6,7,5,8,0,1]

arr1 = np.array(data1)
print(arr1)

# Create numpy array in a single line
import numpy as np
arr1= np.array([6, 7.5, 8, 0, 1])
#Print the array
print(arr1)
### 2D array
#Create a 2d numpy array
import numpy as np
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
# Print the 2d array
print(arr2)

