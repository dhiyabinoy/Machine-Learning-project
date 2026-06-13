import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
import matplotlib.pyplot as plt 
df=pd.read_csv("train (1).csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.info())
df['Sex']=df['Sex'].map({'male':0,'female':1})
df['Age']=df['Age'].fillna(df['Age'].mean())
y=df["Survived"]
x=df [["Pclass", "Sex","Age","SibSp","Parch","Fare"]]
print(y.head())
print(x.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=SVC()
model.fit(x_train,y_train)
pred=model.predict(x_test)
print(pred) 
accuracy=accuracy_score(pred,y_test)
print(accuracy)
plt.bar(["SVC"],[accuracy],color="red")
plt.ylim(0,1)
plt.xlabel("model")
plt.ylabel("accuracy")
plt.title("SVC")
plt.show()
