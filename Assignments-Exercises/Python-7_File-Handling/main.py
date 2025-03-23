# read sample.txt's content and print it
try:
    with open('sample.txt', 'r') as file:
        contents = file.read()
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")

# create/write a new file
with open('newfile.txt', 'w') as file:
    file.write("This is a new file")
    print("\nNew file created")

# print the content of the newly created text file
with open('newfile.txt', 'r') as file:
    contents = file.read()
    print("\nContents of the new file:")
    print(contents)

# closes the file to ensure resources are freed up
file.close()
