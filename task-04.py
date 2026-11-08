import numpy as np
from scipy.stats import skew, kurtosis

x = np.fromstring(input(), sep=" ")
for name, value in {
    "Среднее": np.mean(x), "Медиана": np.median(x),
    "Дисперсия (смещённая)": np.var(x), "СКО (смещённое)": np.std(x),
    "Дисперсия (исправленная)": np.var(x, ddof=1), "СКО (исправленное)": np.std(x, ddof=1),
    "Асимметрия (несмещённая)": skew(x, bias=False), "Эксцесс (несмещённый)": kurtosis(x, bias=False)
}.items(): print(f"{name}: {value:.6g}")
