from gensim.models import Word2Vec
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

sentences=[
["rahul","goes","to","college"],
["neha","studies","data science"],
["amit","likes","python"],
["priya","travels","by","car"],
["stdents","learn","machine","learning"]
]

model=Word2Vec(sentences,vector_size=50,window=2,min_count=1,sg=0)
words=list(model.wv.index_to_key)
print(words)
vectors=[model.wv[word] for word in words]
print(vectors)

pca=PCA(n_components=2)
result=pca.fit_transform(vectors)
plt.figure()
plt.scatter(result[:,0],result[:,1])

for i, word in enumerate(words):
    plt.annotate(word,xy=(result[i,0],result[i,1]))
    
    plt.title("Word2Vec Visualization")
    plt.show()