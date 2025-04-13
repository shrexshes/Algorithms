"""
Write a program that takes in a word list and outputs a 
list of all the words that are anagrams of another word in the list.
"""

word_list = [ "supersonic", "car", "tree", "boy","percussion", "girl", "arc"]

anagram_list=[]

for word_1 in word_list:
    # print("word 1: "+word_1)
    for word_2 in word_list:
        # print("word 2: "+word_2)
        print("Word 1: ", sorted(word_1))
        print("Word 2: ", sorted(word_2))
        if word_1 !=word_2 and (sorted(word_1)==sorted(word_2)):
            anagram_list.append(word_1)
print(anagram_list)
