import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.preprocessing import LabelEncoder, MinMaxScaler


df = globals()["df"]

# Remove null rows
df.dropna(inplace=True)
# Remove duplicates
df.drop_duplicates()
# Drop Columns with unique values
df.drop(['Order ID', 'Product ID'], axis=1, inplace=True)
# Drop columns with data irrelevant to K means
df.drop(["Delivery Date", "Date Order was placed"], axis=1, inplace=True)
# Transform status column to lowercase
df['Customer Status'] = df['Customer Status'].str.lower()
# Transform status column from str to int
le = LabelEncoder()
df['Customer Status'] = le.fit_transform(df['Customer Status'])
# Apply feature scaling on columns
cols = df.columns
ms = MinMaxScaler()

df = ms.fit_transform(df)
df = pd.DataFrame(df, columns=[cols])

df.to_csv("res_dpre.csv")

globals()["df"] = df
exec(open('vis.py').read())
