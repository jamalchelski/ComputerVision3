import os
from dotenv import load_dotenv
from Adafruit_IO import Client, Feed, RequestError
import time

load_dotenv()

ADAFRUIT_IO_USERNAME = os.getenv("user_Name")

ADAFRUIT_IO_KEY = os.getenv("active_Key")

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try:
    payload = aio.feeds('temp')
except RequestError:
    feed = Feed(name="temp")
    payload = aio.create_feed(feed)

# Adding data
# aio.send_data(temperature.key, 0)

while True:
    data = aio.receive(payload.key).value
    Data = int(data)
    if Data == 1:
        print('Lampu On')
    else:
        print('Lampu Off')
    time.sleep(1)
