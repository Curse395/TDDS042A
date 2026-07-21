import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
text='Text normalization is an essential step in processing text data! It includes steps like stemming and lemmanization.'
text=text.lower()
text=text.translate(str.maketrans('', '', string.punctuation))
tokens=word_tokenize(text)
stop_words=set(stopwords.words('english'))
filtered_tokens=[]
for word in tokens:
    if word not in stop_words:
        filtered_tokens.append(word)
        stemmer=PorterStemmer()
        stemmed_words=[]
        for word in filtered_tokens:
            stemmed_words.append(stemmer.stem(word))
            lemmatizer=WordNetLemmatizer()
            lemmatized_words=[]
            for word in filtered_tokens:
                lemmatized_words.append(lemmatizer.lemmatize(word))
                
                print("original token:", tokens)
                print("filtered token:", filtered_tokens)
                print("stemmed words:", stemmed_words)
                print("lemmatized words:", lemmatized_words)