# initialized a list
example_list = [5, 3, 8, 1]

print("Original list:", example_list)

try:
    num = int(input("Enter a number to add: "))
    # add number to the end of the list
    example_list.append(num)

    print(f"Added {num} to the list:", example_list)

    num = int(input("Enter a number to remove: "))
    # remove number from the list
    if num in example_list:
        example_list.remove(num)
        print(f"Removed {num} from the list:", example_list)
    else:
        print("The number is not in the list.")

    # sort the list in ascending order
    example_list.sort()

    print("Sorted list:", example_list)
except ValueError:
    print("Please enter a valid number.")