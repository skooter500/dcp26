---
marp: true
theme: default
paginate: true
style: |
  section {
    font-size: 26px;
  }
  pre {
    font-size: 22px;
  }
  table {
    font-size: 22px;
  }
---

# SQL Databases in Python

SQLite, PostgreSQL and MySQL

---

# Why use a database?

A CSV file is fine for one table that one person reads. A database is better when you have:

- Several tables that link together
- Too much data to load all at once
- Lots of people or programs using the data at the same time
- Changes that must never be half done

You ask a database questions in **SQL** (Structured Query Language)

---

# Tables, rows and columns

A database holds **tables**. A table is like a DataFrame:

| id | thesession.org_id | title | artist |
|----|-------------------|-------|--------|
| 1 | 1 | The Lonesome Touch | Martin Hayes |
| 2 | 2 | Under The Moon | Martin Hayes |
| 3 | 3 | Otherworld | Lunasa |

Every column has a name and a type (`integer`, `varchar`, ...)

The **primary key** (`id`) is different for every row, so it picks out exactly one row

---

# Three databases

|  | SQLite | PostgreSQL | MySQL |
|--|--------|------------|-------|
| Data lives in | One file | A server | A server |
| Python module | `sqlite3` | `psycopg` | `mysql.connector` |
| Install | Nothing, it comes with Python | `pip install "psycopg[binary]"` | `pip install mysql-connector-python` |
| Placeholder | `?` | `%s` | `%s` |
| Used for | Apps, phones, learning | Big multi-user systems | Websites |

The SQL is almost the same in all three, and so is the Python

---

# The pattern

Every database works the same way in Python:

1. **Connect** to the database
2. Get a **cursor**
3. **Execute** some SQL
4. **Fetch** the results
5. **Commit** if you changed anything, then **close**

Learn it once with SQLite and it works for PostgreSQL and MySQL too

---

# Our database: data/tunepal.db

The database behind Tunepal. We'll use these tables:

| Table | Rows | What's in it |
|-------|------|--------------|
| `tuneindex` | 66,962 | Tunes: `title`, `tune_type`, `key_sig`, `time_sig`, `source` |
| `source` | 35 | Where the tunes came from: `id`, `shortName` |
| `album` | 3,944 | Albums: `id`, `title`, `artist` |
| `albumtracktune` | 102,023 | Tunes on each album: `album_id`, `track_num`, `title` |

`tuneindex.source` is the `id` of a row in `source`

`albumtracktune.album_id` is the `id` of a row in `album`

---

# Connecting to SQLite

```python
import sqlite3

conn = sqlite3.connect("data/tunepal.db")
cursor = conn.cursor()

cursor.execute("SELECT id, title, artist FROM album LIMIT 5")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()
```

```
(1, 'The Lonesome Touch', 'Martin Hayes')
(2, 'Under The Moon', 'Martin Hayes')
(3, 'Otherworld', 'Lunasa')
(4, 'Blackwater', 'Altan')
(5, 'Live In Concert', 'The Bothy Band')
```

Each row is a **tuple**: `row[0]` is the id, `row[1]` is the title

---

# "no such table"

```
sqlite3.OperationalError: no such table: album
```

If `connect` can't find the file, it **makes a new empty database** instead of giving an error. Then the first query fails because the new database has no tables

Check that your terminal is in the root of the repo (the folder with `data` in it). Delete the empty `tunepal.db` it made in the wrong folder

---

# Fixing text errors

Ask for every album and you get this:

```
sqlite3.OperationalError: Could not decode to UTF-8 column 'artist'
with text 'Kevin Burke And M�che�l O'Domhnaill'
```

Some names were saved in an old Windows encoding. Tell `sqlite3` how to read them:

```python
def decode(b):
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("cp1252")    # the old Windows encoding

conn = sqlite3.connect("data/tunepal.db")
conn.text_factory = decode
```

Now you get `Mícheál`. `b.decode(errors="ignore")` also stops the error, but it throws away the letters with fadas: `Mchel`

---

# What's in the database?

```python
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
print(cursor.fetchall())

cursor.execute("PRAGMA table_info(album)")
for column in cursor.fetchall():
    print(column[1], column[2])        # the name and the type
```

```
id INTEGER
thesession.org_id INTEGER
title varchar(255)
artist varchar(255)
```

These two only work in SQLite. You can also open the file in **DB Browser for SQLite** (sqlitebrowser.org) and look around

---

# SELECT

```sql
SELECT * FROM album                  -- every column
SELECT title, artist FROM album      -- only these columns
```

- SQL keywords are written in CAPITALS by convention, but SQL doesn't mind
- Text goes in **single quotes**: `'Altan'`
- `--` starts a comment

