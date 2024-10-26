# database.py
import sqlite3
from settings import DB_PATH

def create_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def initialize_db():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS daily_weather (
                        id INTEGER PRIMARY KEY,
                        city TEXT,
                        date TEXT,
                        avg_temp REAL,
                        max_temp REAL,
                        min_temp REAL,
                        dominant_condition TEXT
                    )''')
    conn.commit()
    conn.close()

def insert_summary(summary):
    initialize_db()
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO daily_weather (city, date, avg_temp, max_temp, min_temp, dominant_condition)
                      VALUES (?, ?, ?, ?, ?, ?)''',
                   (summary['city'], summary['date'], summary['average_temp'], 
                    summary['max_temp'], summary['min_temp'], summary['dominant_condition']))
    conn.commit()
    conn.close()

