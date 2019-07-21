"""Grok 8, Mutability and Advanced Sequences"""
# %% Mutability
my_list = [1,0]
print("id of my_list:", id(my_list))
print(my_list)
my_list[0] = 3; print(my_list)
print("id of my_list:", id(my_list))         # For a list, the id remains the same while the value changes

my_int = 5
print("my_int:",my_int)
print("Id:", id(my_int))
my_int = 5+1           # Generally, when we perform operations, we create a new object
print("my_int:",my_int)
print("Id:",id(my_int))                       # For an integer, the id of the object changes.


my_tuple = (7,[])
print("ids of items in tuple:", id(my_tuple[0]),id(my_tuple[1]))
my_tuple[1].append("hello")                  # Making changes to our list (which is allowed)
print(my_tuple)
print("ids of items in tuple:", id(my_tuple[0]),id(my_tuple[1]))


# %% Mutability and Assignment
print(id(5))
q = 5
print(id(q), id(5))        # The 'object' now pointed to by the variable q.


list1 = [1, 2, 3]
print("The id of the object pointed to by list1:", id(list1))  # point list1 to an object
list2 = list1                                                  # They now both point to the same object
print("The id of the object pointed to by list2:", id(list2))
list1.append(8); print(list1, list2)



"""Sorted Words
Things learned: a sorted list does not equal a non-sorted list """
def sorted_words(wordlist):
    result=[]
    for word in wordlist:
        list1=[]
        for letter in word:
            list1.append(ord(letter))
        if sorted(list1)==list1:
            result.append(word)
    return sorted(result)
