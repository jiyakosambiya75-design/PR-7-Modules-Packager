import math

def explore_module():
    module_name = input("Enter module name to explore: ")

    if module_name == "math":
        print("Available Attributes in math module:")
        print(dir(math))
    else:
        print("Module not supported!")