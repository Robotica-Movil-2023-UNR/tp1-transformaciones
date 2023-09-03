# Ejercicio 5
1. El ground-truth se encuentra en coordenadas de la IMU (Body). Se pide crear un script en python
que dada la trayectoría ground-truth (timestamp, x, y, z, qw, qx, qy, qz) (primeras 8 columnas del
archivo MH_01/state_groundtruth_estimate0.csv) genere el ground-truth pero que este esté dado
en el sistema de coordenadas de la cámara inicial. Para esto deberá utilizar las transformaciones
provistas en el dataset.
2. Modifique el script para que el timestamp del nuevo ground-truth este en segundos con precisión de
nanosegundos. Agregar las primeras 5 filas del ground-truth resultante y las del original del dataset
al informe.
3. Modifique el script para que genere una imagen con ambos ground-truth (el camino de la IMU y el
camino de la cámara). Aplique las transformaciones necesaria para que ambos caminos esten en el
sisma de coordenadas del ground-truth original. Agregar la imagen al informe.

## Pasos para ejecutar el código
Dependencias:
- Numpy
- csv
- scipy
- matplotlib
- Dataset Machine Hall 01 Easy [MH_01_easy](https://projects.asl.ethz.ch/datasets/doku.php?id=kmavvisualinertialdatasets)

En una terminal ejecutar:
```bash
python3 main.py
```
