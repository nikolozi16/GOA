mixed_list = [1, 'a', 2, 'b', 3, 'c', 4]

integers = [x for x in mixed_list if isinstance(x, int)]
strings = [x for x in mixed_list if isinstance(x, str)]

print("Integers:", integers)
print("Strings:", strings)
