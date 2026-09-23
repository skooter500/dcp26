# Python Fundamentals - Complete Lesson Plan

## Session 1: Variables, Data Types, and Operators

### Learning Objectives
- Understand what variables are and how to use them
- Identify different data types (int, float, str, bool)
- Perform operations using arithmetic, comparison, and logical operators

### Activities

**1. Variable Declaration Challenge**
- Have students declare variables for their: name, age, height, favorite color, and whether they like Python
- Practice type checking using `type()` function
- Convert between different types and observe what happens

**2. Calculator Exercise**
Students create a simple calculator that:
- Takes two numbers as input
- Performs all arithmetic operations (+, -, *, /, //, %, **)
- Displays results with descriptive messages

**3. Comparison Challenge**
Write a program that:
- Compares two numbers entered by the user
- Prints which is larger, smaller, or if they're equal
- Uses all comparison operators

### Exercises

**Exercise 1.1: Personal Profile**
```
Create variables for a person's profile:
- Full name, age, city, is_employed (boolean)
- Print a formatted sentence using all variables
- Convert age to months and days
```

**Exercise 1.2: Temperature Converter**
```
Convert Celsius to Fahrenheit using: F = (C * 9/5) + 32
- Take input in Celsius
- Calculate and display Fahrenheit
- Also convert to Kelvin: K = C + 273.15
```

**Exercise 1.3: Logic Puzzle**
```
Given three variables: age = 25, has_license = True, has_car = False
Use logical operators to determine:
- Can they drive? (age >= 18 AND has_license)
- Need to buy a car? (has_license AND NOT has_car)
- Ready for road trip? (all three conditions)
```

---

## Session 2: Control Flow and Decision Making

### Learning Objectives
- Use if/elif/else statements to make decisions
- Nest conditional statements
- Apply ternary operators for simple conditions

### Activities

**1. Age Classifier**
Students build a program that:
- Takes age as input
- Categorizes: child (<13), teenager (13-19), adult (20-59), senior (60+)
- Provides appropriate messages for each category

**2. Grade Calculator**
Create a grading system:
- Input: numerical score (0-100)
- Output: letter grade (A, B, C, D, F)
- Include +/- grades (e.g., A-, B+)

**3. Login Simulator**
Build a simple authentication system:
- Check username and password
- Maximum 3 attempts
- Different messages for wrong username vs wrong password

### Exercises

**Exercise 2.1: Leap Year Checker**
```
A year is a leap year if:
- Divisible by 4 AND
- (NOT divisible by 100 OR divisible by 400)
Write a program to check if a year is a leap year.
```

**Exercise 2.2: Ticket Pricing**
```
Movie ticket prices:
- Children (< 12): $8
- Students (12-17): $10
- Adults (18-64): $15
- Seniors (65+): $10
Input age and student status, output price.
```

**Exercise 2.3: Number Analyzer**
```
Input a number and determine:
- Positive, negative, or zero
- Even or odd
- Divisible by 5
- Single, double, or triple digit
Use nested if statements.
```

---

## Session 3: Loops - For and While

### Learning Objectives
- Iterate using for loops with ranges and sequences
- Control loops with break and continue
- Use while loops for conditional repetition
- Apply enumerate for indexed iteration

### Activities

**1. Multiplication Table Generator**
- Use nested loops to create multiplication tables
- Allow user to choose which table (1-12)
- Format output in a neat grid

**2. Pattern Printing**
Create programs to print:
```
*
**
***
****
*****
```
```
    *
   ***
  *****
 *******
*********
```

**3. Number Guessing Game**
- Computer picks random number (1-100)
- Player has limited guesses
- Provide "higher" or "lower" hints
- Use while loop and break

### Exercises

**Exercise 3.1: Sum and Average**
```
Use a for loop to:
- Calculate sum of numbers 1 to 100
- Calculate average
- Find sum of even numbers only
- Find sum of numbers divisible by 3
```

**Exercise 3.2: Factorial Calculator**
```
Calculate factorial using:
a) For loop
b) While loop
Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
```

**Exercise 3.3: Menu-Driven Program**
```
Create a calculator with menu:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Use while loop to keep showing menu until user exits.
Handle invalid menu choices.
```

**Exercise 3.4: Skip Multiples**
```
Print numbers 1 to 50, but:
- Skip multiples of 3 (use continue)
- Stop at first multiple of 7 after 30 (use break)
```

---

## Session 4: Functions

### Learning Objectives
- Define and call functions
- Use parameters and return values
- Implement default parameters
- Create functions with multiple return values
- Write proper docstrings

### Activities

**1. Function Library**
Students create a math_tools.py with functions:
- `square(n)` - returns n squared
- `cube(n)` - returns n cubed
- `is_even(n)` - returns True if even
- `max_of_three(a, b, c)` - returns largest
- `celsius_to_fahrenheit(c)` - temperature conversion

**2. String Utilities**
Create string helper functions:
- `count_vowels(text)` - count vowels in string
- `reverse_string(text)` - return reversed string
- `is_palindrome(text)` - check if palindrome
- `title_case(text)` - capitalize first letter of each word

**3. Validation Functions**
Build input validators:
- `is_valid_email(email)` - basic email check
- `is_strong_password(pwd)` - password strength
- `is_valid_age(age)` - age range check

### Exercises

**Exercise 4.1: Area Calculator**
```
Create functions to calculate area of:
- Rectangle (length, width)
- Circle (radius) - use pi = 3.14159
- Triangle (base, height)
- Square (side)

Each function should have a docstring.
Create a menu to let user choose shape.
```

**Exercise 4.2: Prime Number Checker**
```
Write a function is_prime(n) that:
- Returns True if n is prime
- Returns False otherwise
- Handles edge cases (n < 2)

Then write list_primes(start, end) that:
- Returns list of all primes in range
```

**Exercise 4.3: Statistics Calculator**
```
Create functions that take a list of numbers:
- calculate_mean(numbers) - average
- calculate_median(numbers) - middle value
- calculate_range(numbers) - max - min
- calculate_sum(numbers) - total

Test with: [12, 15, 18, 20, 22, 25, 30]
```

**Exercise 4.4: Text Analyzer**
```
Function: analyze_text(text)
Returns a dictionary with:
- character_count
- word_count
- sentence_count (count periods)
- average_word_length

Test with a paragraph.
```

---

## Session 5: Lists and Tuples

### Learning Objectives
- Create and manipulate lists
- Use list methods (append, insert, remove, pop, sort)
- Slice lists to extract portions
- Understand tuples and their immutability
- Unpack tuples and lists

### Activities

**1. Shopping List Manager**
Create a program that:
- Maintains a shopping list
- Allows add, remove, view, and clear operations
- Shows items with numbers
- Sorts items alphabetically

**2. Grade Book**
Manage student grades:
- Store grades in a list
- Add new grades
- Calculate average
- Find highest and lowest
- Remove outliers

**3. Coordinate System**
Work with tuples:
- Store points as (x, y) tuples
- Calculate distance between two points
- Find if point is in a certain quadrant
- Cannot modify coordinates (demonstrate immutability)

### Exercises

**Exercise 5.1: List Operations**
```
Given: numbers = [3, 7, 1, 9, 2, 5, 8, 4, 6]
Perform:
1. Add 10 to the list
2. Remove the number 1
3. Insert 0 at the beginning
4. Sort the list
5. Reverse the list
6. Find index of 5
7. Count how many times 2 appears
```

**Exercise 5.2: List Slicing Challenge**
```
Given: letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
Extract:
1. First 3 elements
2. Last 3 elements
3. Every second element
4. Elements from index 2 to 7
5. Reverse the list using slicing
6. Middle 4 elements
```

**Exercise 5.3: Merge and Deduplicate**
```
Given two lists:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

Create a program that:
- Merges both lists
- Removes duplicates
- Sorts the result
- Finds common elements
```

**Exercise 5.4: Tuple Unpacking**
```
Create a function get_student_info() that returns:
- name, age, grade, gpa (as a tuple)

Unpack the values and print:
"[name] is [age] years old, in grade [grade] with GPA [gpa]"

Create a list of 5 students and process them all.
```

---

## Session 6: Dictionaries and Sets

### Learning Objectives
- Create and manipulate dictionaries
- Access, add, modify, and delete key-value pairs
- Iterate through dictionaries
- Use sets for unique collections
- Perform set operations (union, intersection, difference)

### Activities

**1. Phone Book Application**
Build a contact manager:
- Store contacts as {name: phone_number}
- Add new contacts
- Search by name
- Update phone numbers
- Delete contacts
- Display all contacts

**2. Word Frequency Counter**
Analyze text:
- Count how many times each word appears
- Store in dictionary: {word: count}
- Find most common word
- Display sorted by frequency

**3. Student Records System**
Manage student data:
```python
students = {
    "S001": {"name": "Alice", "age": 20, "major": "CS", "gpa": 3.8},
    "S002": {"name": "Bob", "age": 21, "major": "Math", "gpa": 3.6}
}
```
- Add new students
- Update information
- Search by ID
- List all students in a major

### Exercises

**Exercise 6.1: Inventory System**
```
Create a store inventory:
inventory = {
    "apple": {"price": 0.99, "quantity": 50},
    "banana": {"price": 0.59, "quantity": 100},
    "orange": {"price": 1.29, "quantity": 75}
}

Functions needed:
- add_item(name, price, quantity)
- update_quantity(name, quantity)
- calculate_total_value()
- low_stock_alert(threshold) - items below threshold
```

**Exercise 6.2: Set Operations**
```
Given:
students_math = {"Alice", "Bob", "Charlie", "David"}
students_science = {"Bob", "David", "Eve", "Frank"}

Find:
1. Students in both classes (intersection)
2. Students in either class (union)
3. Students only in math (difference)
4. Students in exactly one class (symmetric difference)
```

**Exercise 6.3: Character Frequency**
```
Write a program that:
- Takes a sentence as input
- Creates a dictionary of character frequencies
- Ignores spaces and is case-insensitive
- Displays results sorted by frequency

Example: "Hello World" → {'l': 3, 'o': 2, 'h': 1, 'e': 1, ...}
```

**Exercise 6.4: Menu Order System**
```
menu = {
    "burger": 5.99,
    "pizza": 8.99,
    "salad": 6.99,
    "soda": 1.99
}

Create a program that:
- Shows menu
- Takes orders (item and quantity)
- Stores order in dictionary
- Calculates total bill
- Applies 10% discount if total > $20
```

---

## Session 7: String Manipulation

### Learning Objectives
- Use string methods for transformation and searching
- Format strings using f-strings and format()
- Split and join strings
- Validate and process text data

### Activities

**1. Text Processor**
Build a program that:
- Converts text to uppercase, lowercase, title case
- Counts words, characters, sentences
- Removes extra spaces
- Finds and replaces words

**2. Name Formatter**
Create a name processing tool:
- Input: "john doe"
- Output variations: "John Doe", "DOE, John", "J. Doe", "john.doe@email.com"

**3. Password Strength Checker**
Analyze passwords:
- Check length (min 8 characters)
- Contains uppercase and lowercase
- Contains digits
- Contains special characters
- Give strength rating (Weak/Medium/Strong)

### Exercises

**Exercise 7.1: String Methods Practice**
```
Given: text = "  Python Programming is FUN!  "

Perform:
1. Remove whitespace from both ends
2. Convert to lowercase
3. Convert to uppercase
4. Replace "FUN" with "AWESOME"
5. Check if it starts with "Python"
6. Check if it ends with "!"
7. Count the number of 'a's (case insensitive)
```

**Exercise 7.2: Email Validator**
```
Write a function is_valid_email(email) that checks:
- Contains exactly one @
- Has characters before @
- Has at least one dot after @
- Ends with valid domain (.com, .org, .edu, .net)
- No spaces

Test cases:
"user@example.com" → True
"invalid.email" → False
"user@domain" → False
```

**Exercise 7.3: CSV Parser**
```
Given CSV string:
"John,30,Engineer,New York
Jane,25,Doctor,Los Angeles
Bob,35,Teacher,Chicago"

Write a program that:
- Splits into lines
- Splits each line by comma
- Creates a list of dictionaries with keys: name, age, job, city
- Prints in formatted way
```

**Exercise 7.4: Pig Latin Translator**
```
Pig Latin rules:
- If word starts with vowel: add "way" (apple → appleway)
- If word starts with consonant: move consonants to end + "ay" (hello → ellohay)

Create function to_pig_latin(word) and translate sentences.
```

---

## Session 8: List Comprehensions

### Learning Objectives
- Create lists using comprehensions
- Apply filtering with conditional comprehensions
- Use nested comprehensions
- Create dictionary and set comprehensions

### Activities

**1. Data Transformation Challenge**
Given data, use comprehensions to:
- Extract specific fields
- Filter based on conditions
- Transform values (e.g., square all numbers)
- Create derived data structures

**2. Matrix Operations**
Use list comprehensions for:
- Creating identity matrix
- Transposing matrix
- Flattening nested lists
- Element-wise operations

**3. Text Processing**
Process text using comprehensions:
- Extract words of certain length
- Convert list to uppercase
- Filter out stop words
- Count character frequencies

### Exercises

**Exercise 8.1: Basic Comprehensions**
```
Create using list comprehensions:
1. Squares of numbers 1 to 20
2. Even numbers from 1 to 50
3. Lengths of words in a sentence
4. First characters of each word
5. Numbers divisible by both 3 and 5 from 1 to 100
```

**Exercise 8.2: Conditional Comprehensions**
```
Given: numbers = [12, 7, 18, 5, 23, 30, 9, 15, 42]

Create lists using comprehensions:
1. Even numbers only
2. Numbers greater than 15
3. "Even" or "Odd" for each number
4. Squared if even, cubed if odd
5. Numbers that are multiples of 3
```

**Exercise 8.3: Nested Comprehensions**
```
Create using nested comprehensions:
1. Multiplication table (10x10)
2. All coordinate pairs (x,y) where x and y range 0-4
3. Flattened list from [[1,2], [3,4], [5,6]]
4. List of all possible 2-letter combinations from "ABC"
```

**Exercise 8.4: Dictionary Comprehensions**
```
Create using dictionary comprehensions:
1. {number: square} for numbers 1-10
2. {letter: position} for "ABCDEFGHIJ"
3. Invert a dictionary (swap keys and values)
4. Filter dictionary keeping only values > 50
5. {word: len(word)} for list of words
```

---

## Session 9: File Handling

### Learning Objectives
- Read from and write to text files
- Work with different file modes
- Process CSV files
- Handle file exceptions
- Use context managers (with statement)

### Activities

**1. Note-Taking Application**
Build a simple note app:
- Create new notes (append to file)
- Read and display all notes
- Search for keywords in notes
- Each note with timestamp

**2. Log File Analyzer**
Process a log file:
- Count total lines
- Find errors (lines containing "ERROR")
- Extract timestamps
- Create summary report

**3. Grade Book File Manager**
Store student grades in file:
- Save grades to file (name, grade)
- Load grades from file
- Calculate class average
- Find top performers

### Exercises

**Exercise 9.1: File Writer**
```
Create a program that:
1. Asks user for 5 favorite movies
2. Writes them to "movies.txt", one per line
3. Reads the file back
4. Displays movies with numbers
5. Counts total movies
```

**Exercise 9.2: Word Counter**
```
Read a text file and create a report:
- Total words
- Total characters (excluding spaces)
- Total lines
- Average words per line
- Longest word

Test with a paragraph saved in a file.
```

**Exercise 9.3: CSV Operations**
```
Create "students.csv" with:
Name,Age,Grade,GPA
Alice,20,A,3.8
Bob,21,B,3.4
...

Write programs to:
1. Read and display all records
2. Add new student record
3. Find students with GPA > 3.5
4. Calculate average GPA
5. Sort by name and save to new file
```

**Exercise 9.4: File Merger**
```
Given three files:
- file1.txt: "Hello"
- file2.txt: "World"
- file3.txt: "Python"

Create a program that:
- Reads all three files
- Merges content into "merged.txt"
- Each on a separate line
- Adds a blank line between each
```

---

## Session 10: Exception Handling

### Learning Objectives
- Understand different types of exceptions
- Use try-except blocks
- Handle multiple exceptions
- Use else and finally clauses
- Raise custom exceptions

### Activities

**1. Robust Calculator**
Build a calculator that:
- Handles division by zero
- Validates numeric input
- Handles invalid operations
- Never crashes
- Provides helpful error messages

**2. File Operations with Error Handling**
Create file manager that:
- Handles FileNotFoundError
- Handles PermissionError
- Validates file paths
- Always closes files properly

**3. User Input Validator**
Build validators that:
- Check age (must be positive number)
- Check email format
- Check password strength
- Handle all input errors gracefully

### Exercises

**Exercise 10.1: Safe Division**
```
Create function safe_divide(a, b):
- Try to divide a by b
- Handle ZeroDivisionError
- Handle TypeError (if inputs aren't numbers)
- Handle any other exception
- Return result or error message

Test cases:
safe_divide(10, 2) → 5.0
safe_divide(10, 0) → "Error: Division by zero"
safe_divide(10, "2") → "Error: Invalid input type"
```

**Exercise 10.2: List Access**
```
Create function safe_get_element(lst, index):
- Try to access list[index]
- Handle IndexError
- Handle TypeError (if index not int)
- Return element or None with error message

Test with: numbers = [10, 20, 30, 40, 50]
```

**Exercise 10.3: File Reader with Error Handling**
```
Create function read_file_safely(filename):
- Try to open and read file
- Handle FileNotFoundError
- Handle PermissionError
- Handle any other IOError
- Use finally to print "Operation complete"
- Return file content or None

Test with existing and non-existing files.
```

**Exercise 10.4: Age Validator**
```
Create function validate_age(age_str):
- Convert string to integer
- Check if age is between 0 and 150
- Raise ValueError with message if invalid
- Handle ValueError in calling code
- Keep asking until valid age entered

Create main program that uses this validator.
```

---

## Session 11: Modules and Imports

### Learning Objectives
- Import and use built-in modules
- Use specific functions from modules
- Create custom modules
- Understand module structure
- Organize code across multiple files

### Activities

**1. Math Toolkit**
Explore math module:
- Calculate square roots, powers
- Use trigonometric functions
- Work with constants (pi, e)
- Round numbers different ways

**2. Random Number Games**
Use random module to create:
- Dice roller
- Lottery number generator
- Random password generator
- Coin flip simulator with statistics

**3. Date/Time Applications**
Use datetime module:
- Display current date and time
- Calculate age from birthdate
- Add/subtract days from dates
- Format dates in different ways
- Create countdown timer

### Exercises

**Exercise 11.1: Math Module Practice**
```
Using the math module:
1. Calculate square root of 144
2. Round 3.7 up and down
3. Calculate 2^10
4. Find factorial of 7
5. Calculate sin(45 degrees) - convert to radians first
6. Find GCD of 48 and 18
7. Calculate circle area with radius 5
```

**Exercise 11.2: Random Module Applications**
```
Create programs using random module:

1. Dice Game:
   - Roll two dice
   - Sum the values
   - Play 100 times
   - Count how many times you get 7

2. Password Generator:
   - Generate 8-character password
   - Include: uppercase, lowercase, digits, symbols
   - Make it configurable (length, character types)

3. Shuffle Quiz:
   - List of questions
   - Shuffle order
   - Present to user
   - Track score
```

**Exercise 11.3: Datetime Practice**
```
Using datetime module:

1. Current Information:
   - Display current date
   - Display current time
   - Display current day of week
   - Display current month name

2. Age Calculator:
   - Input birthdate
   - Calculate exact age in years, months, days
   - Calculate days until next birthday

3. Date Arithmetic:
   - Add 30 days to today
   - Subtract 7 days from today
   - Find difference between two dates
```

**Exercise 11.4: Create Your Own Module**
```
Create "string_utils.py" with functions:
- reverse(text)
- count_vowels(text)
- remove_spaces(text)
- title_case(text)
- is_palindrome(text)

Create "main.py" that:
- Imports your module
- Tests all functions
- Shows example usage

Create "math_utils.py" with functions:
- is_prime(n)
- factorial(n)
- fibonacci(n)
- gcd(a, b)

Import and test all functions.
```

---

## Mini Projects

These projects integrate multiple concepts and can be assigned after relevant sessions.

### Project 1: Contact Book Application
**Topics: Dictionaries, Files, Functions, Loops, Exception Handling**

Create a complete contact management system:
- Add new contacts (name, phone, email, address)
- View all contacts
- Search by name
- Update contact information
- Delete contacts
- Save to file
- Load from file
- Input validation
- Error handling

---

### Project 2: Student Grade Management System
**Topics: Lists, Dictionaries, Files, Functions, Statistics**

Build a grade tracking system:
- Add students with multiple grades
- Calculate individual averages
- Calculate class average
- Find highest/lowest grades
- Generate grade reports
- Save/load from CSV
- Sort students by average
- Grade distribution analysis

---

### Project 3: Text Adventure Game
**Topics: Functions, Control Flow, Loops, Strings**

Create an interactive story game:
- Multiple rooms/locations
- Inventory system
- Decision making (if/elif/else)
- Game loop
- Win/lose conditions
- Save game state
- Load game state

---

### Project 4: Personal Finance Tracker
**Topics: Dictionaries, Files, Datetime, Functions**

Build expense tracking app:
- Add income/expense transactions
- Categorize transactions
- View transaction history
- Calculate totals by category
- Monthly summaries
- Save to CSV file
- Date-based filtering
- Budget warnings

---

### Project 5: Quiz Application
**Topics: Lists, Dictionaries, Files, Random, Functions**

Create interactive quiz program:
- Load questions from file
- Randomize question order
- Multiple choice questions
- Track score
- Time limits (using datetime)
- High scores system
- Different difficulty levels
- Review wrong answers

---

### Project 6: Word Game (Hangman/Wordle)
**Topics: Strings, Lists, Sets, Random, Loops**

Build a word guessing game:
- Random word selection
- Letter guessing mechanism
- Track used letters
- Display progress
- Limited attempts
- Word difficulty levels
- Score calculation
- Word list from file

---

## Assessment Ideas

### Coding Challenges
1. **FizzBuzz** - Classic interview problem
2. **Palindrome Checker** - String manipulation
3. **Prime Number Generator** - Loops and logic
4. **List Flattening** - Nested lists
5. **Dictionary Merge** - Data structures

### Practical Exams
1. Create a function that solves a specific problem
2. Debug broken code
3. Complete partially written program
4. Optimize inefficient code
5. Write test cases for functions

### Project-Based Assessment
Students create a program that:
- Uses at least 5 different concepts
- Includes proper documentation
- Has error handling
- Saves/loads data
- Has user-friendly interface

---

## Additional Practice Resources

### Online Platforms
- **Codewars** - Kata challenges by difficulty
- **LeetCode** - Algorithm problems
- **HackerRank** - Skill-based challenges
- **Python Challenge** - Puzzle-based learning
- **Exercism** - Mentor-guided exercises

### Practice Suggestions
1. Daily coding challenges (15-30 minutes)
2. Peer code review sessions
3. Refactor old code
4. Contribute to small open source projects
5. Build personal utility scripts

### Extension Activities
- Explore Python standard library
- Learn about virtual environments
- Introduction to pip and packages
- Code style and PEP 8
- Introduction to debugging tools
- Version control with Git basics

---

## Tips for Teachers

### For Each Session:
1. **Live Coding** - Demonstrate concepts in real-time
2. **Think Aloud** - Explain your thought process
3. **Errors are Teaching Moments** - Show how to debug
4. **Incremental Complexity** - Start simple, add features
5. **Student Solutions** - Let students share different approaches

### Differentiation:
- **Struggling Students:** Pair programming, more examples, smaller steps
- **Advanced Students:** Optimization challenges, research topics, help peers
- **All Students:** Choice in project topics, self-paced exercises

### Best Practices:
- Encourage experimentation
- Celebrate mistakes as learning
- Use real-world examples
- Connect to student interests
- Regular feedback and code reviews
- Build portfolio of projects