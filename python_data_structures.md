# Python Data Structures
## Lists, Tuples, and Dictionaries

---

## Overview

Python has three fundamental data structures for storing collections:
- **Lists** - Ordered, mutable collections
- **Tuples** - Ordered, immutable collections
- **Dictionaries** - Key-value pairs for fast lookups

Understanding these is essential before diving into pandas!

---

## Part 1: Lists (Arrays)

### What is a List?

A **list** is an ordered collection that can hold any type of data. Lists are **mutable** - you can change them after creation.

```python
# Creating lists
tunes = ["Cooley's", "The Butterfly", "Banish Misfortune"]
downloads = [4432, 2767, 4292]
mixed = ["Sol", 0, True, 4.85]  # Can mix types

# Empty list
empty = []
also_empty = list()
```

### Accessing Elements

Lists use **zero-based indexing** - the first element is at index 0.

```python
tunes = ["Cooley's", "The Butterfly", "Banish Misfortune", "Sirius"]

# Positive indexing (from start)
print(tunes[0])   # "Cooley's" (first)
print(tunes[1])   # "The Butterfly"
print(tunes[3])   # "Sirius" (fourth)

# Negative indexing (from end)
print(tunes[-1])  # "Sirius" (last)
print(tunes[-2])  # "Banish Misfortune" (second to last)

# This causes an error!
# print(tunes[10])  # IndexError: list index out of range
```

### Slicing

Get a portion of a list using slice notation: `list[start:end:step]`

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4] - from index 2 up to (not including) 5
print(numbers[:3])     # [0, 1, 2] - first 3 elements
print(numbers[5:])     # [5, 6, 7, 8, 9] - from index 5 to end
print(numbers[-3:])    # [7, 8, 9] - last 3 elements
print(numbers[::2])    # [0, 2, 4, 6, 8] - every 2nd element
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] - reversed!
```

### Modifying Lists

Lists are **mutable** - you can change them.

```python
stars = ["Sol", "Sirius", "Procyon"]

# Change a single element
stars[1] = "Alpha Centauri"
print(stars)  # ["Sol", "Alpha Centauri", "Procyon"]

# Add to end
stars.append("Barnard's Star")
print(stars)  # ["Sol", "Alpha Centauri", "Procyon", "Barnard's Star"]

# Insert at position
stars.insert(1, "Rigel Kentaurus")
print(stars)  # ["Sol", "Rigel Kentaurus", "Alpha Centauri", "Procyon", "Barnard's Star"]

# Remove by value
stars.remove("Procyon")

# Remove by index
del stars[0]  # Removes "Sol"

# Remove and return last element
last = stars.pop()
print(last)  # "Barnard's Star"

# Extend with another list
more_stars = ["Vega", "Altair"]
stars.extend(more_stars)
# Or use: stars = stars + more_stars
```

### List Operations

```python
numbers = [1, 2, 3, 4, 5]

# Length
print(len(numbers))  # 5

# Check if element exists
print(3 in numbers)  # True
print(10 in numbers)  # False

# Count occurrences
data = [1, 2, 3, 2, 2, 4]
print(data.count(2))  # 3

# Find index of element
print(data.index(3))  # 2

# Sort (modifies original)
data.sort()
print(data)  # [1, 2, 2, 2, 3, 4]

# Sort (returns new list)
original = [3, 1, 4, 1, 5]
sorted_data = sorted(original)
print(original)      # [3, 1, 4, 1, 5] - unchanged
print(sorted_data)   # [1, 1, 3, 4, 5]

# Reverse
numbers.reverse()

# Clear all elements
numbers.clear()
```

### Iterating Over Lists

```python
tunes = ["Cooley's", "The Butterfly", "Banish Misfortune"]

# Method 1: Simple iteration
for tune in tunes:
    print(tune)

# Method 2: With index
for i in range(len(tunes)):
    print(f"{i}: {tunes[i]}")

# Method 3: Enumerate (best of both worlds)
for index, tune in enumerate(tunes):
    print(f"{index}: {tune}")

# Method 4: Start enumerate at 1
for number, tune in enumerate(tunes, start=1):
    print(f"#{number}: {tune}")
