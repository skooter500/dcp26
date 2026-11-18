import pandas as pd

df = pd.read_csv("data/exams.csv")

print(df.loc[10])

df.info()
print(df.head())
print(df.tail())
print(df.count())
print(df.columns)
print("-----")
print(df.value_counts())
print("-----")
print(df.describe())

print(df["first"])
print(df[["first", "last"]])
print("-----")

print(df[df["engagement"] < 40])

df = df.fillna(0)
# df[["exam"].]
print("-----")
print(df.groupby("first").count())
print("-----")
print(df["engagement"].isna(). sum())
print("-----")

df["total"] = df["engagement"] * .2 +  df["assignment"] *.3 +  df["exam"] *.5 
df["result"] = "pass"
# if df["total"] >= 40 else "fail"



df.loc[(df["total"] <= 40), "result"] = "fail"

print(df.head())

for i, s in df.iterrows():
    print(f"{i} {s['first']} {s['last']}")
print("-----")
for i, s in reversed(list(df.iterrows())):
    print(f"{s['first']} {s['last']}")

