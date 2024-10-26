# alerting.py
from settings import TEMP_THRESHOLD

def check_alert_conditions(weather_data, alert_triggered):
    temp_celsius = weather_data['temp'] #- 273.15
    
    if temp_celsius > TEMP_THRESHOLD:
        if not alert_triggered:
            print(f"ALERT: Temperature exceeds {TEMP_THRESHOLD}°C in {weather_data['city']}")
            return True
    return False

