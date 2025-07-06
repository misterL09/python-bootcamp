example = "Hello {} {} World"

var_example = example.lower()
test = example.format('aa','bb')
print(test)
print(example)
print(var_example)

example2 = ['a','b','c']
clean_result = " ".join(example2)
print(clean_result)