def create_file():
    filename = input("Enter file name: ")
    open(filename, "w").close()
    print("File created successfully!")


def write_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")
    with open(filename, "w") as file:
        file.write(data)
    print("Data written successfully!")


def read_file():
    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        data = file.read()
    print("File Content:")
    print(data)


def append_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")
    with open(filename, "a") as file:
        file.write(data)
    print("Data appended successfully!")


def file_operations():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        print("="*50)
        choice = int(input("Enter your choice: "))

        if choice == 1:
            create_file()
            print("="*50)
        elif choice == 2:
            write_file()
            print("="*50)
        elif choice == 3:
            read_file()
            print("="*50)
        elif choice == 4:
            append_file()
            print("="*50)
        elif choice == 5:
            print("Back to the Main Menu:")
            break
        else:
            print("Invalid choice!")