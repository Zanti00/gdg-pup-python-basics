
# list of some of my favorite foods
favorite_foods = ['Chicken', 'Ice Cream', 'Pancit Canton']

# prints the list of favorite foods
print("Here are my favorite foods:\n")
for index, food in enumerate(favorite_foods):
    print(f"Food {index+1}: {food}")

# to separate the list and the countdown
print("\n")

# ask user for a starting value then counts it down to 0
try:
    num = int(input("Enter a positive number to start the countdown: "))

    if num <= 0:
        raise ValueError("Invalid input: Please enter a number greater than zero.")
    while num > 0:
        print(num)
        num -= 1
        if num == 0:
            print("Countdown complete!")
    
except ValueError:
    print("Invalid input: Please enter a valid number.")