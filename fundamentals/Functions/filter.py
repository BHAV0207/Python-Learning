#  filter all words that starts with letter c

words = ["cat", "dog", "camel", "elephant", "cow"]
word = list(filter(lambda x : x[0] == 'c' , words))
print(word)  # Output: ['cat', 'camel', 'cow']