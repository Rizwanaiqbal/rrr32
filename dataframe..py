import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    "student": ["a","b","c","d","e"],
     "hours":[5, 2, 7, 3, 6],
     "percentage(%)":[75, 60, 85, 65, 80]
      } 

df = pd.DataFrame(data)
print(df)
x = df[["hours"]]
y = df["percentage(%)"]
modle = LinearRegression() #this is for calling
model.fit(x,y)
r_squared =model.score(X,y)
print(r_squared)
accuracy =model.score(X,y)
print(f"the accuracy of model is {accuracy*100:.2f}")
new =pd.DataFrame({"hours":4})
prediction = model.predict(new)
print(prediction)