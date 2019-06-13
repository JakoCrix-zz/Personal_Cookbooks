## What is a default dictionary
from collections import defaultdict
some_string="Boaty mcBoatFace."



tally2= defaultdict(float)
some_string="Boaty mcBoatFace."
for x in some_string:
    tally2[x]+=1
tally2

tally=defaultdict(list)
for i in range(1, len(list)):
    tally[list[i]].append(list[i-1])
tally

tally= defaultdict(str)
tally= defaultdict(float)


#### Question 1 #####
some_string="Boaty mcBoatFace."
some_string[1:4]

dict1=defaultdict(float)
for elem in range(len(some_string)-2):
    val=some_string[elem:elem+3]
    dict1[val]+=1

#### Question 2 #####
from math import sqrt
def count_trigrams(document):
    """ count_trigrams takes a string and returns a dictionary of the counts
    of trigrams within the document. """
    dict1=defaultdict(float)
    for elem in range(len(document)-2):
      val=document[elem:elem+3]
      dict1[val]+=1
    return dict1
def normalise(counts_dict):
    """ normalise takes a dictionary of trigram counts counts_dict and
    normalises it by it's length."""
    mag = sqrt(sum([x**2 for x in counts_dict.values()]))
    return dd(int, {key: value/mag for (key, value) in counts_dict.items()})

file=open('example_tset.csv')
data1=csv.reader(file)
data2=list(data1)
print(data2)
