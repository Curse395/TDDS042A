import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df=pd.read_csv("D:\\TYDS42A\\student_data.csv")
print("Dataset:")
print(df)

x=df[['Hours studied']]
y=df[['Result']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)

y_pred=knn.predict(x_test)

print("\nACTUAL RESULTS:")
print(y_test)
print("\nPREDICTED RESULTS:")
print(y_pred)
print("\nACCURACY:")
print(accuracy_score(y_test, y_pred))
print("\n Accuracy:",accuracy_score)

y_pred=knn.predict([[5]])
print("Hours studied: 5")
print("Predicted Result:", y_pred[0])