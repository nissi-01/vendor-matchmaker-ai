import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("vendors.csv")

# AI score
df['score'] = (
    (df['rating'] * 0.6)
    +
    (df['experience'] * 0.3)
    -
    (df['price'] / 100000 * 0.1)
)

# Features
X = df[
    ['price', 'rating', 'experience']
]

# Target
y = df['score']

# Train model
model = RandomForestRegressor()

model.fit(X, y)