import sqlite3

conn = sqlite3.connect('data/tunepal.db')
# Source - https://stackoverflow.com/a/58891189
# Posted by Adam Dingle
# Retrieved 2026-11-20, License - CC BY-SA 4.0

conn.text_factory = lambda b: b.decode(errors = 'ignore')
cursor = conn.cursor()

cursor.execute('SELECT * FROM album')

    # Get all results
results = cursor.fetchall()

# Print results
for row in results:
    print(row)    
    print(row[0])
    print(row[1])
# Close

