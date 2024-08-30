# one hot encoding
import pandas as pd

# sample data
data={'color':['red','green','blue','green','red']}
df=pd.DataFrame(data)

#one hot encoder the data
one_hot_encoded_data=pd.get_dummies(df['color'])

print(one_hot_encoded_data)
