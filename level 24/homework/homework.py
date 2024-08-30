def manual_count(string, count_char):
    count = 0
    for char in string:
        if char == count_char:
            count += 1
    return count

result = manual_count("hello world", "l")
print(result)
