## 2. Matrix Vector Multiplication ##

matrix_a = np.asarray([[0.7, 3, 9], [1.7, 2, 9], [0.7, 9, 2]])
vector_b = np.asarray([[1], [2], [1]])
ab_product = np.dot(matrix_a, vector_b)

## 3. Matrix Multiplication ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

product_ab = np.dot(matrix_a, matrix_b)
product_ba = np.dot(matrix_b, matrix_a)

## 4. Matrix Transpose ##

matrix_a = np.asarray([
    [0.7, 3],
    [1.7, 2],
    [0.7, 9]
], dtype=np.float32)

matrix_b = np.asarray([
    [113, 3, 10],
    [1, 0, 1],
], dtype=np.float32)

transpose_a = matrix_a.T
print(transpose_a.T)
trans_ba = np.dot(matrix_b.T, matrix_a.T)
trans_ab = np.dot(matrix_a.T, matrix_b.T)
product_ab = np.dot(matrix_a, matrix_b)
print(product_ab.T)
product_ab.T == trans_ba

## 5. Identity Matrix ##

i_2 = np.eye(2)
i_3 = np.eye(3)
matrix_33 = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
matrix_23 = np.array([[1, 2, 3], [4, 5, 6]])

identity_33 = np.dot(i_3, matrix_33)
identity_23 = np.dot(i_2, matrix_23)

identity_33 == matrix_33
identity_23 == matrix_23

## 6. Matrix Inverse ##

matrix_a = np.asarray([
    [1.5, 3],
    [1, 4]
])

def matrix_inverse_two(matrix):
    if np.linalg.det(matrix) == 0:
        print('Error: determinant is 0')
    else:
        return np.linalg.inv(matrix)

inverse_a = matrix_inverse_two(matrix_a)
i_2 = np.dot(inverse_a, matrix_a)

## 7. Solving The Matrix Equation ##

inv = numpy.linalg.inv(np.array([[30, -1], [50, -1]]))
x = np.array([[-1000], [-100]])
solution_x = np.dot(inv, x)

## 8. Determinant For Higher Dimensions ##

matrix_22 = np.asarray([
    [8, 4],
    [4, 2]
])

matrix_33 = np.asarray([
    [1, 1, 1],
    [1, 1, 6],
    [7, 8, 9]
])

det_22 = np.linalg.det(matrix_22)
det_33 = np.linalg.det(matrix_33)