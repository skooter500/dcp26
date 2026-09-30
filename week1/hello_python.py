# declare a variable
a = 10
name = "Bryan"
print(a)
print(name)



t = int(input("Times"))
arr = []
#
for i in range(t):
    arr.append(1000)
for i in range(len(arr)):
    print(arr[i])

# get input
name = input("What is your name?")
print(name)

# if statement
if name == "Bryan" or name == "skooter500":
    print(f"User {name} is a leprechaun!")
else:
    print(f"User {name} is a K-Pop star!")

# loops
for c in name:
    print(c)

for i in range(len(name)):
    print(name[i])

i = 10
while (i>=0):
    print(i)
    i -= 1

if name.isdigit():
    print(f"{name} is a number")


count = int(input("How many employees? "))
total_hours = 0.0
total_pay = 0.0
print()
print("PAYROLL RUN          23/09/1961")
print(f"{'NAME':<12}{'HOURS':>7}{'RATE':>10}{'PAY':>10}")
for i in range(count):
    name = input("Name: ")
    hours = float(input("Hours: "))
    rate = float(input("Rate: "))
    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    total_hours += hours
    total_pay += pay
    print(f"{name:<12}{hours:>7.1f}{rate:>10.2f}{pay:>10.2f}")
print("-" * 42)
print(f"{'TOTAL':<12}{total_hours:>7.1f}{'':>10}{total_pay:>10.2f}")