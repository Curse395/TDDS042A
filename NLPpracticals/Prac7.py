from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

documents = input("Enter sentences separated by a period: ").split('.')
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
lda = LatentDirichletAllocation(n_components=5, random_state=42)
lda.fit(X)
words = vectorizer.get_feature_names_out()

topic_number = 1
for topic in lda.components_:
    print(f"Topic",topic_number)
    top_words= topic.argsort()[-2:]
    for word_index in top_words:
        print(words[word_index])
    topic_number += 1
    print()