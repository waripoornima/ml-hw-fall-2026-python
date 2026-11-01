from module5_mod import NumberManager

def main():
    # 1. Enter N positive integer
    while True:
        try:
            n = int(input("Enter a positive integer N: "))
            if n > 0:
                break
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Initialize the Number manager object from our module
    manager = NumberManager()

    # 2. user to provide N numbers one by one
    print(f"Please enter {n} numbers one by one:")
    for i in range(n):
        while True:
            try:
                num = int(input(f"Number {i + 1}: "))
                manager.insert_number(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    # 3. input X integer for search
    try:
        x = int(input("Enter the integer X to search for: "))
    except ValueError:
        x = None

    # search and output the result
    if x is not None:
        result = manager.search_number(x)
        print(f"Result: {result}")
    else:
        print("Result: -1")


if __name__ == "__main__":
    main()