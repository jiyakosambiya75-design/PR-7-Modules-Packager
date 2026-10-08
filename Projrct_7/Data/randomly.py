import random
import string

def random_number():
    print("Random Number:", random.randint(1, 100))

def  random_List():
    n = int(input("Enter list length: "))
    print("Random List:", random.sample(range(1, 101), n))
    

def  random_password():
    length = int(input("Enter password length: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated Password:", password)
     
def  random_OTP():
    print("Generated OTP:", random.randint(100000, 999999))

def generate_randomly():
    while True:
        print("Random Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")
        print("="*50)
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            random_number()
            print("="*50)
        
        elif choice == 2:
            random_List()
            print("="*50)
            
        elif choice == 3:
            random_password()
            print("="*50)
        
        elif choice == 4:
            random_OTP()
            print("="*50)
        
        elif choice == 5:
            print("Back to Main Menu")
            break
        
        else:
            print("Invalid choice")
            print("="*50)