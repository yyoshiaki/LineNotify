import schedule
import time

from main import *
 
    
schedule.every().day.at("9:00").do(main)

while 1:
    schedule.run_pending()
    time.sleep(1)