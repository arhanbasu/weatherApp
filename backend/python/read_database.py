import sqlite3
import pandas as pd

def read_database():
    conn = sqlite3.connect('storage.db')
    df = pd.read_sql_query("SELECT * FROM daily_weather", conn)
    conn.close()
    return df.to_json(orient='records')

if __name__ == "__main__":
    data = read_database()
    print(data)

