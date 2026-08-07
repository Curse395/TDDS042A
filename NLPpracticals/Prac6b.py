from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
sentences = input("Enter sentences separated by a period: ").split('.')

for sentence in sentences:
    sentiment_score = analyzer.polarity_scores(sentence)
    print("Sentence: ", sentence)
    print("Sentiment score: ", round(sentiment_score['compound'], 2))
    print()