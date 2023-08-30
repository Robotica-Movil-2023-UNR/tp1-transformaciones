import numpy as np

def affine_matrix_2d(rotation_angle, translation):
    c = np.cos(rotation_angle)
    s = np.sin(rotation_angle)
    rotation_matrix = np.array([[c, -s],
                                [s, c]])
    translation_vector = np.array(translation).reshape(2, 1)

    affine_matrix = np.hstack((rotation_matrix, translation_vector))
    last_row = np.array([0, 0, 1])
    affine_matrix = np.vstack((affine_matrix, last_row))

    return affine_matrix

rotation_angle = np.radians(45)
translation = [2, 3]

W_to_RA = affine_matrix_2d(rotation_angle, translation)
print("Transformación Mundo al robot A:")
print(W_to_RA)

# Punto b, coordenadas de p1 en sistema de A
# p1 está en el frame W
p1_W = np.array([1, 5, 1])
RA_to_W = np.linalg.inv(W_to_RA)

p1_A = np.dot(RA_to_W, p1_W)
print("Punto 1 en Robot A")
print(p1_A)

# Punto c, coordenadas de p2 en sistema de B
# p2 está en el frame del robot A
p2_A = np.array([1, 2, 1])
RA_to_RB = affine_matrix_2d(np.radians(-45),[1,1])
RB_to_RA = np.linalg.inv(RA_to_RB)

p2_B = np.dot(RB_to_RA, p2_A)
print("Punto 2 en Robot B")
print(p2_B)

# Punto d, obtener la pose y orientación del robot B en W
W_to_B = np.dot(W_to_RA, RA_to_RB)
print("Transformación W->RA")
print(W_to_RA)
print("Transformación RA->RB")
print(RA_to_RB)
print("Transformación de B en el mundo")
print(W_to_B)

