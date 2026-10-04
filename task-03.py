import numpy as np
from scipy.optimize import minimize


def MLE(pdf, x, p0):
    r = minimize(lambda p: -np.log([pdf(t, p) for t in x]).sum(), p0, method="Nelder-Mead")
    if not r.success or not np.isfinite(r.fun):
        raise RuntimeError(r.message)
    return r.x
