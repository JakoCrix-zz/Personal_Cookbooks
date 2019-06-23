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


randomstring='Hello World'
x=list(randomstring)
print(x)
