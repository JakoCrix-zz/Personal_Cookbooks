# Formatting Basics
'{}, {}, {}'.format('a', 'b', 'c')
'{2}, {1}, {0}, {0}'.format('a', 'b', 'c')
'{0}{1}{0}'.format('abra', 'cad', 'tomatoes')

# Method 1
print("{0} {0} It's off to work we go".format("Hi Ho!"))
# Method 2 (Older method)
print("%s It's off to work we go" % "Hi Ho!")
print('I own {} horses'.format(10))

'{}, {}, {}'.format('a', 'b', 'c')
'{2}, {1}, {0}, {0}'.format('a', 'b', 'c')
'{0}{1}{0}'.format('abra', 'cad')



# %% String Formatting
# %s - String (or any object with a string representation, like numbers)
print("strings: {:s}".format("9743"))
print("The quotient of {} and {} is {:.2f}".format(5,6.7,5/6.7))
print("I own {} {} horses ".format(10, "amazingly super"))\

"""{t1} and {t2}
    Agreed to have a battle;
For {t1} said {t2}
    Had spoiled his nice new rattle.""".format(t1="Tweedledum", t2="Tweedledee")

'{:.5}'.format('xylophone')


# %% Formatting Floating Point Numbers
# %d - Integers
# %f - Floating point numbers
# {:6.2f}: use at least 6 characters and use two digits after the decimal point.
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot
import math
pi= 123456.1415926
print('pi: {:2.3}'.format(math.pi))

print('{:6.2f}'.format(math.pi))
print("integer base 10: {:d}".format(9743))


# Conversios
print("strings: {1:s}".format( "Tomatoes",9743))
print("strings: {1!s}".format( "Tomatoes",9743))    # Helps to convert the integer into a string



# %% Other formats
# %b - In terms of binary numbers
# %x/%X - Integers in hex representation (lowercase/uppercase)
# %c - Unicode characters

print("binary number: {:b}".format(9743))
print("Call me on my {:c}".format(9743))  # yes, it's a telephone




# Padding
'{: >10}'.format('test')
'{:>10}'.format('test')

'{:10}'.format('test')
'{:<10}'.format('test')
'{: <10}'.format('test')
'{:_<10}'.format('test')

'{: <16}'.format('Hi')
print('{:6.2f}'.format(pi))   # pad on the left
'{0: <16}'.format('Hi')



