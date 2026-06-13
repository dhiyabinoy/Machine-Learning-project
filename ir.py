import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt
df=pd.read_csv("Iris.csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.info())
y=df["PetalLengthCm"]
x=df.drop(["Species","Id","PetalLengthCm"],axis=1)
print(y.head())
print(x.head())
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
pred=model.predict(x_test)
print(pred) 
mse=mean_squared_error(pred,y_test)
print(mse)
r2_score=r2_score(pred,y_test)
print(r2_score)
plt.scatter(x["PetalWidthCm"],y,color="blue",label="Actual Data")
plt.plot(x["PetalWidthCm"],model.predict(x),color="red",label="Regression line")
plt.xlabel("PetalWidthCm")
plt.ylabel("PetalLengthCm")
plt.title("Linear Regression")
plt.legend()
plt.show()