# data_processing.py
import pandas as pd

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def update_daily_summary(weather_data, daily_data):
    daily_data.append(weather_data)
    
    df = pd.DataFrame(daily_data)
    avg_temp = df['temp'].mean()
    max_temp = df['temp'].max()
    min_temp = df['temp'].min()
    dominant_condition = df['main'].mode()[0]
    
    summary = {
        'city': weather_data['city'],
        'date': pd.to_datetime('today').date(),
        'average_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition
    }
    return summary

