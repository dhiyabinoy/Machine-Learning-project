import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
import matplotlib.pyplot as plt 
df=pd.read_csv("Iris.csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.info())
y=df["Species"]
x=df.drop(["Id","Species"],axis=1)
print(y.head())
print(x.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LogisticRegression(max_iter=200)
model.fit(x_train,y_train)
pred=model.predict(x_test)
print(pred) 
accuracy=accuracy_score(pred,y_test)
print(accuracy)
plt.bar(["LogisticRegression"],[accuracy],color="red")
plt.ylim(0,1)
plt.xlabel("model")
plt.ylabel("accuracy")
plt.title("LogisticRegression Model")
plt.show()