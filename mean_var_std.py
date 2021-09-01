import numpy as np


def calculate(list):
    """
    Calculates the mean, variance, and standard deviation

    Args:
        list (list): Represents the list of numbers to use

    Returns:
        dict: Returns a dictionary containing the mean, variance, and standard deviation if valid    
    """
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")

    arr = np.reshape(list, (3, 3))
    means = [(np.mean(arr, axis=0)).tolist(),
             (np.mean(arr, axis=1)).tolist(), np.mean(arr)]

    variances = [(np.var(arr, axis=0)).tolist(),
                 (np.var(arr, axis=1)).tolist(), np.var(arr)]

    standardDevs = [(np.std(arr, axis=0)).tolist(),
                    (np.std(arr, axis=1)).tolist(), np.std(arr)]

    maxs = [(np.max(arr, axis=0)).tolist(),
            (np.max(arr, axis=1)).tolist(), np.max(arr)]

    mins = [(np.min(arr, axis=0)).tolist(),
            (np.min(arr, axis=1)).tolist(), np.min(arr)]

    sums = [(np.sum(arr, axis=0)).tolist(),
            (np.sum(arr, axis=1)).tolist(), np.sum(arr)]

    return {
        "mean": means,
        "variance": variances,
        "standard deviation": standardDevs,
        "max": maxs,
        "min": mins,
        "sum": sums
    }
