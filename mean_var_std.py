import numpy as np


def calculate(lst):
  if len(lst) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    matriz = np.array(lst).reshape(3, 3)
    calculations = {
        "mean": [
            np.mean(matriz, axis=0).tolist(),
            np.mean(matriz, axis=1).tolist(),
            np.mean(matriz)
        ],
        "variance": [
            np.var(matriz, axis=0).tolist(),
            np.var(matriz, axis=1).tolist(),
            np.var(matriz)
        ],
        "standard deviation": [
            np.std(matriz, axis=0).tolist(),
            np.std(matriz, axis=1).tolist(),
            np.std(matriz)
        ],
        "max": [
            np.max(matriz, axis=0).tolist(),
            np.max(matriz, axis=1).tolist(),
            np.max(matriz)
        ],
        "min": [
            np.min(matriz, axis=0).tolist(),
            np.min(matriz, axis=1).tolist(),
            np.min(matriz)
        ],
        "sum": [
            np.sum(matriz, axis=0).tolist(),
            np.sum(matriz, axis=1).tolist(),
            np.sum(matriz)
        ]
    }
    return calculations
