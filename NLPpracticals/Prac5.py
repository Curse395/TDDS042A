from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

documents=[
    "exam timetable is announced",
    "exam is going to be on offee platform",
    "results will be declared soon enough",
    "results will be given only in hand to the students and online portal only"
]

labels=[0,0,1,1]
vectorizer=CountVectorizer()

x=vectorizer.fit_transform(documents)

model=LogisticRegression()
model.fit(x,labels)

test_doc=["exam is going to be on offee platform"]
test_vec=vectorizer.transform(test_doc)

prediction=model.predict(test_vec)

if prediction[0] == 1:
    print(test_doc," - Prediction: Exam")
else:
    print(test_doc,"- Prediction: Results")