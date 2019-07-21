""" Worksheet 7 revolves around loops such as while and for loops """

# %% Basic While Loops
sec = 10                # Number loops
while sec > 0:
    print('{} seconds to start!'.format(sec))
    sec -= 1                                         # note how we did -= instead of sec= sec-1
print('Ignition complete. Launch initiated!')

word= "rendezvous"       # Basic word loop
while word:
    print(word)
    if word[0] == 'z':  # loops through the word until it finds the letter
        word = word[1:]
        break
    word = word[1:]
print(word)




# %% Basic for loops
my_list = [1,2,3]
for elem in my_list:
    print(elem)

text = "a piece of string"
vowel_count = 0
for letter in text:
    if letter in "aeiou":
        vowel_count = vowel_count + 1
print(vowel_count)