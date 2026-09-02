import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data = {
    'Annual_Income': [15, 16, 17, 18, 19, 20, 60, 67, 62, 63],
    'Spending_Score': [39, 81, 6, 77, 40, 76, 6, 77, 3, 72]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)
X = df[['Annual_Income', 'Spending_Score']]
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

df['Cluster'] = kmeans.labels_

print("\nClustered Dataset:")
print(df)
print("\nCluster Centroids:")
print(kmeans.cluster_centers_)

plt.figure(figsize=(8, 5))
plt.scatter(
    X['Annual_Income'],
    X['Spending_Score'],
    c=df['Cluster'],
    s=100
)

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker='X',
    s=300
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("K-Means Clustering")
plt.show()