from datetime import datetime
import time

def current_datetime():
    now = datetime.now()
    print("\nCurrent Date and Time:", now.strftime("%Y-%m-%d"))
    print(now.strftime("%H:%M:%S"))

def date_difference():
    date1 = input("\nEnter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")

    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    difference = abs((d2 - d1).days)

    print("Difference:", difference, "days")

def format_date():
    date_input = input("\nEnter date (YYYY-MM-DD): ")

    date = datetime.strptime(date_input, "%Y-%m-%d")

    print("Formatted date:", date.strftime("%d-%m-%Y"))

def stopwatch():
    print("\nStopwatch started...")
    input("Press Enter to stop.")

    start = time.time()
    input("Press Enter again to finish.")

    end = time.time()

    print("Elapsed time:", round(end - start, 2), "seconds")

def countdown():
    seconds = int(input("\nEnter countdown time in seconds: "))

    while seconds > 0:
        print("Time remaining:", seconds)
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

 
def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")
        print("="*50)

        choice = input("Enter your choice: ")

        if choice == "1":
            current_datetime()
            print("="*50)

        elif choice == "2":
            date_difference()
            print("="*50)

        elif choice == "3":
            format_date()
            print("="*50)

        elif choice == "4":
            stopwatch()
            print("="*50)

        elif choice == "5":
            countdown()
            print("="*50)

        elif choice == "6":
            print("Back to the main menu")
            break

        else:
            print("Invalid choice!")
            print("="*50)