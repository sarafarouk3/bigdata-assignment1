df = globals()["df"]

print(df.info())
print(df.describe().T)


# Insight 1
sum = 0
for count in df.isnull().sum():
  sum = sum + count

text1 = f"There are {sum} rows with null content."
eda1 = open("eda-in-1.txt", "a")
eda1.write(text1)
eda1.close()

# Instight 2
text2 = f"There is {df.duplicated().sum()} duplicated row(s) in the data"
eda2 = open("eda-in-2.txt", "a")
eda2.write(text2)
eda2.close()

# Insight 3
# print(df['Customer Status'].unique())
uniq_values = ','.join(df['Customer Status'].unique())
text3 = (f"The column Customer Status has 6 unique values: {uniq_values}\n"
         "These unique values can be made to 3 with data transformation"
         )

eda3 = open("eda-in-3.txt", "a")
eda3.write(text3)
eda3.close()



exec(open('dpre.py').read())
