lists = [
    [1, "a", 2, "b"],
    ["c", 3, 4, "d"],
    [5, "e", "f", 6]
]

total_sum = 0
concatenated_string = ""

for lst in lists:
    for element in lst:
        if isinstance(element, int):
            total_sum += element
        elif isinstance(element, str):
            concatenated_string += element

print("Sum of integers:", total_sum)
print("Concatenated string:", concatenated_string)
