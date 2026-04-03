import numpy as np

# --- Constructors ---
def vec2(x: float, y: float) -> np.ndarray:
    return np.array([x, y], dtype=float)

# --- Operations ---
def dot(a: np.ndarray, b: np.ndarray) -> float:
    return np.dot(a, b)

def dist(a: np.ndarray, b: np.ndarray) -> float:
    return np.linalg.norm(a - b)
