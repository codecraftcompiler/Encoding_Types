# label encoding
from sklearn.preprocessing import LabelEncoder

# Sample data
data=['red','green','blue','green','red']

# create a label encoder
label_encoder=LabelEncoder()

# fit and transfer the data
encoder_data=label_encoder.fit_transform(data)

# output: array([2, 1, 0, 1, 2])
print(encoder_data)       