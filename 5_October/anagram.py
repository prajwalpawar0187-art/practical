word1=input("Enter word 1:")
word2=input("Enter word 2:")
if sorted(word1.lower())==sorted(word2.lower()):
    print("Anagram Word")
else:
    print("Not Anagram Word")