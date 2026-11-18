students = {}

def total_mark(student):
    return student["engagement"] * .2 + student["assignment"] * .6 + student["exam"] * .5

def pass_fail(student) -> bool:
        if student["exam"] < 40:
             return False
        elif total_mark(student) >= 40:
             return True


def load_students():
    global students
    with open("data/exams.prn") as f:
        header = f.readline()      # read (and skip) the first line
        for line in f:             # loop over the remaining lines
            # print(line, end="")    # each line already ends with "\n"

            last= line[0:14].strip()
            first = line[14:25].strip()
            number= line[25:42].strip()
            engagement = line[42:56].strip()
            assignment = line[56:68].strip()
            exam = line[68:80].strip()

            # print(last)
            # print(first)
            # print(number)
            # print(engagement)
            # print(assignment)
            # print(exam)

            student = {}
            student["last"] = last
            student["first"] = first
            student["number"] = number
            if engagement.isdigit():
                student["engagement"] = int(engagement)
            else:
                 student["engagement"] = 0
            
            if assignment.isdigit():
                student["assignment"] = int(assignment)
            else:
                    student["assignment"] = 0
            
            if exam.isdigit():
                student["exam"] = int(exam)
            else:
                student["exam"] = 0
            
            # print(student)
            students[number] = student
    print(len(students))

def print_all():
    global students
    for number, student in students.items():
        print(student)
        l = [str(s) for s in student.values()]
        s = ",".join(l)
        s += ", " + str(total_mark(student))
        print(s)

def pass_students():
    global students
    for number, student in students.items():
            if pass_fail(student):
                l = [str(s) for s in student.values()]
                s = ",".join(l)
                s += ", " + str(total_mark(student))
                print(s)

def fail_students():
    global students
    for number, student in students.items():
            if not pass_fail(student):
                l = [str(s) for s in student.values()]
                s = ",".join(l)
                s += ", " + str(total_mark(student))
                print(s)

def find_student(number):
    if number in students.keys():
        print(students[number])
    else:
        print("Not found")

users = {"bryan": "python",
         "ann": "c++",
         "nova": "genai"
                         }

print(users)

for user, password in users.items():
     print(f"{user}  \t    {password}")

for user in users.keys():
     print(f"{user}")

for password in users.values():
     print(f"{password}")

l = [10,7,6,48,0,33,7,9,4,6]

s = 0
for n in l:
     print(n)
     s += n

for i in range(len(l)):
     print(l[i])

     


def check_login():
    while True:
        user = input("Enter username:")
        password = input("Enter password:")
        if user in users.keys():
             if password == users[user]:
                  return True

             
        # if user == "bryan" and password == "python":
        #     return True
        # else:
        #     print("Login incorrect")

def menu():
    check_login()
    while True:
        print("Student Management System")
        print("------")
        print("1. Print all")
        print("2. Pass students")
        print("3. Fail students")
        print("4. Find student")
        print("5. Quit")
        i = int(input())
        match i:
            case 1:
                print_all()
            case 2:
                pass_students()
            case 3:
                fail_students()
            case 4:
                print("Enter a student number:")
                number = input()
                find_student(number)
            case 5:
                quit()

load_students()
menu()