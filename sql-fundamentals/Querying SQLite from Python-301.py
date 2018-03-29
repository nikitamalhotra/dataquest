## 3. Connecting to the Database ##

import sqlite3
conn = sqlite3.connect('jobs.db')

## 6. Creating a Cursor and Running a Query ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = "select * from recent_grads;"
cursor.execute(query)
results = cursor.fetchall()
print(results[0:2])

query = "select major from recent_grads"
cursor.execute(query)
majors = cursor.fetchall()
print(majors[:3])

## 8. Fetching a Specific Number of Results ##

import sqlite3
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

query = 'select Major, Major_category from recent_grads'
five_results = cursor.execute(query).fetchmany(5)

## 9. Closing the Database Connection ##

conn = sqlite3.connect("jobs.db")
conn.close()

## 10. Practice ##

conn = sqlite3.connect("jobs2.db")
cursor = conn.cursor()
query = "SELECT Major FROM recent_grads ORDER BY Major DESC"
reverse_alphabetical = cursor.execute(query).fetchall()
conn.close()