# Complete this program to classify people by age
# age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:



# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        if choice == "1":
            print(f"Your balance is: ${balance:.2f}")
 
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Enter an amount greater than zero.")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"Withdrew ${amount:.2f}. New balance: ${balance:.2f}")
 
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Enter an amount greater than zero.")
            else:
                balance += amount
                print(f"Deposited ${amount:.2f}. New balance: ${balance:.2f}")
 
        elif choice == "4":
            print("Thank you for banking with us. Goodbye!")
            break  # Leaves the while loop, so the program ends here
 
        else:
            print("Invalid option. Please choose 1-4.")
        
else:
    print("Invalid PIN")