```

### List Comprehensions

A concise way to create lists:

```python
# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)

# List comprehension (Pythonic!)
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# With condition
even_squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Transform strings
tunes = ["Cooley's", "The Butterfly", "Banish Misfortune"]
upper_tunes = [tune.upper() for tune in tunes]
print(upper_tunes)  # ["COOLEY'S", "THE BUTTERFLY", "BANISH MISFORTUNE"]

# Extract from list of lists
coords = [[1, -0.9, 0], [1.5, 0.9, 0.4], [-0.6, -1.2, 2]]
x_values = [coord[0] for coord in coords]
print(x_values)  # [1, 1.5, -0.6]
```

---

## Part 2: Tuples

### What is a Tuple?

A **tuple** is an ordered collection like a list, but **immutable** - you cannot change it after creation.

```python
# Creating tuples
coordinates = (1.0, -0.9, 0.0)
star_info = ("Sirius", 2.6, "A0m")
single = (42,)  # Note the comma! Otherwise it's just a number

# Without parentheses (tuple packing)
point = 10, 20, 30
print(point)  # (10, 20, 30)

# Empty tuple
empty = ()
```

### Why Use Tuples?

1. **Performance** - Tuples are faster than lists
2. **Safety** - Cannot accidentally modify the data
3. **Dictionary keys** - Tuples can be dict keys, lists cannot
4. **Function returns** - Return multiple values from functions

```python
def get_star_info(name):
    """Return star data as tuple"""
    return ("Sirius", 2.6, "A0m", 1.46)

name, distance, spectral, magnitude = get_star_info("Sirius")
```

### Accessing Tuples

```python
coordinates = (1.0, -0.9, 0.0)

# Indexing (same as lists)
print(coordinates[0])   # 1.0
print(coordinates[-1])  # 0.0

# Slicing (same as lists)
print(coordinates[1:])  # (-0.9, 0.0)

# Unpacking
x, y, z = coordinates
print(f"x={x}, y={y}, z={z}")

# Partial unpacking with *
first, *rest = (1, 2, 3, 4, 5)
print(first)  # 1
print(rest)   # [2, 3, 4, 5]
```

### Tuple Operations

```python
coords = (1.0, -0.9, 0.0)

# Length
print(len(coords))  # 3

# Check membership
print(1.0 in coords)  # True

# Count and index
numbers = (1, 2, 3, 2, 2, 4)
print(numbers.count(2))  # 3
print(numbers.index(3))  # 2

# Concatenation (creates new tuple)
a = (1, 2)
b = (3, 4)
c = a + b
print(c)  # (1, 2, 3, 4)

# Repetition
repeated = (1, 2) * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)

# Cannot modify!
# coords[0] = 2.0  # TypeError: 'tuple' object does not support item assignment
```

### When to Use Lists vs Tuples

**Use Lists when:**
- Data will change (add, remove, modify)
- Order matters and you need to sort
- Working with homogeneous data (all same type)

**Use Tuples when:**
- Data shouldn't change (coordinates, RGB colors)
- Returning multiple values from functions
- Using as dictionary keys
- Slightly better performance matters

---

## Part 3: Dictionaries

### What is a Dictionary?

A **dictionary** stores **key-value pairs**. Like a real dictionary: you look up a word (key) to get its definition (value).

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

### Nested Dictionaries

```python
# Dictionary of dictionaries - like a database!
stars = {
    "Sirius": {
        "distance": 2.6,
        "spectral_class": "A0m",
        "coordinates": (1.8, -1.9, -0.4)
    },
    "Procyon": {
        "distance": 3.5,
        "spectral_class": "F5IV-V",
        "coordinates": (-2.8, -1.9, 0.8)
    }
}

# Access nested values
print(stars["Sirius"]["distance"])  # 2.6
print(stars["Procyon"]["coordinates"][0])  # -2.8

# Iterate over nested structure
for star_name, star_data in stars.items():
    print(f"\n{star_name}:")
    for key, value in star_data.items():
        print(f"  {key}: {value}")
