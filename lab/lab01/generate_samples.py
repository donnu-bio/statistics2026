
import numpy as np  
def generate_samples():

    distributions = [
        "normal",
        "uniform",
        "exponential",
        "outliers"
    ]

    order = np.random.permutation(distributions)

    samples = {}
    method = {}

    for name in order:

        if name == "normal":
            x = np.random.normal(50, 10, 200)
            method_ = 0

        elif name == "uniform":
            x = np.random.uniform(20, 80, 200)
            method_ = 0    

        elif name == "exponential":
            x = np.random.exponential(20, 200)
            method_ = 1

        elif name == "outliers":
            x = np.random.normal(50, 10, 200)
            x[:5] = [120, 130, 140, 150, 160]
            method_ = 1

        samples[name] = x
        method[name] = method_

    return samples, order, method