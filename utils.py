import math
from optparse import TitledHelpFormatter
import re

def k_vector(vec, k):
    result = []
    for i in vec:
        result.append(i*k)
    return tuple(result)

def vector_sum(vec1, vec2, *argv):
    result = [0,0,0]

    for i in range(len(vec1)):
        result[i] = vec1[i]+vec2[i]
        for arg in argv:
            result[i]+=arg[i]

    return tuple(result)

def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        return None
    result = 0
    for i in range(len(vec1)):
        result += vec1[i]*vec2[i]
    return result

def matrix_vector_product(mat, vec):
    if len(mat) != len(vec):
        return None
    result = []
    for line in mat:
        result.append(dot_product(line, vec))

    return tuple(result)

def rotate_x(vec, theta):
    mat = [(1, 0,0), (0, math.cos(theta), -math.sin(theta)), (0, math.sin(theta), math.cos(theta))]

    return matrix_vector_product(mat, vec)

def rotate_y(vec, theta):
    mat = [(math.cos(theta), 0, math.sin(theta)), (0,1,0) , (-math.sin(theta), 0, math.cos(theta))]

    return matrix_vector_product(mat, vec)

def rotate_z(vec, theta):
    mat = [(math.cos(theta), -math.sin(theta),0), (math.sin(theta), math.cos(theta),0), (0,0,1)]

    return matrix_vector_product(mat, vec)
    

def project_z(vec):
    base = [(1,0,0), (0,1,0)]

    result = (0,0,0)
    for b in base:
        p = dot_product(vec, b)
        result = vector_sum(result,k_vector(b, p))
    
    return result

