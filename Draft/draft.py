import requests

tele_auth_token = "5281854155:AAHo72aMgsPxcfAtHQM1dnCAgqzFHvisSjo"
tel_group_id = "my_group702"

msg = "Messege received from chatbot"

def send_message(msg):
    telegram_api_url = f"https://api.telegram.org/bot{tele_auth_token}/sendMessage?chat_id=@{tel_group_id}&text={msg}"
    tel_resp = requests.get(telegram_api_url)
    if tel_resp.status_code == 200:
        print("Notification sent to telegram..")
    else:
        print("Could`nt send message!!")
for i in range(5):
    send_message(f"message number{i+1} :{msg}")