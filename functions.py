def get_matrix_size():
    size = int(input("Type the matrix size: "))
    return size


def get_matrix_from_input(matrix_size):
    matrix = []

    for i in range(matrix_size):
        line = []

        for j in range(matrix_size):
            element = float(input(f"Type the element in line {i+1} and column {j+1}: "))
            line.append(element)
        matrix.append(line)
    return matrix


def create_identity_matrix(matrix_size):
    identity = []

    for i in range(matrix_size):
        line = []

        for j in range(matrix_size):
            if i == j:
                line.append(1)
            else:
                line.append(0)
        
        identity.append(line)
    
    return identity


def create_diagonal_matrix(matrix, inverse, matrix_size):
    for diagonal_element in range(matrix_size):
        element = matrix[diagonal_element][diagonal_element]

        if element == 0:
            swap_line = (diagonal_element + 1) % matrix_size
            multiplative_factor = 1/(matrix[swap_line][diagonal_element])

            for column in range(matrix_size):
                aux_line = matrix[swap_line][column] * multiplative_factor
                matrix[swap_line][column] = matrix[diagonal_element][column]
                matrix[diagonal_element][column] = aux_line

                aux_line = inverse[swap_line][column] * multiplative_factor
                inverse[swap_line][column] = inverse[diagonal_element][column]
                inverse[diagonal_element][column] = aux_line

    for diagonal_element in range(matrix_size):
        element = matrix[diagonal_element][diagonal_element]

        for line in range(matrix_size):
            if line != diagonal_element:
                multiplative_factor = -(matrix[line][diagonal_element] / element)

                for column in range(matrix_size):
                    matrix[line][column] += multiplative_factor * matrix[diagonal_element][column]
                    inverse[line][column] += multiplative_factor * inverse[diagonal_element][column]
    
    return [matrix, inverse]


def transform_in_identity(matrix, inverse_matrix, matrix_size):
    for diagonal_element in range(matrix_size):
        element = matrix[diagonal_element][diagonal_element]

        if element in [0, 1]:
            continue

        matrix[diagonal_element][diagonal_element] = 1
        for column in range(matrix_size):
            inverse_matrix[diagonal_element][column] /= element

    return [matrix, inverse_matrix]


def is_identity(matrix, matrix_size):
    for line in range(matrix_size):
        for column in range(matrix_size):
            if line == column:
                if matrix[line][column] != 1:
                    return False
            else:
                if matrix[line][column] != 0:
                    return False
    
    return True


def get_inverse_matrix(matrix, matrix_size):
    inverse_matrix = create_identity_matrix(matrix_size)
    matrix, inverse_matrix = create_diagonal_matrix(matrix, inverse_matrix, matrix_size)
    matrix, inverse_matrix = transform_in_identity(matrix, inverse_matrix, matrix_size)

    if is_identity(matrix, matrix_size):
        return inverse_matrix
    else:
        return None


def print_matrix(matrix, matrix_size):
    print('')
    for i in range(matrix_size):
        for j in range(matrix_size):
            print(matrix[i][j], end='\t')
        print('')