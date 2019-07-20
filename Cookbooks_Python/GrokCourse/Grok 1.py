###############################################################################
"""Worksheet 1- Introductory Exercises"""
###############################################################################
# %% Basic Strings
print('Tomatoes'+ 5*'And' + 2*'Ice Cream')
print("Hello, world")
print("Hello" + "World")
print('Hi' + 'Hi' + 'Hi')
print('CEGCEG' + 36*'E' +24*'C')

# %% Variables
message = "Hello world"; print(message)
msg = 'Hi'
num = 3
print(msg * num)

# %% Inputs; Inputs always return strings
name = input("What is your name? ")
age = input("What is your age? ")
print("I know that", name, "is", age, "years old!")

type(name)
type(age)

num = input('Enter a number to double: '); num          # Wrong!
print('2 x', num, '=', 2 * num)
num = float(input('Enter a number to double: ')); num   # Right!
print('2 x', num, '=', 2 * num)


# Other examples
weight= float(input('Enter weight in grams: '))
weight= weight/1000
print(str(weight)+'kg')
