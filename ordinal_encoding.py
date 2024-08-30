import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# sample data
data={'size':['Small','Medium','Large','Small','Large']}
df=pd.DataFrame(data)

# define order of categories
size_order=['Small','Medium','Large']

# create an ordinal encounter
ordinal_encoder=OrdinalEncoder(categories=[size_order])

# fit and transfer the data
encoder_data=ordinal_encoder.fit_transform(df[['size']])

# [[0.]
#  [1.]
#  [2.]
#  [0.]
#  [2.]]
print(encoder_data)
