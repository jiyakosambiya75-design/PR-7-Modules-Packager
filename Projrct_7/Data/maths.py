import math

def calculate_factorial():
    n = int(input("Enter a number: "))
    print("Factorial:", math.factorial(n))

def compound_interest():
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest (in %): "))
    t = float(input("Enter time (in years): "))

    amount = p * (1 + r / 100) ** t
    print("Compound Interest:", round(amount, 2))

def trigonometric_calculations():
    angle = float(input("Enter angle in degrees: "))

    print("sin:", math.sin(math.radians(angle)))
    print("cos:", math.cos(math.radians(angle)))
    print("tan:", math.tan(math.radians(angle)))
def circle_area():
    radius = float(input("Enter radius: "))
    print("Area:", math.pi * radius ** 2)


def rectangle_area():
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area:", length * width)
 
def triangle_area():
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    print("Area:", 0.5 * base * height)

def geometric_area():
    print("\nArea of Geometric Shapes:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = int(input("Enter your choice: "))

    if choice == 1:
       circle_area()

    elif choice == 2:
        rectangle_area()

    elif choice == 3:
        triangle_area()

    else:
        print("Invalid choice!")

def operations():
    while True:

        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")
        print("="*50)

        choice = int(input("Enter your choice: "))

        if choice == 1:
           calculate_factorial()
           print("="*50)
        
        
        elif choice == 2:
           compound_interest()
           print("="*50)
        

        elif choice == 3:
           trigonometric_calculations()
           print("="*50)
        

        elif choice == 4:
           geometric_area()
           print("="*50)
        

        elif choice == 5:
           print("Back to the Main Menu:")
           return

        else:
           print("Invalid choice!")