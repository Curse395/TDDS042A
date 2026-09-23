import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# Create dataset
data = {
    'Student': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Study_Hours': [5, 3, np.nan, 2, 6, 4],
    'Attendance': [85, 70, 90, np.nan, 95, 75],
    'Gender': ['Female', 'Male', 'Female', 'Male', np.nan, 'Female'],
    'Department': ['IT', 'CS', 'IT', 'AI', 'CS', np.nan],
    'Result': ['Pass', 'Pass', 'Pass', 'Fail', 'Pass', 'Fail']
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# ----------------------------------
# 1. Check missing values
# ----------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# ----------------------------------
# 2. Handle numerical missing values
# ----------------------------------

df['Study_Hours'] = df['Study_Hours'].fillna(
    df['Study_Hours'].mean()
)

df['Attendance'] = df['Attendance'].fillna(
    df['Attendance'].mean()
)

# ----------------------------------
# 3. Handle categorical missing values
# ----------------------------------

df['Gender'] = df['Gender'].fillna(
    df['Gender'].mode()[0]
)

df['Department'] = df['Department'].fillna(
    df['Department'].mode()[0]
)

print("\nAfter Handling Missing Values:")
print(df)

# ----------------------------------
# 4. Label Encoding
# ----------------------------------

le = LabelEncoder()

df['Gender_Encoded'] = le.fit_transform(
    df['Gender']
)

print("\nAfter Label Encoding:")
print(df[['Gender', 'Gender_Encoded']])

# ----------------------------------
# 5. One-Hot Encoding
# ----------------------------------

df_encoded = pd.get_dummies(
    df,
    columns=['Department'],
    dtype=int
)

print("\nAfter One-Hot Encoding:")
print(df_encoded)

# ----------------------------------
# 6. Normalization
# ----------------------------------

normalizer = MinMaxScaler()

df_normalized = df.copy()

df_normalized[['Study_Hours', 'Attendance']] = \
    normalizer.fit_transform(
        df_normalized[['Study_Hours', 'Attendance']]
    )

print("\nNormalized Data:")
print(df_normalized)

# ----------------------------------
# 7. Standardization
# ----------------------------------

standardizer = StandardScaler()

df_standardized = df.copy()

df_standardized[['Study_Hours', 'Attendance']] = \
    standardizer.fit_transform(
        df_standardized[['Study_Hours', 'Attendance']]
    )

print("\nStandardized Data:")
print(df_standardized)