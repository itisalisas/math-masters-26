import numpy as np
from scipy.stats import bootstrap


def bootci(est, x):
    return np.array(bootstrap((x,), est, vectorized=False, method="percentile").confidence_interval)
