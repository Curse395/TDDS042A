import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, export_text


data=pd.read_csv("D:\\TYDS42A\\weather.csv")
print("Dataset:\n")
print(data)

data = data.drop("Day", axis=1)
le = LabelEncoder()

for column in data.columns:
    data[column] = le.fit_transform(data[column])

print("\nEncoded Dataset:\n")
print(data)

X = data.drop("Play Golf", axis=1)
y = data["Play Golf"]

model = DecisionTreeClassifier(criterion="entropy")
model.fit(X, y)

print("\nDecision Tree:\n")
print(export_text(model, feature_names=list(X.columns)))
sample = [[2, 0, 0, 0]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("\nPrediction: Yes (Play Golf)")
else:
    print("\nPrediction: No (Don't Play Golf)")