In Python, the SQL is just a string:

```python
cursor.execute("SELECT title, artist FROM album")
```

---

# WHERE

```sql
SELECT title FROM album WHERE artist = 'Martin Hayes'
```

```
('The Lonesome Touch',)
('Under The Moon',)
('Live In Seattle',)
('Martin Hayes',)
```

```sql
SELECT title FROM tuneindex WHERE tune_type = 'reel' AND key_sig = 'Dmaj'
SELECT COUNT(*) FROM tuneindex WHERE tune_type IN ('jig', 'slip jig')
SELECT COUNT(*) FROM tuneindex WHERE tune_type IS NULL
```

`=` `<>` `<` `>` `<=` `>=` `AND` `OR` `NOT` `IN` `IS NULL`

SQL uses one `=`, not `==`. A missing value is `NULL`, and Python gives you `None`

---

# LIKE

`%` matches any text, `_` matches one character

```sql
SELECT title FROM tuneindex WHERE title LIKE '%kesh%'
```

```
('HUMORS OF KESH (jig)',)
('Kesh, The',)
('HILLS OF KESH (reel)',)
("Sean Coghlan's Kesh",)
('Kesh Jig, The',)
...
```

56 tunes. In SQLite and MySQL, `LIKE` ignores capitals. In PostgreSQL it doesn't, so use `ILIKE` there

---

# ORDER BY and LIMIT

```sql
SELECT title FROM album WHERE artist = 'Altan' ORDER BY title LIMIT 5
```

```
('25th Anniversary Celebration',)
('Altan',)
("Altan's Finest",)
('Altan: Live',)
('Another Sky',)
```

`ORDER BY title DESC` sorts the other way

`LIMIT 5` keeps the first 5 rows. Use it while you're testing a query on a big table

---

# Counting and grouping

```python
cursor.execute("SELECT COUNT(*) FROM tuneindex")
print(cursor.fetchone()[0])            # 66962
```

`COUNT` `SUM` `AVG` `MIN` `MAX` work on a whole column

`GROUP BY` works them out for each group, like `groupby` in pandas:

```sql
SELECT tune_type, COUNT(*) AS tunes
FROM tuneindex
GROUP BY tune_type
ORDER BY tunes DESC
LIMIT 5
```

```
('reel', 22461)
('jig', 15323)
('polka', 4628)
('hornpipe', 4311)
(None, 4132)
```

`AS tunes` gives the count a name, so you can sort by it

---

# JOIN

`tuneindex.source` is just a number. The name is in the `source` table. `JOIN` matches the rows up:

```sql
SELECT source.shortName, COUNT(*) AS tunes
FROM tuneindex
JOIN source ON tuneindex.source = source.id
GROUP BY source.shortName
ORDER BY tunes DESC
LIMIT 5
```

```
('thesession.org', 54717)
('Norbeck', 1940)
("Aird's Airs", 1180)
('Nigel Gatherer', 1053)
('Nottingham', 1037)
```

Write `table.column` when both tables have a column with the same name

---

# JOIN: the tunes on an album

```sql
SELECT albumtracktune.track_num, albumtracktune.title
FROM albumtracktune
JOIN album ON albumtracktune.album_id = album.id
WHERE album.title = 'The Lonesome Touch'
ORDER BY albumtracktune.track_num
```

```
(1, "Paddy Fahy's")
(2, 'The Kerfunken')
(3, "Paul Ha'penny")
(3, 'The Garden Of Butterflies')
(3, 'The Broken Pledge')
...
```

Why is track 3 there three times? A track is often a **set** of tunes played one after another

---

# Getting the results

```python
cursor.execute("SELECT title FROM album WHERE artist = 'Altan'")

cursor.fetchone()       # the next row:  ('Blackwater',)
cursor.fetchmany(2)     # the next 2:    [('Island Angel',), ('Harvest Storm',)]
cursor.fetchall()       # all the rows that are left
```

You can also loop over the cursor, one row at a time:

```python
for row in cursor.execute("SELECT title FROM album WHERE artist = 'Lunasa'"):
    print(row[0])
```

A row with one column is still a tuple: `('Blackwater',)`. Use `row[0]` to get the value out

---

# Rows by name

`row[1]` is hard to read. Ask for rows you can use like dictionaries:

```python
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("SELECT id, title, artist FROM album LIMIT 2")
for row in cursor.fetchall():
    print(row["title"], "by", row["artist"])
```

```
The Lonesome Touch by Martin Hayes
Under The Moon by Martin Hayes
```

---

# Never build SQL with an f-string

