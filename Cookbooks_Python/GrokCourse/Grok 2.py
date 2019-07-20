
###############################################################################
"""Worksheet 2- Numerical Expressions
- Type of Operands; int, float, bool, str, tuple, list, dict
- Different Divisions
"""
###############################################################################
# %% Different Operands
type(True)
type("hello")
type((1.0, "hello", "frank"))
type([1.0, "hello", "frank"])
type({"bob": 34, "frankenstein": 203})

# %% Integers
type(5)
type(5.6)
print(1e5); type(1e3)
print(1.23e-2)

a = 2; b = 7
c = a + b; type(c)
a = 2; b = 7.5
c = a + b; type(c)

# %% Type Conversions- Casting
int(32.7)
float(32)
int("32")

int("32.7")
float("32.7")

print(str(32) + str(32.7))

# %% Integer Division
print(3 / 4)
print(13 // 4)    # Divide the number without the decimal
print(13 % 4)

print(3 * 4)
print((13 // 4) * 4 + 13 % 4)
print((3.1 // 1.5) * 1.5 + 3.1 % 1.5)

print(2**2)
print(3**2)
print(2**(13 % 4))


# %% Worksheet examples
RATE = 0.045
amount = int(input("How much money would you like to invest, Mr Frodo? "))
time = int(input("How many days would you like to invest this for? "))
final_amount = amount*(1+RATE/12)**(time//31)
print("After that time you will have: $"+str(final_amount))
