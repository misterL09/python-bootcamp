from random import choice
word_bank = {
"Fruits": ["apple", "banana", "cherry", "mango"],
"Animals": ["cat", "dog", "elephant", "lion"],
"Countries": ["India", "Brazil", "France", "Japan"],
}

print("Current Categories:")
for index, category in enumerate(word_bank,start = 1):
    print(index,category)

input_category = input("Choose a category: ")
if input_category not in word_bank:
    print("Not in category")
else:
    possible_words = word_bank[input_category]
    word = choice(possible_words)
    possible_words.remove(word)

