import requests
from datetime import datetime
import pytz
import time

IST = pytz.timezone('Asia/Kolkata')           # Indian Standard Time - Timezone
raw_TS = datetime.now(IST)      # Tomorrows date
curr_date = raw_TS.strftime("%d-%m-%Y") #Current Date
curr_time = raw_TS.strftime("%H:%M:%S")   #Current time

tele_auth_token = "5242515715:AAH8PjSoQyyoHNRoGOeVo3AvQ1eTo6xhTGU" # Authentication token provided by Telegram bot
tel_group_id = "freq_send"     # Telegram group name

msg = f"Messege received on {curr_date} at {curr_time}"

def send_msg_on_telegram(msg):
     telegram_api_url = f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id=@{tel_group_id}&text={msg}"
     tel_resp = requests.get(telegram_api_url)
     if tel_resp.status_code == 200:
     	print ("Notification has been sent on Telegram") 
     else:
     	print ("Could not send Message")
while True:
    send_msg_on_telegram(msg)
    time.sleep(30)  # Sleep for 3 seconds