import seaborn as sns
import matplotlib.pyplot as plt

sns.kdeplot(list(map(float, input().split())))
plt.show()
