def calculate_mean(array):
    return sum(array) / len(array)


def calculate_variance(array):
    mean_value = calculate_mean(array)
    variance = sum([(val - mean_value) ** 2 for val in array]) / (len(array) - 1)
    return variance
