password = input("Insert your password : ")
lenght = len(password)
check = password.isalnum()
if lenght > 8 and check == False:
    print("Your password is strong!")
else:
    print("Your password is not strong!")