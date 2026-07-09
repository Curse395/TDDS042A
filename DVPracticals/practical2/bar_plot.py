import seaborn as sns
import matplotlib.pyplot as plt
tips = sns.load_dataset("tips")

sns.barplot(data=tips, x="day", y="total_bill")

plt.title("Bar Plot")
plt.show()