import functions

n = functions.get_matrix_size()
matrix = functions.get_matrix_from_input(n)
inverse = functions.get_inverse_matrix(matrix, n)

if inverse is not None:
    functions.print_matrix(inverse, n)
else:
    print("The matrix has not an inverse!")