```

### Dictionary Comprehensions

```python
# Create dictionary from lists
names = ["Sirius", "Procyon", "Vega"]
distances = [2.6, 3.5, 7.7]

star_distances = {name: dist for name, dist in zip(names, distances)}
print(star_distances)  # {'Sirius': 2.6, 'Procyon': 3.5, 'Vega': 7.7}

# Filter and transform
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_squares = {k: v**2 for k, v in numbers.items() if v % 2 == 0}
print(even_squares)  # {'b': 4, 'd': 16}

# Invert dictionary
star_distances = {'Sirius': 2.6, 'Procyon': 3.5}
distance_stars = {dist: name for name, dist in star_distances.items()}
print(distance_stars)  # {2.6: 'Sirius', 3.5: 'Procyon'}
```

---

## Part 4: Choosing the Right Data Structure

### Quick Reference

| Feature | List | Tuple | Dictionary |
|---------|------|-------|------------|
| **Ordered** | ✓ | ✓ | ✓ (Python 3.7+) |
| **Mutable** | ✓ | ✗ | ✓ |
| **Indexed by** | Integer | Integer | Any immutable type |
| **Duplicates** | ✓ | ✓ | Keys: ✗, Values: ✓ |
| **Use case** | Ordered collection | Immutable data | Key-value pairs |

### Real-World Examples

```python
# List: Collection of similar items that might change
tune_names = ["Cooley's", "The Butterfly", "Banish Misfortune"]
tune_names.append("Sirius")  # Can add more

# Tuple: Fixed data that shouldn't change
coordinates = (1.0, -0.9, 0.0)  # x, y, z coordinates
rgb_color = (255, 0, 0)  # Red color

# Dictionary: Named attributes/properties
star = {
    "name": "Sirius",
    "distance": 2.6,
    "coordinates": (1.8, -1.9, -0.4),  # Tuple inside dict!
    "nearby_stars": ["Procyon", "Sol"]  # List inside dict!
}
```

---

## Part 5: Practical Exercises

### Exercise 1: Lists

```python
# Given this list of tune downloads:
downloads = [4432, 2767, 4292, 812, 2850, 1567, 2262]

# Task 1: Find the average downloads
# Task 2: Find the most popular tune (highest downloads)
# Task 3: Count how many tunes have more than 2000 downloads
# Task 4: Create a new list with downloads doubled
# Task 5: Get the top 3 most downloaded tunes
```

**Solutions:**
```python
# Task 1: Average
average = sum(downloads) / len(downloads)
print(f"Average: {average:.2f}")

# Task 2: Most popular
most_popular = max(downloads)
print(f"Most popular: {most_popular}")

# Task 3: Count > 2000
count_popular = len([d for d in downloads if d > 2000])
print(f"Popular tunes: {count_popular}")

# Task 4: Double all
doubled = [d * 2 for d in downloads]
print(doubled)

# Task 5: Top 3
top_3 = sorted(downloads, reverse=True)[:3]
print(f"Top 3: {top_3}")
```

### Exercise 2: Tuples and Unpacking

```python
# Star data as tuples: (name, distance, spectral_class)
stars = [
    ("Sol", 0, "G2V"),
    ("Rigel Kentaurus B", 1.3, "K1V"),
    ("Barnard's Star", 1.8, "sdM4"),
    ("Sirius", 2.6, "A0m")
]

# Task 1: Print each star's name and distance
# Task 2: Find the closest star (excluding Sol)
# Task 3: Create a list of just the star names
# Task 4: Count how many M-class stars there are
```

**Solutions:**
```python
# Task 1: Print name and distance
for name, distance, _ in stars:  # _ ignores spectral class
    print(f"{name} is {distance} parsecs away")

# Task 2: Closest star (excluding Sol)
closest = min([s for s in stars if s[1] > 0], key=lambda s: s[1])
print(f"Closest: {closest[0]}")

# Task 3: Just names
names = [star[0] for star in stars]
print(names)

