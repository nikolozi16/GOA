my_list = [5, 3, 9, 1, 6, 2]
def find_max(lst):
    if not lst:
        return None
    largest = lst[0]
    for num in lst[1:]:
        if num > largest:
            largest = num
    return largest
print("Largest element:", find_max(my_list))
