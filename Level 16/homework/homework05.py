lists = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

even_sum = 0
odd_sum = 0

for lst in lists:
    for num in lst:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)
