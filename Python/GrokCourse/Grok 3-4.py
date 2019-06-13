"Methods for lists"
newlist=['Hello','World'+'World', 1,2,3]
newlist.index('WorldWorld')
newlist.append('Hello')
newlist.count('Hello')
newlist.remove('Hello')  #removes first instance of the word
newlist.reverse()

newlist=['Hello','World'+'World', 1,2,3]
newlist.insert(0,'startingover'); newlist

# removes and returns last item in list with pop
newlist.pop(); newlist
newlist.pop(1)

list1=['This','Love','has','Taken', 'its', 'toll']
'!'.join(list1)


### Worksheet 3- Conditionals
print('lo' in 'hello')
print(5 in [1,2,3,4,5])
print(5 in 10) ## note, can't do this as 10 is not iterable

print(ord('A'), ord('a'))
print((5>4), not(5>4))
print(0<4<6<7, 0>5<6)

'abs'.isalpha()
'ABCd'.isupper()
'Python'.endswith('on')

### Worksheet 4- Sequences
s='The number is 42'
s[4:-6:1]==s[4:-6]
s[::2]

# Creating Lists tricky stuff
y=['pig', 36, 'tomato']; y*2
y[2][2:]
x=[5,6,7];x
z=x+y;z
x*2

x=[1,2,3,4,5,6,7,8]
x[0]=2; x

#Tuples
x=[1,2,3,4,5,6,7,8]
y=(1,2,3,4,5,6,7,8)
x[0]=2; x
y[0]=2; y  #You cannot mutate a Tuple


# Methods of lists:
y=(1,2,3,4,5), print(type(y))
randomstring='Hello World'
x=list(randomstring)
print(x)
