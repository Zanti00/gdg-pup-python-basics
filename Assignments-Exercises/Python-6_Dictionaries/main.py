# initialize dictionary
dict = {'name': 'John', 'age': 22}

print("Original dictionary values: ", dict)

print("\nAdd new key-value pair to the dictionary\n")

# handles exception if invalid input is entered
try:
    # add new key-value pair to the dictionary
    key = input("Enter the new key: ")
    value = input("Enter the new value: ")
    dict[key] = value
    print("Updated dictionary values: ", dict)

    print("\nUpdate a key-value pair in the dictionary\n")

    # update a key-value pair in the dictionary
    key = input("Enter the key to update: ")
    value = input("Enter the new value: ")
    dict[key] = value
    print("Updated dictionary values: ", dict)

    print("\nDelete a key-value pair in the dictionary\n")

    # delete a key-value pair in the dictionary
    key = input("Enter the key to delete: ")
    del dict[key]
    print("Updated dictionary values: ", dict)
except:
    print("Invalid input")