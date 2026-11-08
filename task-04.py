import numpy as np
from scipy.stats import skew, kurtosis

x = np.fromstring(input(), sep=" ")
print(np.mean(x), np.median(x), np.var(x), np.std(x), np.var(x, ddof=1), np.std(x, ddof=1), skew(x, bias=False), kurtosis(x, bias=False))
