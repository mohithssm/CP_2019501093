# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.
import numpy as np

def fun_matrixmultiply(m1, m2):
    result = list(np.dot(m1, m2))
    return result
print(fun_matrixmultiply([[1,3],[2,4],[2,5]], [[1,3,2,2], [2,4,5,1]]))


