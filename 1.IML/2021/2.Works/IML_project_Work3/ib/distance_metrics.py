import numpy as np


def HVDM(array, datapoint):
    # Calculate column-wise standard deviation in array
    column_std = np.std(array, axis=0)
    # Subtract array from datapoint, and divide it by 4*standard deviation
    subtract = np.abs(np.subtract(array, datapoint)) / 4 * column_std
    # Return the sum of each row
    return np.sum(subtract, axis=1)
