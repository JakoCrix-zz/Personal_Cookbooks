###############################################################################
"""Worksheet 4- Sequences
-
"""

# %% Individual elements
s = "The number is 42."
print(s[0])     #Note the 0 offset
print(s[1])
print(s[17])
print(s[-1])
print(s[-3])
print(s[-17])
len(s)

# %% Slicing
s = "The number is 42."
print(s[1:6])
print(len(s))
print(s[0:len(s)])
print(s[4:-7])
print(s[-6:len(s)])


s = "The number is 42."
print(s[:5])
print(s[5:])
print(s[:])

s = "abcdef"
print(s[::2])
print(s[0:3:2])
print(s[2::-1])
print(s[2:0:-1])
print(s[-4:-6:-1])

# Note that if the third number is negative, the direction of the indices must be changed tooo!
# We can't do [3:5:-1] as the result will be 3,4,5 and we can't go backwards.
print(s[3:5:-1])
print(s[0:2:-1])

s='The number is 42'
s[4:-6:1]==s[4:-6]
s[::2]


# %% An example of a phrase
phrase = "This is a random phrase"
if phrase and phrase[0].lower() in 'aeiou':
    print("an", phrase)
else:
    print("a", phrase)


# %% Lists
empty = []
my_words = ['pig','pineapple','panoply','polyp']
my_costs = [5.0, 12.0, 200000000.59]
my_jumble = ['jumbly', 'wumbly', 'number', 5]
print(my_costs)

my_jumble = ['jumbly', 'wumbly', 'number', 5]
print(my_jumble)
print(my_jumble[1])
print(my_jumble[-1])
print(my_jumble[:1:-1])

my_jumble = ['jumbly', 'wumbly', 'number', 5]
print(len(my_jumble))

my_jumble = ['jumbly', 'wumbly', 'number', 5]
print(len(my_jumble))
print(my_jumble[9])


# %% Lists Operations
my_string = "Sufjan" + " Stevens"
print(my_string)
my_list = [1, 2, 3] + [4, 5, 6]
print(my_list)

my_string = "haha" * 5
print(my_string)
my_list = [1, 2, 3] * 5
print(my_list)

my_string = "haha"
print("a" in my_string)
my_list = [1, 2, 3]
print(1 in my_list)

# Creating Lists tricky stuff
x=[1,2,3,4,5,6,7,8]
x[0]=2; x


# %% Tuples
# This is essentially the same as a list in that it can contain any combination of objects,
# but it can't be changed after creation (it is immutable — more on this in Worksheet 8)
empty = ()
print(len(empty))
single = (3,)
print(len(single))

my_tuple= ('height', 3, 'age', 70)
print(my_tuple)
print(my_tuple[1])
print(my_tuple[-1])
print(my_tuple[:1:-1])


y=['pig', 36, 'tomato']; y*2
y[2][2:]
x=[5,6,7];x
z=x+y;z
x*2

#Tuples
x=[1,2,3,4,5,6,7,8]
y=(1,2,3,4,5,6,7,8)
x[0]=2; x
y[0]=2; y  #You cannot mutate a Tuple


# example
suspects = [("Max Zorin", "Kills with guns", "Chip Tycoon"),("Hugo Drax",), ("Jaws", "Bites people", "Mutant"),\
            ("Nick Nack", "Really short"), ("Le Chiffre", "Good at poker", "Really evil"),\
            ("Francisco Scaramanga", "Has a Golden Gun", "Probably will melt"), \
            ("Mr Big", "Also the name of a rock band", "Dictator of San Monique")]

idx=int(input("WHO DID IT HUGO!? "))

if idx==7:
  idx_length= len(suspects[0])
  print("It was "+ suspects[0][0])
  print("Data: "+ str(suspects[0][1:idx_length]))

else:
  idx_length= len(suspects[idx])
  print("It was "+ suspects[idx][0])
  print("Data: "+ str(suspects[idx][1:idx_length]))