# Task 4: Count M-class
m_count = len([s for s in stars if 'M' in s[2]])
print(f"M-class stars: {m_count}")
```

### Exercise 3: Dictionaries

```python
# Create a tune database
tunes = {
    "Cooley's": {"type": "reel", "key": "Emin", "downloads": 4432},
    "The Butterfly": {"type": "slip jig", "key": "Emin", "downloads": 2767},
    "Banish Misfortune": {"type": "jig", "key": "Dmix", "downloads": 4292}
}

# Task 1: Print all tune names
# Task 2: Find the total downloads across all tunes
# Task 3: Find all tunes in E minor
# Task 4: Find the most popular tune
# Task 5: Add a new tune
```

**Solutions:**
```python
# Task 1: All names
for tune_name in tunes:
    print(tune_name)

# Task 2: Total downloads
total = sum(tune["downloads"] for tune in tunes.values())
print(f"Total downloads: {total}")

# Task 3: E minor tunes
emin_tunes = [name for name, data in tunes.items() if data["key"] == "Emin"]
print(f"E minor tunes: {emin_tunes}")

# Task 4: Most popular
most_popular = max(tunes.items(), key=lambda x: x[1]["downloads"])
print(f"Most popular: {most_popular[0]} with {most_popular[1]['downloads']} downloads")

# Task 5: Add new tune
tunes["Sirius"] = {"type": "reel", "key": "Dmaj", "downloads": 1500}
```

### Exercise 4: Combined

```python
# Parse this CSV-like data into a list of dictionaries
csv_data = """name,distance,spectral_class
Sol,0,G2V
Sirius,2.6,A0m
Procyon,3.5,F5IV-V"""

# Task: Convert to list of dictionaries
# Expected output:
# [
#     {"name": "Sol", "distance": 0.0, "spectral_class": "G2V"},
#     {"name": "Sirius", "distance": 2.6, "spectral_class": "A0m"},
#     {"name": "Procyon", "distance": 3.5, "spectral_class": "F5IV-V"}
# ]
```

**Solution:**
```python
lines = csv_data.strip().split('\n')
headers = lines[0].split(',')

stars = []
for line in lines[1:]:
    values = line.split(',')
    star = {}
    for i, header in enumerate(headers):
        value = values[i]
        # Convert distance to float
        if header == "distance":
            value = float(value)
        star[header] = value
    stars.append(star)

print(stars)

# Or with dictionary comprehension:
stars = [
    {
        headers[i]: (float(val) if headers[i] == "distance" else val)
        for i, val in enumerate(line.split(','))
    }
    for line in lines[1:]
]
```

---

## Part 6: Connection to Pandas

Now you understand why pandas is so powerful!

```python
import pandas as pd

# Pandas uses these concepts:
# - Each column is like a LIST
# - Each row is like a DICTIONARY
# - DataFrame is like a LIST OF DICTIONARIES

# From list of dictionaries (what we just learned!)
stars_list = [
    {"name": "Sol", "distance": 0, "spectral_class": "G2V"},
    {"name": "Sirius", "distance": 2.6, "spectral_class": "A0m"},
    {"name": "Procyon", "distance": 3.5, "spectral_class": "F5IV-V"}
]

df = pd.DataFrame(stars_list)
print(df)

# Access column (returns a list-like Series)
print(df['name'])

# Access row (returns a dictionary-like Series)
print(df.iloc[0])

# Iterate over rows (returns dictionary-like objects)
for index, row in df.iterrows():
    print(f"{row['name']}: {row['distance']} parsecs")
```

Understanding lists, tuples, and dictionaries makes pandas much easier to learn!

---

## Summary

**Lists:**
- Ordered, mutable collections
- Access by index: `my_list[0]`
- Modify: `append()`, `insert()`, `remove()`

**Tuples:**
- Ordered, immutable collections
- Access by index: `my_tuple[0]`
- Cannot modify after creation
- Use for fixed data

**Dictionaries:**
- Key-value pairs
- Access by key: `my_dict["key"]`
- Modify: `my_dict["key"] = value`
- Fast lookups

**Remember:**
- Use **lists** for ordered data that changes
- Use **tuples** for fixed coordinates or multiple return values
- Use **dictionaries** for named attributes and lookups

These are the foundation of all Python data manipulation!