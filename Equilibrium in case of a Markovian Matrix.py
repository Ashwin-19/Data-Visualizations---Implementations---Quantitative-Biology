# Author - @ashwin17222

import numpy as np

def equilibrium_stability(Matrix):

    p0 = [2, 3, 2, 4]
    steps = 0

    for i in range(100):

        # p(t+1) = (M**t)*p0
        p0 = np.matmul(Matrix,p0)
        steps += 1

        # check how many values of vector p(t+1) are equal to vector p(t)
        matches = sum([1 if p0[i] == np.matmul(Matrix,p0)[i] else 0 for i in range(4)])

        # if all the values of vectors p(t+1) and p(t) match
        if matches == 4:
            break

    print("No. of steps taken to reach the equilibrium point i.e. population vector no longer changes")
    print(steps)

    print("The population converges to the following vector")
    print(p0)

    print()


def eigenfunction(Matrix):

    eigenvalues, eigenvectors = np.linalg.eig(Matrix)

    return eigenvalues, eigenvectors


def verification(Matrix, eigenvalues, eigenvectors):

    # Theorem 1 -> find if eigenvalue 1 exists
    index = -1
    for i in range(len(eigenvalues)):
        if round(eigenvalues[i],5) == 1:
            index = i
            break

    if index != -1:

        # retrieve corresponding eigenvector to eigenvalue 1
        vector = eigenvectors[index]

        # Theorem 2 -> all entities in eigenvector corresponding to eigenvalue 1 are positive
        positive_check = sum([1 if vector[i] > 0 else 0 for i in range(4)])

        # total of 4 positive values in the vector
        if positive_check == 4:
            print("Theorems hold well")



# predefined Markov matrix, alpha = 0.3, all values non negative
# Matrix =[[0.7, 0.1, 0.1, 0.1],[0.1, 0.7, 0.1, 0.1],[0.1, 0.1, 0.7, 0.1], [0.1, 0.1, 0.1, 0.7]]

# steps to reach equilibrium
# equilibrium_stability(Matrix)

# eigenvalues
# eigenvalues, eigenvectors = eigenfunction(Matrix)


# print(eigenvalues)
# print()

# eigenvectors
# v1 = eigenvectors[:, 0]
# v2 = eigenvectors[:, 1]
# v3 = eigenvectors[:, 2]
# v4 = eigenvectors[:, 3]
# print(v1)
# print(v2)
# print(v3)
# print(v4)
# print()

# verification of theorems
# verification(Matrix, eigenvalues, [v1,v2,v3,v4])
