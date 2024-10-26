# plot_visuals.py
'''import matplotlib.pyplot as plt
import pandas as pd
from database import create_connection

def plot_weather_trends():
    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM daily_weather", conn)
    df['date'] = pd.to_datetime(df['date'])
    
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['avg_temp'], label='Average Temp')
    plt.plot(df['date'], df['max_temp'], label='Max Temp')
    plt.plot(df['date'], df['min_temp'], label='Min Temp')
    plt.legend()
    plt.title('Weather Trends')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.show()'''
    
# plot_visuals.py
import matplotlib.pyplot as plt
import pandas as pd
from database import create_connection

def plot_weather_trends():
    conn = create_connection()
    df = pd.read_sql_query("SELECT * FROM daily_weather", conn)
    conn.close()  # Make sure to close the connection

    # Print the DataFrame to check if data exists
    print(df)

    if df.empty:
        print("No data available to plot.")
        return

    df['date'] = pd.to_datetime(df['date'])

    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['avg_temp'], label='Average Temp')
    plt.plot(df['date'], df['max_temp'], label='Max Temp')
    plt.plot(df['date'], df['min_temp'], label='Min Temp')
    plt.legend()
    plt.title('Weather Trends')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.show()

if __name__ == "__main__":
    plot_weather_trends()
    plt.savefig('./python/plot.png')


