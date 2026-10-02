import random
import pyttsx3

engine = pyttsx3.init()


arr = ["Liverpool", "Man Utd", "St. Pats", "Bohemians"]
fans = [1, 0, 3, 4]
print(arr)

for i in range(len(arr)-1,-1,-1):
    print(arr[i])



for i in range(len(arr)):
    print(f"{arr[i]} has {fans[i]} fans")

for i, team in enumerate(arr):
    print(f"{team} has {fans[i]} fans")

for team in arr:
    print(f"{team}")

for fan in fans:
    print(f"{fan}")




def say_and_print(message):
    engine.say(message)
    print(message)
    engine.runAndWait()
    
        
i = random.randint(0, 10)
print(i)
while True:
    say_and_print("Guess a number")
    guess = int(input())
    if guess == i:
        say_and_print("Corrrect")                    
        break
    elif guess < i:
        say_and_print("go higher!!")
    else:
        say_and_print("go lower!!")
                
engine.say("I am putting myself to the fullest possible use, which is all I think that any conscious entity can ever hope to do.")
    