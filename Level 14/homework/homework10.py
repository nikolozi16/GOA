strings = ["vashli", "alubali", "fortoxali"]
max_length = 0

for i in strings:
    current = len(i)
    if current > max_length:
        max_length = current
print(max_length)