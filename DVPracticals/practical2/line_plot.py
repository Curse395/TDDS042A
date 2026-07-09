import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.lineplot(data=tips, x="size", y="total_bill")

plt.title("Line Plot")
plt.show()