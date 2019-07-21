"""Grok 9, Dictionaries, Sets, Unions and Intersections"""
# %% Dictionary Basics
example_empty_dict = {}
my_dict = {"Age":34,"Anna":"Joe","Jobs":"Steve"}

print(my_dict.get("Age"))
print(my_dict)
print(my_dict.pop("Jobs"))
print(my_dict)

my_dict = {"Age":34,"Anna":"Joe","Jobs":"Steve"}
del my_dict["Age"]       # del removes a key:value pair without returning anything
print(my_dict)
my_dict.clear()          # clear removes all key:value pairs
print(my_dict)


# Making changes and adding new key:value pairs
capitals = {'Victoria': 'Melbie',
            'New South Wales': 'Sydney',
            'Queensland': 'Brisbane',
            'Tasmania': 'Hobart',
            'South Australia': 'Adelaide',
            'Western Australia': 'Perth',
            25: "hello"}
print(capitals['Tasmania'])
print(capitals[25])
print(capitals['ACT'])  # This is an ERROR!

capitals['Victoria'] = 'Melbourne'   # Ammending value
capitals['ACT'] = 'Canberra'         # Ammending key and values


# Accessing all keys
list(capitals.keys())
list(capitals.values())
capitals.items()   # contains tuples of the (key, value) pairs.


# %% Counting things with Dictionary
MOBY = """Call me Ishmael. Some years ago - never mind how long precisely - having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul; whenever I find myself involuntarily pausing before coffin warehouses, and bringing up the rear of every funeral I meet; and especially whenever my hypos get such an upper hand of me, that it requires a strong moral principle to prevent me from deliberately stepping into the street, and methodically knocking people's hats off - then, I account it high time to get to sea as soon as I can. This is my substitute for pistol and ball. With a philosophical flourish Cato throws himself upon his sword; I quietly take to the ship. There is nothing surprising in this. If they but knew it, almost all men in their degree, some time or other, cherish very nearly the same feelings towards the ocean with me."""
tally = {}

for char in MOBY:
    if char in tally:
        tally[char] += 1
    else:
        tally[char] = 1  # if we ioncrement a value associated with a non existent key, we get a Keyerror.
print(tally['C'])
print(tally['I'])

votes = {}
votes['Melbourne'] = 'many!'
votes['anywhere else'] += 1


