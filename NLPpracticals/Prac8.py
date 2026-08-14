import nltk 
from nltk import word_tokenize,bigrams
from collections import Counter
nltk.download('punkt')
text=input("Enter the text: ")
wordds=word_tokenize(text.lower())
unigrams_counts=Counter(wordds)
bigrams_counts=Counter(bigrams(wordds))


sentence=input("Enter the sentence: ")

input_words=word_tokenize(sentence.lower())
input_bigrams=list(bigrams(input_words))
probability=1

for w1,w2 in input_bigrams:
    
    if unigrams_counts[w1]>0:
        probability*=bigrams_counts[(w1,w2)]/unigrams_counts[w1]
    else:
        probability=0
        
print("The probability of the sentence is: ",probability)   
print("bigrams counts: ",bigrams_counts)