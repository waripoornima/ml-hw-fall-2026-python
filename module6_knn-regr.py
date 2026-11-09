"""
Create a Python program:

The program asks the user for input N (positive integer) and reads it.
Then the program asks the user for input k (positive integer) and reads it.
Then the program asks the user to provide N (x, y) points (one by one) and reads all of them: first: x value, then: y value for every point one by one. X and Y are the real numbers.
In the end, the program asks the user for input X and outputs: the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
The basic functionality of data processing (data initialization, data insertion, data calculation) should be done using Numpy library as much as possible (note: you can combine with OOP from the previous task).
Name this program "module6_knn-regr.py" and upload it to the above-mentioned repo.

"""
# File name: module6_knn-regr.py

import numpy as np

def main():
    # 1. Ask for N (positive integer)
    while True:
        try:
            N = int(input("Enter the number of training points N (positive integer): "))
            if N > 0:
                break
            print("N must be a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # 2. Ask for k (positive integer)
    while True:
        try:
            k = int(input("Enter k for k-NN (positive integer): "))
            if k > 0:
                break
            print("k must be a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Check validation condition: k <= N
    if k > N:
        print(f"Error: k ({k}) cannot be greater than N ({N}).")
        return

    # 3. Read N (x, y) points one by one
    X_train = np.zeros(N)
    y_train = np.zeros(N)

    print(f"\nProvide {N} data points (x, y) one by one:")
    for i in range(N):
        while True:
            try:
                x_val = float(input(f"  Point {i+1} - x value: "))
                break
            except ValueError:
                print("  Invalid input. Please enter a real number for x.")
        
        while True:
            try:
                y_val = float(input(f"  Point {i+1} - y value: "))
                break
            except ValueError:
                print("  Invalid input. Please enter a real number for y.")
                
        X_train[i] = x_val
        y_train[i] = y_val

    # 4. Ask for test input X
    while True:
        try:
            X_test = float(input("\nEnter test input X for prediction: "))
            break
        except ValueError:
            print("Invalid input. Please enter a real number for X.")

    # 5. Data processing and calculation using NumPy
    # Compute Euclidean (l2) distance in 1D: absolute difference
    distances = np.abs(X_train - X_test)

    # Get indices that would sort the distances in ascending order
    sorted_indices = np.argsort(distances)

    # Select the k nearest neighbors' y values
    k_nearest_y = y_train[sorted_indices[:k]]

    # Calculate prediction Y as the mean of the k nearest neighbors' labels
    y_pred = np.mean(k_nearest_y)

    # Output the result
    print(f"\n--- Result ---")
    print(f"Predicted Y for X = {X_test} using {k}-NN Regression: {y_pred}")

if __name__ == "__main__":
    main()

