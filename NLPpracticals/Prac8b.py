import nltk 
from nltk import word_tokenize,bigrams,trigrams
from collections import Counter
nltk.download('punkt')
text=input("Enter the text: ")
wordds=word_tokenize(text.lower())
unigrams_counts=Counter(wordds)
bigrams_counts=Counter(bigrams(wordds))
trigrams_counts=Counter(trigrams(wordds))


sentence=input("Enter the sentence: ")

input_words=word_tokenize(sentence.lower())
input_bigrams=list(bigrams(input_words))
input_trigrams=list(trigrams(input_words))
probability=1

for w1,w2,w3 in input_trigrams:
    
    if unigrams_counts[w1]>0:
        probability*=trigrams_counts[(w1,w2,w3)]/bigrams_counts[(w1,w2)]
    else:
        probability=0
        
print("The probability of the sentence is: ",probability)   
print("bigrams counts: ",input_bigrams)