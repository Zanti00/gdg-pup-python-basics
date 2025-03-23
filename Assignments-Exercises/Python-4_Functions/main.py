# function to accept a name and return a greeting message
def create_greeting(name):
    return f"Hello {name}, welcome to the GDG Web Development Team! You're doing great, and I truly believe that someday you'll be an amazing developer. Life may feel challenging right now, and programming can be overwhelming at times, but remember, all your hard work will pay off in the end. Keep pushing forward, you're on the right path!"

try:
    # ask user for a name to include in the greet message
    name = input("What's your name? ")
    # print the greet message
    print(create_greeting(name))

# handle invalid input
except ValueError: 
    print("Invalid input: Please enter a valid name.")