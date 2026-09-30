message = "The Way that can be named is not the Way"

print(message)
print(message.upper())
print(message.lower())
print(message.capitalize())

if message.lower().startswith("the way"):
    print("The way")
else:
    print("Not the way")

s = message[4:7]
print(s)
print(len(s))

s = message[8:12]
print(s)
print(len(s))

s = message[11:7:-1]
print(s)

s = message[20: 25]
print(s)

s = message[24:19:-1]
print(s)

message = message[::-1]
print(s)
message = message[::-1]
print(s)

def is_palindrome(s) -> bool:
    return s == s[::-1]

print(is_palindrome("racecar"))

words = message.split(" ")
for word in words:
    print(word)
new_message = " ".join(words)
print(new_message)

def initials_short(name):
    return ".".join(word[0] for word in name.split())

    
def initials(name):
    # "James Tiberius Kirk" should return J.T.K."
    words = name.split()
    initials = ""
    for word in words:
        initials += word[0].upper() + "."
    return initials

loc = message.find("Way", 5, 10)
print(loc)

def date_sep(date):
    # date is in the format "DD/MM/YYYY HH:MM:SS" 10/7/2027 9:12:7
    # print the different elements
    d = date.split("/")
    print(d[0])
    print(d[1])
    print(d[2][:4])

    t = date.split(":")
    print(t[0])
    print(t[1])
    print(t[2])
    pass


print(initials("James Tiberius Kirk"))
print(initials_short("James Tiberius Kirk"))

arr = [i * 5 for i in range(10)]

for i in arr:
    print(i)


date_sep("01/09/2028 9:21:09")