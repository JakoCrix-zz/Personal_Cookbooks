"""Grok 9, Sets"""
### Sets
my_set1 = set()
print(my_set1)
my_set2 = {"a", "b", "c"}
print(my_set1, my_set2)

my_set3 = {"a", "b", "c", "a", "a"}
print(my_set3)

my_set={"a", "b", "c", 1}
print("a" in my_set)
print(True in my_set)

my_sequence = "hello"
my_set = set(my_sequence);my_set
print(my_set)

my_set1 = {2, 3, 4}
my_set2 = {2, 5}
print("my_set1-my_set2", my_set1 - my_set2)
print("my_set2-my_set1", my_set2 - my_set1)
#union and intersection
print("Union: my_set2|my_set1", my_set2 | my_set1)
print("Intersection: my_set2 & my_set1", my_set2 & my_set1)
