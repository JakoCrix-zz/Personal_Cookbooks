"Methods for lists"
randomstring='Hello World'
x=list(randomstring); print(x)

# %% Basic Lists methods
newlist=['Hello','World'+'World', 1,2,3]
newlist.index('WorldWorld')
newlist.append('Hello')
newlist.count('Hello')
newlist.reverse()

newlist=['Hello','World'+'World', 1,2,3]
newlist.insert(0,'startingover'); newlist

list1=['This','Love','has','Taken', 'its', 'toll']
'!'.join(list1)


# %% Insering, removing and pop
newlist=['Hello','World'+'World', 1,2,3]
newlist.insert(0,'startingover'); print(newlist)    # inserts as the element 0 of the list

newlist=['Hello','World'+'World', 1,2,3]
newlist2=newlist.pop(); print(newlist)              # removes and returns last item in list
print(newlist2)
newlist=['Hello','World'+'World', 1,2,3]
newlist3=newlist.pop(1); print(newlist)             # removes and returns the first element in the list
print(newlist3)

newlist.remove('Hello')                             # removes first instance of the word

my_list = [1,2,5,4]   # Think about this, why does this happennn!
for i in my_list:
    my_list.remove(i)
    print(my_list)
print(my_list)

