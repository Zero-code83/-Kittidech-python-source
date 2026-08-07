
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def setup_person():
    """Collect the starting details and build the initial tuple."""
    name = input("Enter name: ").strip()
    try:
        age = int(input("Enter age: "))
    except ValueError:
        print("Invalid age, defaulting to 0.")
        age = 0
    city = input("Enter city: ").strip()
    country = input("Enter country: ").strip()
    return (name, age, city, country)
def display_info(person, hobbies):
    """Display the person's basic info and hobbies."""
    name, age, city, country = person
    print("\n--- Personal Information ---")
    print(f"Name:    {name}")
    print(f"Age:     {age}")
    print(f"City:    {city}")
    print(f"Country: {country}")
    print(f"Hobbies: {', '.join(hobbies) if hobbies else 'None yet'}")
    print("-----------------------------")
def add_hobby(hobbies):
    """Add a new hobby. Lists are mutable, so we can update it in place."""
    new_hobby = input("Enter a hobby to add: ").strip()
    if new_hobby:
        hobbies.append(new_hobby)
        print(f"Added '{new_hobby}' to hobbies.")
    else:
        print("No hobby entered.")
def remove_hobby(hobbies):
    """Remove a hobby from the list, if it exists."""
    if not hobbies:
        print("There are no hobbies to remove.")
        return
    print(f"Current hobbies: {', '.join(hobbies)}")
    target = input("Enter the hobby to remove: ").strip()
    if target in hobbies:
        hobbies.remove(target)
        print(f"Removed '{target}' from hobbies.")
    else:
        print(f"'{target}' was not found in the hobbies list.")
def update_age(person):
    """
    Tuples are immutable, so person[1] = new_age would raise an error.
    Instead we unpack the old tuple's values and build a brand new one.
    """
    name, age, city, country = person
    try:
        new_age = int(input("Enter new age: "))
    except ValueError:
        print("Invalid age entered. Age unchanged.")
        return person
 
    updated_person = (name, new_age, city, country)  # a new tuple, not an edit
    print(f"Age updated from {age} to {new_age}.")
    return updated_person
def personal_info_manager():
    # Create initial person tuple
    person = setup_person()
    hobbies = []
 
    menu = """
Personal Information Manager
1. Display all information
2. Add a hobby
3. Remove a hobby
4. Update age
5. Quit
"""
 
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()
 
        if choice == "1":
            display_info(person, hobbies)
        elif choice == "2":
            add_hobby(hobbies)
        elif choice == "3":
            remove_hobby(hobbies)
        elif choice == "4":
            person = update_age(person)  # tuple is immutable, so we reassign
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 5.")
    pass

if __name__ == "__main__":
    personal_info_manager()


"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

def number_operations():
    numbers = []
    
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
            num = get_number(f"Number {i + 1}: ")
            numbers.append(num)
            pass
    
    # Display original list
    print(f"Original numbers: {numbers}")
    
    # Create filtered lists
    even_numbers = [n for n in numbers if n % 2 == 0]
    odd_numbers = [n for n in numbers if n % 2 != 0]  
    
    # Calculate average
    average = sum(numbers) / len(numbers) 
    
    # Numbers greater than average
    above_average = [n for n in numbers if n > average] 
    
    # Display results
    print(f"Even numbers: {even_numbers}")
    print(f"Odd numbers: {odd_numbers}")
    print(f"Numbers above average: {above_average}")
 
    print("\n--- Statistics ---")
    print(f"Sum:     {sum(numbers)}")
    print(f"Average: {average:.2f}")
    print(f"Min:     {min(numbers)}")
    print(f"Max:     {max(numbers)}")

if __name__ == "__main__":
    number_operations()