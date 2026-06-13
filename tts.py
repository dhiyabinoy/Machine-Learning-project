import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
df=pd.read_csv("train.csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.info())
y=df["SalePrice"]
x=df[["GrLivArea","BedroomAbvGr","FullBath","HalfBath","OverallQual"]]
print(y.head())
print(x.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=SVC()
model.fit(x_train,y_train)
pred=model.predict(x_test)
print(pred) 
accuracy=accuracy_score(pred,y_test)
print(accuracy)
plt.scatter(x["BedroomAbvGr"],y,color="blue",label="Actual Data")
plt.plot(x["BedroomAbvGr"],model.predict(x),color="red",label="Regression line")
plt.xlabel("BedroomAbvGr")
plt.ylabel("SalePrice")
plt.title("svc")
plt.legend()
plt.show()