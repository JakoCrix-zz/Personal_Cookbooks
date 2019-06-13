"""Grok 7, For and while loops"""
sec=5
while sec >0:
    print(str(sec), 'seconds to start')
    sec-=1

word= 'rendezvous'
while word:
    if word[0]=='z':
        word=word[1:]
        break
    word=word[1:]
word

"""Grok 8, Mutability and Advanced Sequences"""
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
