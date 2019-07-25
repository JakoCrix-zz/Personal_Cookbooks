from collections import defaultdict

# %% Dictionaries vs DefaultDictionaries
my_dict = {}   # Normal dictionary usage:
my_string = "I want to go home now"
for char in my_string:
    if char in my_dict.keys():
        my_dict[char]+=1
    else:
        my_dict[char]=1
print(my_dict)   # A frequency count of the letters in my_dict.


# Default Dictionary:
# the default value is usually the "zero value" of a type —
# for list, the empty list [];
# for str, the empty string "";
# for int, 0; for float, 0.0;
my_dict = {}
my_dict["joe"]

my_dict = defaultdict(int)  # create a default dictionary
print(my_dict)
a = my_dict["joe"]          # try to access the element "joe" which is not in it.
print(a)                    # notice the value that was returned and that it was added to the dictionary.
print(my_dict)


# The long code now becomes:
my_dd = defaultdict(int)
my_string = "I want to go home now"
for char in my_string:
    my_dd[char] += 1
print(my_dd)

