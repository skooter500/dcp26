import random

with open("data/shakespere.txt", 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()

poems = {}

len_poem = 17
num_poems = int(len(lines) / len_poem)
for i in range(num_poems):
    start = i * len_poem
    index = lines[start].strip()
    poem = lines[start + 2: start + 16]
    poems[index] = poem    

for index in poems.keys():    
    print(f"{index} {poems[index][0].strip()}")

print(poems["XII"])

model = {}

def clean_word(word):
    word = word.replace(",", "")
    word = word.replace("`", "")
    word = word.replace("’", "")
    word = word.replace("?", "")
    word = word.replace("!", "")
    word = word.replace("\n", "")
    word = word.replace(".", "")
    word = word.replace(":", "")
    word = word.replace(";", "")
    word = word.replace("'", "")
    word = word.lower().strip()
    return word


def add_to_model(sentence):
    global model
    words = sentence.split(" ")
    for i in range(len(words)):
        word = clean_word(words[i])        
        after = None if i == len(words) - 1 else clean_word(words[i + 1])            
        if word in model.keys():
            after_list = model[word]
            if after and after not in after_list:
                after_list.append(after)
                model[word] = after_list
        else:
            if after:
                model[word] = [after]
            else:
                model[word] = []

def print_model():
    for key, value in model.items():
        print(f"{key} {value}")

for index in poems.keys():    
    poem = poems[index]
    for s in poem:
        add_to_model(s)


def generate_poem():
    global model
    poem = ""

    for j in range(14):
        word = random.choice(list(model.keys()))    
        sentence = ""
        for i in range(8):
            sentence += word + " "
            if word in model.keys():
                after_list = model[word]
                if len(after_list) == 0:
                    break
                else:
                    word = random.choice(after_list)
        poem +=  sentence + "\n"
    return poem

poem = generate_poem()
print()
print(poem)

# print_model()