```python
artist = input("Artist: ")
cursor.execute(f"SELECT title FROM album WHERE artist = '{artist}'")   # NO!
```

Type `Kevin Burke And Mícheál O'Domhnaill`:

```
sqlite3.OperationalError: near "Domhnaill": syntax error
```

The `'` in the name ends the SQL string early. Lots of Irish names have one

Type `' OR '1'='1` and you get **all 3,944 albums**. The user has rewritten your SQL. This is called **SQL injection**, and it's one of the most common ways websites get hacked

---

# Use placeholders

Put a `?` where the value goes and pass the values in a tuple:

```python
artist = input("Artist: ")
cursor.execute("SELECT title FROM album WHERE artist = ?", (artist,))
```

The database puts the value in safely, so `O'Domhnaill` works and `' OR '1'='1` finds nothing

- `(artist,)` needs the comma. `("Altan")` is just a string, and you get `Incorrect number of bindings supplied`
- Put the `%` for `LIKE` in the value: `("%" + word + "%",)`
- Placeholders are for values only, not table or column names

---

# Changing data

Practise on **your own** database, not `tunepal.db`:

```python
conn = sqlite3.connect("data/my_tunes.db")    # made if it isn't there
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS practice (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    minutes INTEGER
)""")

cursor.execute("INSERT INTO practice (title, minutes) VALUES (?, ?)", ("The Kesh", 20))

sessions = [("Drowsy Maggie", 15), ("Out On The Ocean", 30), ("Cooley's", 45)]
cursor.executemany("INSERT INTO practice (title, minutes) VALUES (?, ?)", sessions)

conn.commit()
```

`INTEGER PRIMARY KEY` fills in the `id` for you. `cursor.lastrowid` tells you what it was

---

# UPDATE and DELETE

```python
cursor.execute("UPDATE practice SET minutes = ? WHERE title = ?", (25, "The Kesh"))
cursor.execute("DELETE FROM practice WHERE minutes < ?", (20,))
print(cursor.rowcount)        # how many rows were changed
conn.commit()
```

**Don't forget the `WHERE`.** `DELETE FROM practice` deletes every row

---

# Commit

Changes are only saved when you **commit**. Close without committing and they're gone

```python
conn.commit()
```

Or use `with`. It commits at the end of the block, or undoes everything if there's an error:

```python
with conn:
    conn.execute("INSERT INTO practice (title, minutes) VALUES (?, ?)", ("Banish Misfortune", 10))
```

This is what makes a database safe: a change is either all done or not done at all

---

# PostgreSQL

A database **server**. You need the server running (from postgresql.org, or online) and:

```
pip install "psycopg[binary]"
```

```python
import psycopg

conn = psycopg.connect(host="localhost", dbname="tunepal",
                       user="student", password=password)
cursor = conn.cursor()

cursor.execute("SELECT title FROM album WHERE artist = %s", (artist,))
for row in cursor.fetchall():
    print(row[0])

conn.close()
```

