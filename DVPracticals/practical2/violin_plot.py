import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

sns.violinplot(data=tips, x="day", y="total_bill")

plt.title("Violin Plot")
plt.show()