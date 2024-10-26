# schedule_tasks.py
import schedule
import time
#from jobs.fetch_weather import fetch_all_cities_weather
from fetch_weather import fetch_all_cities_weather
from data_processing import update_daily_summary
from alerting import check_alert_conditions
from database import insert_summary


def job():
    weather_data_list = fetch_all_cities_weather()
    daily_data = []
    
    for weather_data in weather_data_list:
        #print(weather_data)
        summary = update_daily_summary(weather_data, daily_data)
        insert_summary(summary)
        alert_triggered = False
        check_alert_conditions(weather_data, alert_triggered)

#schedule.every(1).minutes.do(job)

#while True:
#    schedule.run_pending()
#    time.sleep(1)