The same pattern. The placeholder is `%s` (it isn't Python's `%` formatting, so don't add quotes)

---

# PostgreSQL: what's different

- `LIKE` cares about capitals. Use `ILIKE` to ignore them
- Names are changed to lower case unless you quote them. `source.shortName` gives `column source.shortname does not exist`, so write `source."shortName"`
- List the tables with:
  ```sql
  SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'
  ```
- `with psycopg.connect(...) as conn:` commits **and closes** at the end
- Rows as dictionaries: `conn.cursor(row_factory=psycopg.rows.dict_row)`
- Older code uses `psycopg2`. It works the same way

---

# MySQL

Also a server (from mysql.com, or MariaDB which works the same). Then:

```
pip install mysql-connector-python
```

```python
import mysql.connector

conn = mysql.connector.connect(host="localhost", database="tunepal",
                               user="student", password=password)
cursor = conn.cursor()

cursor.execute("SELECT title FROM album WHERE artist = %s", (artist,))
for row in cursor.fetchall():
    print(row[0])

conn.close()
```

---

# MySQL: what's different

- The placeholder is `%s`
- `SHOW TABLES` and `DESCRIBE album` show you what's there
- Quote odd names with backticks: `` `thesession.org_id` ``
- Changes need `conn.commit()`
- Rows as dictionaries: `conn.cursor(dictionary=True)`
- Fetch all the rows of one query before you run the next, or you get `Unread result found`

---

# Keep passwords out of your code

Code goes on GitHub. Passwords shouldn't

```python
import os
password = os.environ["DB_PASSWORD"]      # set it in the terminal first
```

```python
from getpass import getpass
password = getpass("Database password: ")  # asks without showing it
```

---

# Same code, three databases

|  | SQLite | PostgreSQL | MySQL |
|--|--------|------------|-------|
| Import | `import sqlite3` | `import psycopg` | `import mysql.connector` |
| Connect | `sqlite3.connect` | `psycopg.connect` | `mysql.connector.connect` |
| Connect needs | The file name | `host`, `dbname`, `user`, `password` | `host`, `database`, `user`, `password` |
| Placeholder | `?` | `%s` | `%s` |
| List tables | `sqlite_master` | `information_schema.tables` | `SHOW TABLES` |
| Ignore capitals | `LIKE` | `ILIKE` | `LIKE` |
| Odd names | `"name"` | `"name"` | `` `name` `` |

Everything else (cursor, execute, fetch, commit, close) is the same

---

# Pandas: read_sql_query

Run a query and get a DataFrame back:

```python
import sqlite3
import pandas as pd

conn = sqlite3.connect("data/tunepal.db")
conn.text_factory = decode

df = pd.read_sql_query("SELECT title, tune_type, key_sig FROM tuneindex", conn)
print(df.head())
conn.close()
```

```
                         title   tune_type key_sig
0             Condon's frolics  Double jig    Ador
1                The idle road  Double jig       G
2                 Billy Barlow  Double jig       A
```

Use placeholders with `params`:

```python
albums = pd.read_sql_query("SELECT title FROM album WHERE artist = ?",
                           conn, params=("Altan",))
```

---

# SQL or pandas?

The same question two ways:

```python
pd.read_sql_query("""SELECT tune_type, COUNT(*) AS tunes FROM tuneindex
                     GROUP BY tune_type ORDER BY tunes DESC""", conn)
```

```python
df = pd.read_sql_query("SELECT tune_type FROM tuneindex", conn)
df["tune_type"].value_counts()
```

Let the **database** pick out and join the rows (`WHERE`, `JOIN`), so you only bring back what you need

Use **pandas** for the analysis and the graphs

---

# A graph from a query

```python
import matplotlib.pyplot as plt

sql = """SELECT title, COUNT(*) AS recordings
         FROM albumtracktune
         GROUP BY title
         ORDER BY recordings DESC
         LIMIT 10"""
top = pd.read_sql_query(sql, conn)

plt.bar(top["title"], top["recordings"])
plt.ylabel("Number of recordings")
plt.title("Most recorded tunes")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
```

The winner, with 640, is *Gan Ainm*. It's Irish for "no name". Look for *Paddy Fahy's* and *Paddy Fahey's* too: the same tune, spelled two ways

---

# Writing a DataFrame to a database

`to_sql` makes a table from a DataFrame:

```python
exams = pd.read_csv("data/exams.csv")

conn = sqlite3.connect("data/my_tunes.db")
exams.to_sql("exams", conn, if_exists="replace", index=False)

print(pd.read_sql_query(
    "SELECT last, first, exam FROM exams WHERE exam >= 95 ORDER BY exam DESC", conn))
```

```
      last first   exam
0    Quinn  Luke  100.0
1  Buckley   Mei  100.0
2  OConnor  Kofi   95.0
```

`if_exists` can be `"fail"`, `"replace"` or `"append"`

---

# Pandas with PostgreSQL and MySQL

Pandas only takes a plain connection for SQLite. For the others, give it an **engine** from SQLAlchemy:

```
pip install sqlalchemy
```

```python
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg://student:password@localhost/tunepal")
engine = create_engine("mysql+mysqlconnector://student:password@localhost/tunepal")

df = pd.read_sql_query("SELECT title FROM album WHERE artist = %s",
                       engine, params=("Altan",))
```

The address is `type+driver://user:password@host/database`

Pass a plain `psycopg` connection and pandas warns you: `pandas only supports SQLAlchemy connectable...`

---

# Common errors

| Error | What it means |
|-------|---------------|
| `no such table: album` | Wrong folder, so `connect` made a new empty database |
| `Could not decode to UTF-8` | Set `conn.text_factory` |
| `near "...": syntax error` | A mistake in your SQL. Print it and read it |
| `Incorrect number of bindings` | You forgot the comma: `(artist,)` |
| `database is locked` | Another program (e.g. DB Browser) has changes it hasn't saved |
| My changes disappeared | You forgot `conn.commit()` |

---

# Key takeaways

Connect → cursor → execute → fetch → commit → close

`SELECT` `WHERE` `LIKE` `ORDER BY` `LIMIT` `COUNT` `GROUP BY` `JOIN`

**Always** use placeholders (`?` or `%s`) for values. Never f-strings

SQLite is a file. PostgreSQL and MySQL are servers, but the Python is the same

`pd.read_sql_query(sql, conn)` gives you a DataFrame, ready to graph
