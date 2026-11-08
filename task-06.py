import numpy as np
from scipy.stats import norm, t, kstwo

x = np.fromstring(input(), sep=" "); c = float(input()); m = int(input()); n = len(x)
if m == 3:
    a, b = map(float, input().split()); d = (b - a) * kstwo.ppf(c, n)
else:
    q = norm.ppf((1 + c) / 2) if m == 1 else t.ppf((1 + c) / 2, n - 1)
    d = q * np.std(x, ddof=1) / np.sqrt(n)
print(np.mean(x) + np.array([-d, d]))
