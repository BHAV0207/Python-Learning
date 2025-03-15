import pandas as pd

data = {
  "city" : ["jaipur" , "nagpur" , "mumbai"],
  "population" : [100000 , 200000 , 300000]
}

df = pd.DataFrame(data)

print(df)