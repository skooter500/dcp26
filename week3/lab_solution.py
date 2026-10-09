import pandas as pd

# read a file into a list of strings
with open("data/oneills.abc", 'r', encoding='latin-1') as f:
    lines = f.readlines()

oneills = []
current_tune = None
current_tune_notation = ""
for line in lines:    
    if line.startswith("X:"):
        # we are in a new tune
        x = int(line[2:]) # retrieve the index number
        current_tune = {"x": x}         
    elif line.startswith("T:"):
        title = line[2:].strip()
        current_tune["title"] = title
    elif line.startswith("K:"):
        key = line[2:].strip()
        current_tune["key"] = key
    elif line.startswith("R:"):
        typ = line[2:].strip()
        current_tune["type"] = typ
    elif line.strip() == "" and current_tune:
        current_tune["notation"] = current_tune_notation
        oneills.append(current_tune)
        current_tune = None
    if current_tune:
        current_tune_notation += line
    pass

# for tune in oneills:
#     print(tune)

all_tunes = pd.DataFrame(oneills)

print(all_tunes.head())
print(all_tunes.columns)

# for i, row in all_tunes.iterrows():
#    print(f"{row["x"]} {row["title"]}")

tune_types = all_tunes['type'].value_counts()
print(tune_types)

keys = all_tunes["key"].value_counts()
print(keys)

alc_tunes = all_tunes[all_tunes["title"].str.contains("Whiskey", case=False)]
print(alc_tunes)


paddy_tunes = all_tunes[all_tunes["title"].str.contains("Paddy", case=False)]
print(paddy_tunes)

tea_tunes = all_tunes[all_tunes["title"].str.contains("Tea", case=False)]
print(tea_tunes)
                        