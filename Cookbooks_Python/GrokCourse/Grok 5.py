# Creating Functions
def function1(x, y):
    return x*y

function2=lambda x, y: x*y

function1(5,2)
function2(5,2)


#FOrmat specifiers
print('This is the original sentence')
print('I own {} horses'.format(10))
import math
print('pi: {}'.format(math.pi))
print('pi: {:2.3}'.format(math.pi))

'{}, {}, {}'.format('a', 'b', 'c')
'{2}, {1}, {0}, {0}'.format('a', 'b', 'c')
'{0}{1}{0}'.format('abra', 'cad')

print('string: {:s}'.format('hello'))
print('binary number: {:b}'.format(9743))
print('inteder base 10: {:d}'.format(9743))
