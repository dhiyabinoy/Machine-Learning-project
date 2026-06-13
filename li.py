import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt
df=pd.read_csv("linear regression dataset.csv")
print(df.head())
print(df.tail())
print(df.columns)
print(df.info())
df=df.dropna(subset=['y'])
y=df["y"]
x=df.drop(["y"],axis=1)
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
plt.scatter(x,y,color="blue",label="Actual Data")
plt.plot(x,model.predict(x),color="red",label="Regression line")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Regression")
plt.legend()
plt.show() 