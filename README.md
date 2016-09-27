## Getting Started

Mininet requires some knowledge of python. This readme covers some important components of python which you will need to 
get started with mininet.

Main reference for this tutorial: [Tutorials Point](http://www.tutorialspoint.com/python/)

## Motivation
If you know english then you know python. Yes it's that simple.* Terms and conditions applied ;) 

## The basics
Assuming that you have already installed python. Let's write our fast program to check if python is working properly or 
not. For installation instructions you can refer to the tutorials point link which I gave above.
```py
# hello.py
print "Hello World"

# Run it in terminal: 
python hello.py
```
Once you are through that, let's go ahead. 

```py
a = 1
a = "john"

# You can see that this wont raise any type errors unlike java or C/C++
```

### String in python
```py
#!/usr/bin/python

str = 'Hello World!'

print str          # Prints complete string
print str[0]       # Prints first character of the string
print str[2:5]     # Prints characters starting from 3rd to 5th
print str[2:]      # Prints string starting from 3rd character
print str * 2      # Prints string two times
print str + "TEST" # Prints concatenated string

'''
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST

'''

```

### Decision making. (If else)
```py

# Basic syntax

if <condition>:
    print "If"
else:
    print "Else"


if <condition>:
    print "If"
elif <condition>:
    print "Elif"
else:
    print "Else"

# An example of single line if statement.
var = 100
if ( var  == 100 ) : print "Value of expression is 100"

```
### List in python
```py
# You can consider it as analogous to an array which can store any data type.
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"]

# Printing value
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]

# Updating value
print list[2]
list[2] = 2001;

# For other advanced usage refer to tutorialspoint. 
```
### Dictionary in python
```py
# Key, value pair.
# hash. O(1) access time.
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']

```
### Functions
```py
# Basic syntax for a function
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]
   

def advanced(*params):
    return sum(*params)

l = [x for x in range(1, 101)]
print advanced(l)
# Why should I care about this? 
# Sometimes in a function you have to pass many arguments, sometimes not so many for the same function.
```
### Loops
For understanding loops I strongly recommend you to look these articles
https://www.tutorialspoint.com/python/python_for_loop.htm
https://www.tutorialspoint.com/python/python_while_loop.htm

### Class 
```py
# TODO: 
'''
Explain the importance of self.
Class variables
Object variables
__init__ 
'''
class Employee:
   'Common base class for all employees'
   empCount = 0 # This is a class variable

   def __init__(self, name, salary):
      # All the variables defined by self.* are object variables
      # They will be different for all instances of a class.
      self.name = name
      self.salary = salary
      Employee.empCount += 1 #empCount is a class variable and hence is not getting accessed by self.* notation 
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
      
      
"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

# Please note that this is a very very brief intro to classes but this should be enough to get you started for mininet.
```

### That's it. 
You have successfully covered most of the python which you will require for understand mininet. Rest I may explain in a
video later. You can refer to all *.py examples to understand mininet code as well. I have written a lot of comments 
which can help you understand the code better. 