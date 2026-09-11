from transformers import pipeline

summarizer = pipeline("summarization", framework="pt")

text = """
Natural Language Processing (NLP) is a subfield of artificial intelligence (Al) that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful. NLP combines computational

linguistics, computer science, and machine learning to process and analyze large amounts of natural language data. Applications of NLP include text analysis, machine translation, sentiment analysis, and chatbots, among others.
"""

summary = summarizer(text)

print("Original Text:")

print(text)

print("\nSummary:")

print(summary[0]['summary_text'])
