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


def get_number(prompt):
    """Keep asking until the user enters a valid number (whole or decimal)."""
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                print("That's not a valid number. Try again.")


def number_operations():
    numbers = []

    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        num = get_number(f"Number {i + 1}: ")
        numbers.append(num)

    # Display original list
    print(f"\nOriginal numbers: {numbers}")

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