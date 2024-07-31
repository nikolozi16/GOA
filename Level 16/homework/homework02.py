my_list = [10, 20, 30, 40, 50, 60, 70, 80]

indices = [1, 3, 5]
for index in indices:
    if index < len(my_list):
        print(f"Element at index {index}: {my_list[index]}")
