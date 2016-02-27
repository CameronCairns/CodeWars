# Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

def capitals(word):
    indices = []
    index = 0
    for letter in list(word):
        if letter.isupper():
            indices.append(index)
        index += 1
    return indices
