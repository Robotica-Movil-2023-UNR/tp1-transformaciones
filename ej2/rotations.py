import numpy as np

# Definición de los ángulos de rotación
roll_angle = np.radians(np.pi*4/7)
pitch_angle = np.radians(np.pi/2)
yaw_angle = np.radians(-np.pi/3)

# Función que obtiene la matriz de rotación
def get_rotation_matrix(axis, angle):
    c = np.cos(angle)
    s = np.sin(angle)
    if axis == 'x':
        return np.array([[1, 0, 0],
                         [0, c, -s],
                         [0, s, c]])
    elif axis == 'y':
        return np.array([[c, 0, s],
                         [0, 1, 0],
                         [-s, 0, c]])
    elif axis == 'z':
        return np.array([[c, -s, 0],
                         [s, c, 0],
                         [0, 0, 1]])
    else:
        raise ValueError("Eje inválido. Use 'x', 'y', o 'z'.")

Rx = get_rotation_matrix('x', roll_angle)
Ry = get_rotation_matrix('y', pitch_angle)
Rz = get_rotation_matrix('z', yaw_angle)

print("Imprime matrices de rotación:")
print("Rx:",Rx)
print("Ry:",Ry)
print("Rx:",Rz)
r12 = np.matmul(Ry, Rx)
print("Imprime Ry*Rx:")
print("R12:",r12)
print("Imprime Rz*Ry*Rx:")
r23 = np.matmul(Rz, r12)
print("R23:",r23)