import seaborn as sns
import matplotlib.pyplot as plt

df = globals()["df"]

sns.heatmap(df.corr())
plt.savefig("vis.png")

exec(open('model.py').read())
