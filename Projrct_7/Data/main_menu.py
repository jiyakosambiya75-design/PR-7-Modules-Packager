import Date_time
import maths
import randomly
import generate_uuid
import file_operators
import module_attributes

while True:
    print("="*50)
    print("      Welcome to Multi-Utility Toolkit ")
    print("="*50)
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("="*50)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        Date_time.datetime_menu()
        print("="*50)

    elif choice == 2:
        maths.operations()
        print("="*50)

    elif choice == 3:
        randomly.generate_randomly()
        print("="*50)

    elif choice == 4:
        generate_uuid.uuid_create()
        print("="*50)

    elif choice == 5:
        file_operators.file_operations()
        print("="*50)

    elif choice == 6:
        module_attributes.explore_module()
        print("="*50)

    elif choice == 7:
        print("=" * 50)
        print("Thank you for using the Multi-Utility Toolkit!")
        print("=" * 50)
        break

    else:
        print("Invalid choice!")