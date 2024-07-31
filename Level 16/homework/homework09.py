original_list = [10, 20, 30, 40, 50, 60, 70]

even_index_elements = [original_list[i] for i in range(len(original_list)) if i % 2 == 0]

print("Elements at even indices:", even_index_elements)
