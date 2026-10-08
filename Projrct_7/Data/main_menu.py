import Date_time
import maths
import randomly
import generate_uuid
import file_operators
import module_attributes
import math_util

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
    print("7. Custom Mathematical Utilities")
    print("8. Exit")
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
     while True:
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Calculate Logarithm")
        print("4. Calculate Power")
        print("5. Back to tne main menu")

        sub_choice = int(input("Enter your choice: "))

        if sub_choice == 1:
           c = float(input("Enter Celsius: "))
           print(math_util.celsius_to_fahrenheit(c))
        elif sub_choice == 2:
           f = float(input("Enter Fahrenheit: "))
           print(math_util.fahrenheit_to_celsius(f))
        elif sub_choice == 3:
           n = float(input("Enter positive number: "))
           print(math_util.calculate_log(n))
        elif sub_choice == 4:
           b = float(input("Enter base: "))
           e = float(input("Enter exponent: "))
           print(math_util.calculate_power(b, e))
        elif sub_choice == 5:
            print("Back to the main menu")
            break        
        else:
           print("Invalid choice!")

    elif choice == 8:
       print("Thank you!!!")
    else:
        print("Invalid choice!")