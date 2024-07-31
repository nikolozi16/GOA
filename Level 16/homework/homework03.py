list_integers = [1, 3, 5, 7, 9]
list_strings = ['a', 'b', 'c', 'd', 'e']

combined_list = []
min_length = min(len(list_integers), len(list_strings))

for i in range(min_length):
    combined_list.append(list_integers[i])
    combined_list.append(list_strings[i])

# თუ რომელიმე ლისტში მეტი ელემენტი დარჩა
if len(list_integers) > min_length:
    combined_list.extend(list_integers[min_length:])
elif len(list_strings) > min_length:
    combined_list.extend(list_strings[min_length:])

print("Combined list:", combined_list)
