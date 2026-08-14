from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.decomposition import NMF

documents = input("Enter sentences on one topic only: ").split(".")

vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

lda = LatentDirichletAllocation(n_components=2)
lda.fit(X)

nmf = NMF(n_components=2)
nmf.fit(X)

words = vectorizer.get_feature_names_out()

print("\nTopic modeling using LDA")
topic_number = 1
for topic in lda.components_:
    print("Topic", topic_number)
    top_words = topic.argsort()[-5:]
    for index in top_words:
        print(words[index])
    topic_number += 1
    print()

print("\nTopic modeling using NMF")
topic_number = 1
for topic in nmf.components_:
    print("Topic", topic_number)
    top_words = topic.argsort()[-5:]
    for index in top_words:
        print(words[index])
    topic_number += 1
    print()