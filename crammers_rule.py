# Function to calculate the determinant of a matrix using Cramer's rule
def determinant(matrix):
    if len(matrix) == 2:  # Base case for 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):  # Recursive case for larger matrices
        sub_matrix = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
    return det


# Function to replace a column in a matrix with a vector
def replace_column(matrix, column_index, new_column):
    modified_matrix = [row[:] for row in matrix]  # Create a copy of the matrix
    for i in range(len(new_column)):
        modified_matrix[i][column_index] = new_column[i]
    return modified_matrix


# Function to find RREF (Row-Reduced Echelon Form)
def rref(matrix):
    A = [row[:] for row in matrix]
    rows = len(A)
    cols = len(A[0])
    lead = 0
    for r in range(rows):
        if lead >= cols:
            return A
        i = r
        while A[i][lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if lead == cols:
                    return A
        A[i], A[r] = A[r], A[i]  # Swap rows
        lead_val = A[r][lead]
        A[r] = [x / lead_val for x in A[r]]
        for i in range(rows):
            if i != r:
                A[i] = [A[i][j] - A[i][lead] * A[r][j] for j in range(cols)]
        lead += 1
    return A


# Function to solve the system using Cramer's Rule
def cramer_solve(A, b):
    det_A = determinant(A)

    print(f"Step 1: Calculate the determinant of matrix A: det(A) = {det_A}")

    if det_A == 0:  # No unique solution case
        print("Step 2: Since det(A) = 0, we need to check if the system has no solutions or infinitely many solutions.")

        all_zero_dets = True
        for i in range(len(b)):
            modified_matrix = replace_column(A, i, b)
            det_modified = determinant(modified_matrix)
            print(
                f"Step 3: Calculate the determinant of modified matrix A with column {i + 1} replaced by b: det(A') = {det_modified}")

            if det_modified != 0:
                all_zero_dets = False
                print("\nConclusion: The system has no solution (it's inconsistent).")
                return None

        print("\nConclusion: The system has infinitely many solutions.")
        # Perform Gaussian elimination to provide free variables and parameterized solution
        augmented_matrix = [row[:] + [b[i]] for i, row in enumerate(A)]
        rref_matrix = rref(augmented_matrix)
        print("\nRow-Reduced Echelon Form of the augmented matrix:")
        for row in rref_matrix:
            print(row)

        # Find free and dependent variables
        num_rows, num_cols = len(rref_matrix), len(rref_matrix[0])
        basic_vars = []
        free_vars = []

        for col in range(num_cols - 1):  # Exclude the last column (vector b)
            if any(rref_matrix[row][col] != 0 for row in range(num_rows)):
                if rref_matrix[row][col] == 1:
                    basic_vars.append(col)
                else:
                    free_vars.append(col)

        print("\nFree variables (can take any value):", [f"x{var + 1}" for var in free_vars])
        print("Basic variables (dependent on free variables):")

        for var in basic_vars:
            row = next(row for row in range(num_rows) if rref_matrix[row][var] == 1)
            expression = f"x{var + 1} = " + " + ".join(
                [f"{-rref_matrix[row][j]}x{j + 1}" for j in free_vars if rref_matrix[row][j] != 0])
            expression += f" + {rref_matrix[row][-1]}"
            print(expression)

        return None

    else:  # Unique solution case
        print("Step 2: Since det(A) is not 0, the system has a unique solution.")

        solutions = []
        for i in range(len(b)):
            modified_matrix = replace_column(A, i, b)
            det_modified = determinant(modified_matrix)
            print(
                f"Step 3: Calculate the determinant of modified matrix A with column {i + 1} replaced by b: det(A') = {det_modified}")

            solution = det_modified / det_A
            solutions.append(solution)
            print(f"Step 4: Using Cramer's Rule, x{i + 1} = det(A') / det(A) = {det_modified} / {det_A} = {solution}")

        print("\nConclusion: The system has a unique solution.")
        return solutions


# Function to get matrix input from the user
def input_matrix():
    n = int(input("Enter the number of variables (size of matrix): "))
    print("Enter the matrix A (row by row):")
    A = []
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        A.append(row)
    print("Enter the values of vector b (space-separated):")
    b = list(map(float, input().split()))
    return A, b


# Main Program
if __name__ == "__main__":
    A, b = input_matrix()
    solution = cramer_solve(A, b)
    if solution:
        print("Solution:", solution)
