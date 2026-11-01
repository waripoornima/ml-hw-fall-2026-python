# This class is to manage thne numbers 
#   supports initializing number, insertion and search number using Oops

class NumberManager:
    # initializing an empty list to store numbers 
    def __init__(self):
        self.numbers = []

    # insert number into collection
    def insert_number(self,number):
        self.numbers.append(number)

    # search the number from collection and return index if found, or -1 otherwise
    def search_number(self,number):
        if number in self.numbers:
            return self.numbers.index(number) + 1
        return -1

def main():
    # 1. input N (positive integer)
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            if n > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Initialize the number manager object
    manager = NumberManager()

    # 2. Enter N numbers one by one
    print(f"Please enter {n} numbers one by one:")
    for i in range(n):
        while True:
            try:
                num = int(input(f"Number {i + 1}: "))
                manager.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # 3. Ask user for input X (integer) to search
    try:
        x = int(input("Enter the integer X to search for: "))
    except ValueError:
        print("Invalid input for X. Assuming 0 or treating as non-integer.")
        x = None

    # Perform search and output the result
    if x is not None:
        result = manager.search_number(x)
        print(f"Result: {result}")
    else:
        print("Result: -1")


if __name__ == "__main__":
    main()