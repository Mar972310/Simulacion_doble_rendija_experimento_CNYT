import numpy as np

def dimension_vectors(v1,v2):
    if v1.shape == v2.shape:
        return True
    return False

def dimension_matrices(M1,M2):
    dimension1 = M1.shape
    dimension2 = M2.shape
    if dimension1 == dimension2:
        return True
    return False

def compatible_matrices(M1,M2):
    if M1.shape[1] == M2.shape(0):
        return True
    return False

def add_complex_vectors(v1,v2):
    if dimension_vectors(v1,v2) == True:
        return np.add(v1,v2)
    else:
        raise Exception ("Error: Los vectores no tienen las mismas dimensiones")

def iverso_vector(v1):
    inverso = np.negative(v1)
    return inverso

def multiplication_scalar_vector(scalar,vec1):
    multiplication = np.multiply(scalar,vec1)
    return multiplication

def add_complex_matrix(M1, M2):
    if dimension_matrices(M1,M2) == True:
        sum = np.add(M1,M2)
        return sum
    else: 
        raise Exception ("Error: Las matrices no tienen las mismas dimensiones")

def inversa_complex_matrix(M):
    return np.negative(M)

def multiplication_scalar_matrix(scalar,M):
    multiplication = np.multiply(scalar,M)
    return multiplication

def transpose_complex_matrix_vecto(a):
    transpose = a.T
    return transpose

def conjugate_complex_matrix_or_vector(a):
    conjugate = np.conjugate(a)
    return conjugate

def adjunct_matrix_or_vector(a):
    adjunct = np.conjugate(a.T)
    return adjunct

def product_complex_matrix(M1,M2):
    if compatible_matrices(M1,M2) == True:
        multiplication = np.dot(M1,M2)
        return multiplication
    else:
        raise Exception ("Error: Las matrices no son compatibles")

def action_matix_vector(v,M):
    return np.dot(M,v)

def product_int_vectors(v1,v2):
    product = np.vdot(v1,v2)
    return product

def norm_vec(v1):
    return np.linalg.norm(v1)

def distance(v1,v2):
    return np.linalg.norm(v1 - v2)

def values_vector(v1):
    eigenvalues, eigenvectors = np.linalg.eig(v1)
    return eigenvalues, eigenvectors

def unit_matrix(M):
    unit = product_complex_matrix(adjunct_matrix_or_vector(M),M)
    if np.allclose(unit, np.eye(M.shape[0], dtype=complex)):
        return True
    return False

def hermitian_matrix(M):
    if np.array_equal(adjunct_matrix_or_vector(M),M):
        return True
    return False

def tensor_matrix_or_vector(a,b):
    return np.kron(a,b)
       

       

