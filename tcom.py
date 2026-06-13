import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import  LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
df=pd.read_csv("train (1).csv")
df['Sex']=df['Sex'].map({'male':0,'female':1})
df['Age']=df['Age'].fillna(df['Age'].mean())
y=df["Survived"]
x=df [["Pclass", "Sex","Age","SibSp","Parch","Fare"]]
print(y.head())
print(x.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
models={"Logistic Regression":LogisticRegression(max_iter=200), "Decison Tree":DecisionTreeClassifier(),
        "K Nearest Neighbors":KNeighborsClassifier(), "Random Forest":RandomForestClassifier(),
        "Support Vector Machine":SVC()}
names=[]
accuracy=[]
for name,model in models.items():
    model.fit(x_train,y_train)
    pred=model.predict(x_test)
    acc=accuracy_score(y_test,pred)    
    accuracy.append(acc)
    names.append(name)
    print(name,":",acc)
plt.bar(names,accuracy,color= "green")
plt.ylim(0,1)
plt.xlabel("model")
plt.ylabel("accuracy")
plt.title("comparison")
plt.xticks(rotation=20)
plt.show()
