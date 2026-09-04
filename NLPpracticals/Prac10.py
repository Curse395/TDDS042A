import numpy as np 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

n=int(input("Enter the number of sentences: "))

texts=[]
labels=[]

for i in range(n):
    sentence=input("Enter sentence: ")
    label=int(input("Enter label(1 = Positive, 0 = Negative): "))
    
    texts.append(sentence)
    labels.append(label)
labels=np.array(labels)

tokenizer=Tokenizer()
tokenizer.fit_on_texts(texts)
sequences=tokenizer.texts_to_sequences(texts)
padded=pad_sequences(sequences,maxlen=10)

print("\n Tokenized sequences:")
print(padded)

print("\n padded sequences:")
print(padded)

model=Sequential()

model.add(Embedding(input_dim=len(tokenizer.word_index)+1,output_dim=8,input_length=10))

model.add(SimpleRNN(16))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(padded,labels,epochs=10)

print("\nPredictions:")
predictions=model.predict(padded)
