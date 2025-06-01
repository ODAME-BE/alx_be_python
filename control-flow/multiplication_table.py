while True:
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Print multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")