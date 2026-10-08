
import importlib

def explore_module():
    module_name = input("Enter module name to explore: ").strip()

    try:
        module = importlib.import_module(module_name)

        print("\nModule:", module_name)
        print("\nAvailable attributes and functions:")

        for item in dir(module):
            if not item.startswith("_"):
                print(item)

    except ModuleNotFoundError:
        print("Module not found! Please enter a valid module name.")

    except Exception as error:
        print("Error:", error)


if __name__ == "__main__":
    explore_module()