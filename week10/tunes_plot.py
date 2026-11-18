# Week 9 lab solution - plotting the tune index with pandas and matplotlib
# Run from the root of the repo:  python week10/tunes_plot.py

import pandas as pd
import matplotlib.pyplot as plt

# Step 1 - Load the file

df = pd.read_csv("data/tuneindex.csv")
print(len(df))  # 24482

# Step 2 - Tune types

counts = df["tune_type"].value_counts().head(10)

plt.bar(counts.index, counts.values)
plt.xlabel("Tune type")
plt.ylabel("Number of tunes")
plt.title("Most common tune types (before fixing)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("step2_before.png")
plt.show()

# Q1. Reels are the most common tune type
# Q2. "reel" and "Reel" are counted as two different tune types because
#     they have different capital letters, so reels appear twice

df["tune_type"] = df["tune_type"].str.lower()
counts = df["tune_type"].value_counts().head(10)

plt.bar(counts.index, counts.values)
plt.xlabel("Tune type")
plt.ylabel("Number of tunes")
plt.title("Most common tune types")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("step2.png")
plt.show()

# Q3. About 7,700 reels (7,726 exactly)

# Step 3 - Downloads

plt.hist(df["downloaded"], bins=50, edgecolor="black")
plt.xlabel("Downloads")
plt.ylabel("Number of tunes")
plt.title("How many times tunes are downloaded")
plt.savefig("step3.png")
plt.show()

# Q4. Only a few. Most tunes are in the bars on the far left, under about
#     500 downloads, and the bars get smaller and smaller to the right
# Q5. About 9,000 tunes are in the tallest bar (0 to about 90 downloads)
# Q6. No. Cooley's is only one tune, so its bar at 4,432 is 1 tune high.
#     That's far too small to see next to bars that are thousands high

# Step 4 - Common or popular?

top = counts.index
common = df[df["tune_type"].isin(top)]
avg = common.groupby("tune_type")["downloaded"].mean()
avg = avg.sort_values(ascending=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.bar(counts.index, counts.values)
ax1.set_title("Number of tunes")
ax1.set_xlabel("Tune type")
ax1.set_ylabel("Number of tunes")
ax1.tick_params(axis="x", labelrotation=45)

ax2.bar(avg.index, avg.values, color="orange")
ax2.set_title("Average downloads")
ax2.set_xlabel("Tune type")
ax2.set_ylabel("Average downloads")
ax2.tick_params(axis="x", labelrotation=45)

plt.tight_layout()
plt.savefig("step4.png")
plt.show()

# Q7. Reels have the most downloads on average (about 340).
#     Strathspeys have the least (about 140)
# Q8. Slides. They are 8th of 10 for how many tunes there are, but 3rd for
#     average downloads. There aren't many slides, but the ones there are
#     get downloaded a lot. (Slip jigs are another example: 6th and 4th)

# Step 5 - Time signatures

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

reels = df[df["tune_type"] == "reel"]["time_sig"].value_counts().head(3)
axes[0, 0].bar(reels.index, reels.values)
axes[0, 0].set_title("Reels")
axes[0, 0].set_ylabel("Number of tunes")

jigs = df[df["tune_type"] == "jig"]["time_sig"].value_counts().head(3)
axes[0, 1].bar(jigs.index, jigs.values)
axes[0, 1].set_title("Jigs")

polkas = df[df["tune_type"] == "polka"]["time_sig"].value_counts().head(3)
axes[1, 0].bar(polkas.index, polkas.values)
axes[1, 0].set_title("Polkas")
axes[1, 0].set_xlabel("Time signature")
axes[1, 0].set_ylabel("Number of tunes")

waltzes = df[df["tune_type"] == "waltz"]["time_sig"].value_counts().head(3)
axes[1, 1].bar(waltzes.index, waltzes.values)
axes[1, 1].set_title("Waltzes")
axes[1, 1].set_xlabel("Time signature")

plt.tight_layout()
plt.savefig("step5.png")
plt.show()

# Q9. Jigs 6/8, polkas 2/4, waltzes 3/4
# Q10. C means "common time", which is 4/4. C| means "cut time", which is
#      2/2. Reels are in 4/4 (or 2/2), so some people write the time
#      signature for a reel using the symbol instead of the numbers

# Step 6 - Old tunes and new tunes

session = df[df["source"] == 1]
session_reels = session[session["tune_type"] == "reel"]
session_jigs = session[session["tune_type"] == "jig"]

plt.figure(figsize=(10, 5))
plt.scatter(session_reels["x"], session_reels["downloaded"], s=5, alpha=0.3, label="Reels")
plt.scatter(session_jigs["x"], session_jigs["downloaded"], s=5, alpha=0.3, label="Jigs")
plt.xlabel("Tune number on thesession.org")
plt.ylabel("Downloads")
plt.title("Old tunes and new tunes")
plt.legend()
plt.savefig("step6.png")
plt.show()

# Q11. The old tunes (low numbers) get the most downloads. They have been
#      on the site the longest, and the best known tunes were the first
#      ones people added
# Q12. Below about 1,000

# Step 7 - Save your graphs
# Each graph is saved with plt.savefig just before plt.show above

# Bonus - Keys

keys = df["key_sig"].value_counts().head(10)

plt.bar(keys.index, keys.values)
plt.xlabel("Key")
plt.ylabel("Number of tunes")
plt.title("Most common keys (before fixing)")
plt.savefig("bonus_keys_before.png")
plt.show()

df["key_sig"] = df["key_sig"].replace({
    "G": "Gmaj",
    "D": "Dmaj",
    "A": "Amaj",
    "C": "Cmaj",
    "F": "Fmaj",
    "Am": "Amin",
    "Em": "Emin",
    "Bm": "Bmin",
    "Dm": "Dmin",
})
keys = df["key_sig"].value_counts().head(10)

plt.bar(keys.index, keys.values)
plt.xlabel("Key")
plt.ylabel("Number of tunes")
plt.title("Most common keys")
plt.savefig("bonus_keys.png")
plt.show()

# G major and D major are the two most common keys, and they are very
# close (7,470 and 7,332)
