print('Hello world!')

# This is my comment
# To-So I need add some functionally right here later

#  let's talk about variables real quick 

xlksdjflkdshfl = 5
print(xlksdjflkdshfl)

print(type(xlksdjflkdshfl))


# Data types
# Intergers

num1 = 10

# Float
num2 = 5.0

print(num1)
print(type(num1))

print(num1,num2)
print(type(num1), type(num2))

#Math Operations:
#Add +
sum = 10 + 10
print(sum)

#subtract -
sub = 20 - 5
print(sub)

# Multiplication *
prod = 5 * 5
print(prod)

# Divide /
div1 = 25 / 5
print(div1)
print(type(div1))

#Floor Division //
div2 = 25 // 5
print(div2)
print(type(div2))

div3 = 26 // 5
print(div3)
print(type(div3))

# Modulo %
mod = 25 % 5
print(mod)

mod1 = 30 % 5
print(mod1)
print('\n\n')

# odd or even? ANYTHING % 2 ==0 is even, otherwiae it's odd
print(65 % 2 == 0)
#type AND value equality 
# = this symbol represents assigning a value
# == this is a equality check
# != this is NOT equal
#           a note on the double equals we are checking TYPE and VALUE equality

print('5' == 5)

# Another side-note 'protected' terms-convert to int
print(int('5'))

# int = 56
# print(int('5')) - means we have to be vary careful with a naming convention

# let's talk about strings!
print('\n\nSTRINGS:')

# single or double quotes are fine:
string1 = 'this is a string'
string2 = "so is this eiworu@!#$%^*U()I)?><!!!"
# Watch your single and double quotes!
# st3 = 'so's this! 
string3 = "so's this!"
string4 = 'that is so "last year".!'
string5 = 'so\'s this' #the escape charater is telling python to ignore the special behavior of the character
print(string5)

# some things about strings
# string are IMMUTEABLE!  Also ordered, also iterable
print(string1[3])
print(string1[3].upper())
print(string1.upper())
print(string1.lower())

# Another sidebar
# Functions and Methods
# Function: a function (should)work on anything regardless, take a whatever data
# where as a method only works on a particular(specific) class
# In short, functions are general wehere as methods are specifics to the class 

# Here in the above example print(string1.lower())here when we put the cursor in print
# it shows as function but when we put the cursor in .lower()it shows method.

# Manipulating strings
# 2 pieces:
# 1. concatenation - join or combine two or more data together
st7 = string1 + string2
print(st7)

st8 = string1 + ' ' + string2 +' '+ string5 + ' ' '/and why not more?/' + string3
print(st8)

# Interplation:- we'll just call f-strings here!
# where this interplation is coming handing later first you see in functions and stuffs like that but 
# imagine building the webpage that your using to do with python with some functionality. 
# if you want to show exactly what you what to show and we can put where in the sentence or paragraph fstring function is useful.

interp = f"This is also just a string except I can throw it python stuff like this -->{mod1}<-- yay the integer print!!!"
print(interp)

num3 = 23976843758932
interp2 = f"This is also {num1} just a string except {num2} I can throw it python {num3}stuff like this -->{mod1}<-- yay the integer print!!!"
print(interp2)


# lets talk about  strings!
# print('\n\nStrings:') 

#lists!
print('\nLISTS:')
# list are:
#ordered (indeexed), dynamic, muteable

a_list = []
print(a_list, type(a_list))
nums_list = [1,2,3,4,5]
print(nums_list)
r_list =['a', 1, 5.0, None, True, []]
print(r_list)
print(r_list[3])
print(r_list[2])
print(len (r_list))

# Function vs method syntax 
#      function call and input /arguments
# myfunction(myargument) vs datatype.method(myargument)
# METHODA:
#append
a_list.append(5)
print(a_list)
a_list.append(10)
print(a_list)
a_list.append(50)
print(a_list)
a_list.append(2)
print(a_list)
a_list.append(False)
print(a_list)

#pop():
#  takes out the last item of the list

r_list.pop()
print(r_list)
# but there's more for pop!
#we can store it to a variable, and also there is an OPTIONAL parameter to specify which position to pop from
a = r_list.pop(0)
print(a)



# looping 
print('\nLOOPING:')

print(a_list, r_list)

print('The standard for loop-->')
# for loop
# syntax    for item in items:
#                this is the code block to execute on each step
for r in r_list:
    print(r)

for a in a_list:
    print(a)

# range function --> frange (start, stop, step)
for x in range(0,5,1):
    print(x)
print('\n')
for x in range(5):
    print(x)
print('\n')
for x in  range(10,4,-1):
    print(x)
print('\n')
for x in range(5):
    print('this is 5 steps')


#True tree:
#T and T == True
#T and F ==





