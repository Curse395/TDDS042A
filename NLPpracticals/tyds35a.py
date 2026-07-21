import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt_tab")
text = "Hello, world! NLP is fun."
tokens=word_tokenize(text)
print("Word Tokens:", tokens)