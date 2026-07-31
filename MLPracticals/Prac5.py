from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

iris=datasets.load_iris()

X=iris.data
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

svm=SVC(kernel='linear')

svm.fit(x_train,y_train)
y_pred=svm.predict(x_test)

print("Predicted values:",y_pred)
print("Accuracy:",accuracy_score(y_test,y_pred))
print("\nConfusion Matrix:\n",confusion_matrix(y_test,y_pred))
print("\nClassification Report:\n",classification_report(y_test,y_pred))