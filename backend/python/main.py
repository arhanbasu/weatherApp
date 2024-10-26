# main.py
from schedule_tasks import job
import schedule
import time

if __name__ == '__main__':
    schedule.every(1).minutes.do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

