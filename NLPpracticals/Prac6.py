from textblob import TextBlob

sentences= input("Enter sentences separated by a period: ").split('.')
for sentence in sentences:
    blob=TextBlob(sentence)
    print("Sentence: ",sentence)
    print("Sentiment score: ",round(blob.sentiment.polarity, 2))
    print()