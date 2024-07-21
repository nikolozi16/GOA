



correct_password = 'cindela' 
user_input = ''

while correct_password != user_input:
    user_input = input("please enter your correct_password"  )

    if user_input == correct_password:
        print("you succsesfully signed in: ")
    else: 
        print("password is incorrect")
 