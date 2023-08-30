import csv
import numpy as np
from scipy.spatial.transform import Rotation as R
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Matrix de transformación imu->cámara
T_BS = np.array([0.0148655429818, -0.999880929698, 0.00414029679422, -0.0216401454975,
    0.999557249008, 0.0149672133247, 0.025715529948, -0.064676986768,
    -0.0257744366974, 0.00375618835797, 0.999660727178, 0.00981073058949,
    0.0, 0.0, 0.0, 1.0]).reshape(4,4)

def transform_pose(pose, transformation_matrix):
    timestamp, x, y, z, qw, qx, qy, qz = pose

    # Transformo pose 3D
    ## Armo la matriz de transformación de 4x4
    transformation_matrix[0:3, 3] = [x, y, z]

    ## Transformo pose
    transformed_position = np.dot(transformation_matrix, np.array([x, y, z, 1.0]))

    # Armo matrix de rotación desde los quaternions
    rotation_matrix = R.from_quat([qx, qy, qz, qw]).as_matrix()

    # Aplico rotación
    transformed_rotation_matrix = np.dot(transformation_matrix[:3, :3], rotation_matrix)

    # Vuelvo a quaterniones
    transformed_quaternion = R.from_matrix(transformed_rotation_matrix).as_quat()

    # Nota: El quaternion original viene en formato qw,qx,qy,qz
    return np.array([ transformed_position[0],
                  transformed_position[1],
                  transformed_position[2],
                  transformed_quaternion[3],
                  transformed_quaternion[0],
                  transformed_quaternion[1],
                  transformed_quaternion[2]])

def main():
    ground_truth_path = "./MH_01_easy/mav0/state_groundtruth_estimate0/data.csv"
    ground_truth_trajectory = []

    # Punto a
    ## Parsear los datos de entrada. Solo primero 8 columnas
    try:
        with open(ground_truth_path, 'r') as file:
            csv_reader = csv.reader(file)
            first_row = next(csv_reader)
            print(first_row[0:8])
            for row in csv_reader:
                pose = np.array(row[0:8]).astype(float)
                pose_in_camera = transform_pose(pose, T_BS)
                ground_truth_trajectory.append(pose_in_camera)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

    print("Filas: ", len(ground_truth_trajectory))

    # Punto b
    ## Convertir a segundos y transformar coordenadas
    ground_truth_trajectory_seconds = []
    for row in ground_truth_trajectory:
        timestamp_seconds = np.array([row[0] / 1e9])
        new_row = np.hstack((timestamp_seconds, row[1:]))
        ground_truth_trajectory_seconds.append(new_row)

    ## Imprime primeras 5 lineas
    print("Camino original:")
    with open(ground_truth_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for i,row in enumerate(csv_reader):
            print(row)
            if i > 5:
                break

    print("Camino transformado:")
    print(ground_truth_trajectory[:5])
    print("Camino transformado y en segundos:")
    print(ground_truth_trajectory_seconds[:5])

    # Punto c
    # Busco solo las poses 3D
    positions = np.array([pose[1:4] for pose in ground_truth_trajectory_seconds])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the trajectory
    ax.plot(positions[:, 0], positions[:, 1], positions[:, 2])

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Trajectory')

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main()
