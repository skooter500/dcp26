import pandas as pd

df = pd.read_csv("data/tuneindex.csv", )


df.info()
# print(df.head())
# print(df.describe())
# print("----")
# print(df["title"])
# print(df[["title", "alt_title", "downloaded"]])
# print("downloaded")
# print(df[df["downloaded"] > 1000])

mask = df["title"].str.contains("WhiStle", case = False)
filtered = df[mask]
print(filtered)

print(filtered["title"])
s = "Hello"

print(s.startswith("He"))

# Tunes that start with The
# Tunes where the title contains whiskey or beer

print(df[df["title"].str.startswith("The")]["title"])

mask = df["title"].str.startswith("The")
print(df[mask][["title", "downloaded"]])

# all tunes that end with "Spear"
mask = df["title"].str.endswith("Spear")
print(df[mask][["title", "downloaded", "tune_type"]])

print(df.count())

print(df["downloaded"].sum())
print(df[["title", "downloaded"]].min())
print(df[["title", "downloaded"]].max())
print(df["downloaded"].max())


mask = df["tune_type"] == "Reel"
print(df[mask][["title", "tune_type"]])

df = pd.read_csv("data/understanding.csv")
df.info()