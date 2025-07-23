from sensors.dht_sensor import get_temp_humidity
from sensors.ultrasonic_sensor import get_distance
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import time

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials/credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("SmartJalRakshak_Data").sheet1

# Infinite loop to collect and log data
while True:
    try:
        temp, humidity = get_temp_humidity()
        distance = get_distance()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data = [timestamp, distance, temp, humidity]
        sheet.append_row(data)
        print("Data logged:", data)

        time.sleep(60)  # log every 60 seconds
    except Exception as e:
        print("Error:", e)
        time.sleep(10)
