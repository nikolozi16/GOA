my_list = [5, 3, 9, 1, 6, 2]
def find_min(lst):
    if not lst:
        return None
    smallest = lst[0]
    for num in lst[1:]:
        if num < smallest:
            smallest = num
    return smallest
print("Smallest element:", find_min(my_list))
