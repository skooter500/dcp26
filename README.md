# TU850 Data Centric Programming 2026 - SEMESTER 1

```
Welcome to the Metaverse
```

![](holo.jpg)

## Assessment
- 20% Weekly submissions
- [30% Assignment/Test]()
- 50% Exam

# Resources
- [CSResources git repo](https://github.com/skooter500/csresources/blob/main/git_ref.pdf). Here you will find links to the previous courses and all my quick references
- [Git for poets](https://www.youtube.com/watch?v=BCQHnlnPusY)
- [Python a Crash Course](https://drive.google.com/file/d/1Hu_Rd-spILyNWmoBw1HubHWrkmfz0zKh/view)
- https://codingbat.com/python
* [The Coding Train](https://www.youtube.com/channel/UCvjgXvBlbQiydffZU7m1_aw)
* [The Nature of Code](http://natureofcode.com/)
* [Games Fleadh](http://www.gamesfleadh.ie/)

What you will need to install:

- Python
- VSCode
- Git

Course Notes:
- [Python Introduction](week1/python_complete_presentation.pdf)
- [Python Fundamentals](week4/python_fundamentals.pdf)
- [Pandas](pandas.pdf)
- [SQL Databases]()
- [TKInter](week4/tkinter_slides.pdf)
- [MatPlotLib](week10/matplotlib_lesson.pdf)


Quick References:
- [Python Quick Reference](week1/python_quick_ref.html)
- [Git Quick Reference](http://github.com/skooter500/csresources/git_ref.pdf)


## Week 3 - Lists, Dictionaries, Strings, Slicing

- [Slides](week4/python_fundamentals.pdf)


### Lab 3 - Parsing Traditional Music Scores in ABC Notation

ABC is a text-based music score notation system. [Read about ABC notation](https://abcnotation.com/).  Each tune has metadata (title, key, type) and the melody.

An ABC file looks like this:

```
X:21001 
T:FUNNY TAILOR, The
R:jig 
M:6/8
L:1/8
K:G
BA|GED GAB|GBA G2G|...

%%%

X:21002 
T:BUNKER HILL (reel)
R:reel
K:G
...
```

- Every tune starts with `X:` followed by a number!!
- `T:` or `t:` lines contain the title (can have multiple T: lines - first is main title, second is alt_title)
- `R:` is the tune type (reel, jig, hornpipe, slip jig, etc.)
- `K:` is the musical key (G, D, Em, Dmaj, etc.)
- Tunes end with blank lines
- Everything from X: to the blank lines is the tune

## Loading the file

```
# read the file to a list of strings
with open("data/oneills.abc", 'r', encoding='latin-1') as f:
    lines = f.readlines()

```

- Print the total number of lines
- Print the first 20 lines to see the structure
- Print the last 10 lines
- Print the file backwards!

## Parse Tunes into a List of Dictionaries

- Loop through all lines
- When you see a line starting with "X:", that's a new tune
- Collect lines until you hit blank lines
- A blank line is when `line.strip() == ""`

```python
tunes = []
in_tune = False

for line in lines:
    # Check if this starts a new tune
    if line.startswith("X:"):
        pass
    ...
    ...
        
```

### Dictionaries
```python
# Creating dictionaries
star = {
    "name": "Sirius",
    "distance": 2.6,
    "spectral_class": "A0m",
    "magnitude": 1.46
}

# Empty dictionary
empty = {}
also_empty = dict()

# From list of tuples
star2 = dict([("name", "Sol"), ("distance", 0)])
```

### Accessing Dictionary Values

```python
star = {
    "name": "Sirius",
    "distance": 2.6,
    "spectral_class": "A0m"
}

# Access by key
print(star["name"])  # "Sirius"
print(star["distance"])  # 2.6

# Safe access with get() - returns None if key doesn't exist
print(star.get("name"))  # "Sirius"
print(star.get("color"))  # None
print(star.get("color", "Unknown"))  # "Unknown" (default value)

# This causes an error!
# print(star["color"])  # KeyError: 'color'
```

### Modifying Dictionaries

```python
star = {"name": "Sirius", "distance": 2.6}

# Add new key-value pair
star["spectral_class"] = "A0m"

# Modify existing value
star["distance"] = 2.64

# Remove key-value pair
del star["spectral_class"]

# Remove and return value
magnitude = star.pop("magnitude", None)

# Update multiple values at once
star.update({"distance": 2.6, "color": "white"})

# Clear all items
star.clear()
```

### Dictionary Operations

```python
star = {
    "name": "Sirius",
    "distance": 2.6,
    "spectral_class": "A0m"
}

# Length (number of key-value pairs)
print(len(star))  # 3

# Check if key exists
print("name" in star)  # True
print("color" in star)  # False

# Get all keys
print(star.keys())  # dict_keys(['name', 'distance', 'spectral_class'])

# Get all values
print(star.values())  # dict_values(['Sirius', 2.6, 'A0m'])

# Get all key-value pairs
print(star.items())  # dict_items([('name', 'Sirius'), ('distance', 2.6), ('spectral_class', 'A0m')])
```

### Iterating Over Dictionaries

```python
star = {
    "name": "Sirius",
    "distance": 2.6,
    "spectral_class": "A0m"
}

# Iterate over keys (default)
for key in star:
    print(key)

# Explicitly iterate over keys
for key in star.keys():
    print(f"{key}: {star[key]}")

# Iterate over values
for value in star.values():
    print(value)

# Iterate over key-value pairs (most common)
for key, value in star.items():
    print(f"{key} = {value}")
```



For each tune, extract:
- **X:** The tune ID (just the number part)
- **T:** Title (first T: line you encounter)
- **Alt Title:** Second T: line (if it exists)
- **R:** Tune type (the text after R:)
- **K:** Key (the text after K:)
- **Notation:** All lines from X: to end (as a single string)

```
tune = {
    'X': None,
    'title': None,
    'alt_title': None,
    'tune_type': None,
    'key': None,
}
```

Final output should be a printout of all the titles and alt_titles for each tune in the file by iterating through the list of dictionaries.
 
```python
print(f"Found {len(tunes)} tunes")
print("\nFirst tune:")
print(tunes[0])
print("\nLast tune:")
print(tunes[-1])
```

Additional challenges!

- Count of all the reels
- Count of all the jigs
- List of all tunes with "Green" in the title

(One line of code for each!)

Submit your code on brightspace. Attempt this lab without the use of AI code. If you wish, you may ask AI prompts such as:

"Explain how to load text files in python with examples"

"Teach me how to use dictionaries with examples"
"How does a for loop work. Show me"

## Week 2 - Python Fundamentals

### Lab

# Lab 1: Night Shift at the Data Centre

You will find many interesting interesting videos in my [playlist of computer science history](https://www.youtube.com/watch?v=Iz_L47OKjJg&list=PL1n0B6z4e_E7afXxRh-nbjmRUssHMZDns).

```
 ______________________________________________________________________________
|  /  IBM 1401 DATA PROCESSING SYSTEM                                  1961  |
| |   0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 |
| |   1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 |
| |   2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 |
| |   ...                                                                    |
|_|__________________________________________________________________________|
```

It's 1961. You've just been hired as the night-shift operator at a data centre running an **IBM 1401**, the first computer to sell more than 10,000 units. It has 4,000 characters of memory (not 4 GB, not 4 MB: 4,000 characters), reads [punched cards](https://en.wikipedia.org/wiki/Punched_card) at 800 cards a minute, and prints 600 lines a minute on a line printer. Every night, boxes of punched cards arrive: payroll, invoices, stock counts. Your job is to get the data through the machine before the morning.

The 1401's software is written in Autocoder and FORTRAN. You've been asked to rewrite the operator's toolkit in Python. Build it up one option at a time and test each one before moving to the next.

Rules of the machine room:
- Only what you already know: variables, `input`, `if`, `while`, `for`, strings and f-strings.
- No lists, tuples, dictionaries or sets. The 1401 didn't have them and neither do you.
---

## The Menu

Start with this. It should loop until the operator chooses 0, and complain about anything that isn't a valid option.

```
IBM 1401 OPERATOR CONSOLE
=========================
1. Card reader check
2. Payroll batch run
3. Job time estimate
4. Core memory calculator
5. Two-digit date check
6. GCD (converted from FORTRAN)
7. Interest table (converted from FORTRAN)
0. Power down

Select: _
```

Each option below is one branch of your menu.

---

## Option 1: Card Reader Check

A punched card has exactly **80 columns**. Records longer than 80 characters get truncated, which is how a lot of 1960s data got corrupted.

Ask the operator to type a record. Then report:
- its length, and whether it's `OK`, `SHORT` (padded with spaces to 80) or `OVERFLOW` (and show what would be lost)
- how many digits, letters and spaces it contains (loop over the string one character at a time; `ch.isdigit()` and `ch.isalpha()` will help)

```
Record: SMITH J          00042  0000450  DUBLIN
Length: 43 -> SHORT, padded to 80
Digits: 15  Letters: 12  Spaces: 16
```

---

## Option 2: Payroll Batch Run

The classic 1401 job. Ask how many employees are in tonight's batch, then for each one read their **name**, **hours worked** and **hourly rate**.

- The first 40 hours are paid at the normal rate.
- Anything over 40 is overtime at **1.5×**.

Print a report with **aligned columns** and totals at the bottom. f-strings can pad and align: `f"{name:<12}"` left-aligns in 12 characters, `f"{pay:>9.2f}"` right-aligns a number to 2 decimal places in 9 characters.

```
How many employees? 3
Name: Murphy
Hours: 38
Rate: 12.50
...

PAYROLL RUN          23/09/1961
NAME          HOURS      RATE       PAY
Murphy         38.0     12.50    475.00
O'Brien        45.0     15.00    712.50
Byrne          40.0     10.00    400.00
------------------------------------------
TOTAL         123.0             1587.50
```

Keep running totals in variables. Nothing needs to be stored once it's been printed. That's how the 1401 worked: one record in, one line out.

---

## Option 3: Job Time Estimate

The card reader manages **800 cards per minute** and the printer **600 lines per minute**. They don't overlap: the job reads all the cards, then prints.

Ask how many cards are in the job and how many lines it will print. Work out the total time and display it as `h:mm:ss`. Then tell the operator whether the job will be finished before the morning shift arrives at **08:00**, given the current time (ask for it as hours and minutes on the 24-hour clock).

```
Cards: 250000
Lines: 180000
Start time (hh mm): 22 30
Reading: 312.5 min, Printing: 300.0 min
Total: 10:12:30
Finishes at 08:42 -> LATE. Morning shift will not be happy.
```

---

## Option 4: Core Memory Calculator

The 1401 was sold with 1.4K, 2K, 4K, 8K, 12K or 16K **characters** of core memory. Ask the operator:
- how many characters of memory the machine has
- how many records are in the file and how many characters per record

Print how many records fit in memory at once, and therefore how many **passes** the job needs (round up! a partial pass is still a pass). Then, for perspective, print how many 1401s at that size you'd need to equal the memory of a laptop with 8 GB (treat 1 GB as 1,000,000,000 characters). Use thousands separators: `f"{n:,}"`.

```
Memory (characters): 4000
Records: 25000
Characters per record: 80
Records per pass: 50
Passes needed: 500
An 8 GB laptop has the memory of 2,000,000 of these machines.
```

---

## Option 5: Two-Digit Date Check

Memory was so tight that years were stored as **two digits**. This seemed fine in 1961. It seemed less fine in 1999.

Ask for a date as `DD MM YY`. Decide the century using a **pivot**: two-digit years from 00 to 30 mean 20xx, and 31 to 99 mean 19xx. Then validate the date properly:
- months 1 to 12
- correct number of days for the month, including leap years (divisible by 4, except centuries, except every 400 years)

Print the full date or an error. Test with `29 02 00` (valid: 2000 is a leap year), `29 02 99` (invalid), `31 04 61` (invalid), `31 12 99`.

```
Date (DD MM YY): 29 02 00
29/02/2000 -> VALID (leap year)
```

---

## Options 6 and 7: Converting from FORTRAN

Two of the programs in the machine room are in FORTRAN. Nobody left knows FORTRAN. Convert them to Python and add them to your menu.

Things you need to know about 1960s FORTRAN:
- Everything is in **CAPITALS** and starts in column 7 (columns 1–5 are for **statement labels**, the numbers on the left).
- `C` in column 1 means a comment.
- `GO TO 20` jumps to the line labelled `20`.
- `IF (X) 10, 20, 30` is the **arithmetic IF**: jump to label 10 if X is negative, 20 if zero, 30 if positive.
- `DO 50 I = 1, 10` is a loop: everything down to the line labelled `50` runs with I = 1, 2, ... 10.
- `READ` and `WRITE` are input and output; ignore the `FORMAT` statements and just print something sensible.
- Variables starting with I, J, K, L, M or N are integers. Everything else is real (a float). Integer division truncates, just like `//`.

### Option 6: Greatest Common Divisor

```fortran
C     EUCLID GCD.  READ TWO INTEGERS, PRINT THEIR GCD.
      READ (5, 100) M, N
  100 FORMAT (2I10)
   10 K = M - (M / N) * N
      IF (K) 20, 30, 20
   20 M = N
      N = K
      GO TO 10
   30 WRITE (6, 200) N
  200 FORMAT (1X, 'GCD IS ', I10)
      STOP
      END
```

Before you write any Python, trace it on paper with M = 48 and N = 18. What does line 10 actually compute? (Python has an operator that does it in one go.) Your version should use a `while` loop and no `GO TO`, because Python doesn't have one.

### Option 7: Compound Interest Table

```fortran
C     COMPOUND INTEREST TABLE
      READ (5, 100) P, R, NYRS
  100 FORMAT (2F10.2, I5)
      WRITE (6, 200)
  200 FORMAT (1X, 'YEAR   BALANCE   INTEREST')
      TOTAL = 0.0
      DO 50 I = 1, NYRS
      AMT = P * R / 100.0
      TOTAL = TOTAL + AMT
      P = P + AMT
      WRITE (6, 300) I, P, AMT
  300 FORMAT (1X, I4, 2F10.2)
   50 CONTINUE
      WRITE (6, 400) TOTAL
  400 FORMAT (1X, 'TOTAL INTEREST', F10.2)
      STOP
      END
```

Reads a principal, an annual rate (as a percentage) and a number of years. Convert the `DO` loop into a `for` loop with `range`, and match the column layout using f-strings.

```
Principal: 1000
Rate (%): 5
Years: 3
YEAR   BALANCE   INTEREST
   1   1050.00      50.00
   2   1102.50      52.50
   3   1157.63      55.13
TOTAL INTEREST    157.63
```

## Handing In

Submit `ibm1401.py` on Brightspace. You don't have to complete everything! Make sure the menu handles bad input without crashing, and that every option returns to the menu when it's done. Also NO AI today. This is the 1960's.

- [Learn how to use bash and git](https://github.com/skooter500/csresources/blob/main/gitlab.md)
- [Python Quick Reference](week1/python_quick_ref.html)

## Week 1 - Introduction to the Course

- [Python Notes](week1/python_complete_presentation.pdf)
- [Python Quick Reference (Printable)](week1/python_quick_ref.html)
- [Hello Python](week1/hello_python.py)