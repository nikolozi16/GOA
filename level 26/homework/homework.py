def process_numbers(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:  
            new_list.append(num / 2)
        else:  
            new_list.append(num * 2)
    return new_list


print(process_numbers([1, 2, 3, 4]))  
