#!/usr/bin/env python
# coding: utf-8

# # Midterm Question - 22

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# This table contains information about the temperature on a certain day.
# 
# Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
# 
# Return the result table in any order.

# In[18]:


import sqlite3

def add_database():
    conn = sqlite3.connect('weather.db')
    cur = conn.cursor()
    
    # Create table
    cur.execute('''
              CREATE TABLE IF NOT EXISTS Weather (
                  id INTEGER PRIMARY KEY,
                  recordDate DATE,
                  temperature INTEGER
              )
              ''')
    
    # Insert into Weather table
    dataofweather = [
        (1, '2015-01-01', 10),
        (2, '2015-01-02', 25),
        (3, '2015-01-03', 20),
        (4, '2015-01-04', 30)
    ]
    
    cur.executemany('INSERT INTO Weather (id, recordDate, temperature) VALUES (?, ?, ?)', dataofweather)
    
    conn.commit()
    conn.close()

# Execute SQL query 
def temp_dates():
    
    conn = sqlite3.connect('weather.db')
    conn.execute('BEGIN')
    
    try:
        sql_query = '''
                SELECT w1.id
                FROM Weather w1
                WHERE w1.temperature > (
                    SELECT w2.temperature
                    FROM Weather w2
                    WHERE DATE(w2.recordDate, '-1 day') = w1.recordDate
                )
                ORDER BY w1.id
                '''
        result = conn.execute(sql_query).fetchall()
        conn.commit()
        return result
    
    finally:
        conn.close()
        
add_database()

result = temp_dates()

print("IDs with higher temperatures compared to previous days: ")
for row in result:
    print(row[0])

