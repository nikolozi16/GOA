shopping_cart = {}

num_items = int(input("How many items do you want to buy? "))

for _ in range(num_items):
    item = input("Enter the name of the item: ")
    quantity = int(input(f"Enter the quantity of {item}: "))
    shopping_cart[item] = quantity

print("Shopping Cart:")
for item, quantity in shopping_cart.items():
    print(f"{item}: {quantity}")
