user_input = int(input("enter your age: "))

if user_input >5 and user_input <12:
    print("you are chindren")
elif user_input >12 and user_input <18:
    print("teen")
elif user_input >18:
    print("you are an adolt")
else:
    print("enter corect age")