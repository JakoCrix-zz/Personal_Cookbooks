def maxlist(numlist):
    if numlist:
        maxnum = numlist[0]
        for num in numlist[1:]:
            if num > maxnum:
                maxnum = num
        return maxnum

print(maxlist([1,2.0,3]))
print(maxlist([4,-1]))
print(maxlist([3,5,1,4,-1]))

##
def maxby(intlist):
    if intlist:
        maxnum=max(intlist)
        margin= max(intlist)-(sorted(intlist))[-2]
        return maxnum, margin

print(maxby([3, 4, 5, 7]))
print(maxby([]))

x=None
if x:
    print('x is not empty')
else:
    print('x is empty')
