import numpy as np, matplotlib.pyplot as plt
x = np.fromstring(input(), sep=" "); p = float(input())
plt.ecdf(x); print(np.quantile(x, p, method="inverted_cdf")); plt.show()
