"""
Create a Python program:

The program asks the user for input N (positive integer) and reads it.
Then the program asks the user for input k (positive integer) and reads it.
Then the program asks the user to provide N (x, y) points (one by one) and reads all of them:
 first: x value, then: y value for every point one by one. 
 X and Y are the real numbers.
In the end, the program asks the user for input X and outputs: 
the result (Y) of k-NN Regression if k <= N, or any error message otherwise.
Additionally, provide the variance of labels in the training dataset.
The basic functionality of data processing (data initialization, 
data insertion), should be done using Numpy library while the 
computation (ML) part should be done using Scikit-learn library as 
much as possible (note: you can combine with what you've done from the 
previous task).


Sample results

Please provide 5 data points (x, y) as real numbers:
  Point 1 - Enter x: 4
  Point 1 - Enter y: 6
  Point 2 - Enter x: 4
  Point 2 - Enter y: 2
  Point 3 - Enter x: 4
  Point 3 - Enter y: 5
  Point 4 - Enter x: 6
  Point 4 - Enter y: 7
  Point 5 - Enter x: 8
  Point 5 - Enter y: 9

[Stats] Variance of labels (y) in training dataset: 5.3600

Enter input X for prediction: 6

Result: For X = 6.0, the predicted Y using 3-NN Regression is 5.0000

"""




import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    print("--- k-NN Regression using NumPy and Scikit-learn ---")
    
    # 1. Read N (positive integer)
    try:
        N = int(input("Enter N (positive integer, number of points): "))
        if N <= 0:
            print("Error: N must be a positive integer greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input for N. Please enter an integer.")
        return

    # 2. Read k (positive integer)
    try:
        k = int(input("Enter k (positive integer for k-NN): "))
        if k <= 0:
            print("Error: k must be a positive integer greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input for k. Please enter an integer.")
        return

    # 3. Data initialization using NumPy
    X_train = np.zeros((N, 1))
    y_train = np.zeros(N)

    print(f"\nPlease provide {N} data points (x, y) as real numbers:")
    for i in range(N):
        while True:
            try:
                x_val = float(input(f"  Point {i+1} - Enter x: "))
                y_val = float(input(f"  Point {i+1} - Enter y: "))
                break
            except ValueError:
                print("  Invalid input. Please enter valid real numbers for x and y.")
        
        # Data insertion into NumPy arrays
        X_train[i, 0] = x_val
        y_train[i] = y_val

    # Additionally calculate and display the variance of labels (y) in the training dataset
    label_variance = np.var(y_train)
    print(f"\n[Stats] Variance of labels (y) in training dataset: {label_variance:.4f}")

    # 4. Check condition: k <= N
    if k > N:
        print(f"\nError: k ({k}) cannot be greater than N ({N}). Cannot perform k-NN regression.")
        return

    # 5. ML Computation using Scikit-learn
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    # Ask for input X and predict Y
    try:
        X_input = float(input("\nEnter input X for prediction: "))
    except ValueError:
        print("Error: Invalid input for X. Please enter a real number.")
        return

    # Predict using the trained model
    X_input_array = np.array([[X_input]])
    y_pred = model.predict(X_input_array)[0]

    print(f"\nResult: For X = {X_input}, the predicted Y using {k}-NN Regression is {y_pred:.4f}")

if __name__ == "__main__":
    main()