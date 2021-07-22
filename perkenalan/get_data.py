import sys
import time
from Adafruit_IO import MQTTClient

uname = 'CHC_APO'
keyPass = 'aio_Djmk90BXrp4UCwNXgZJpygsPvkXv'
feedName = 'temp'

def connected (client):
    print('Conected to Adafruit IO ! Listening for {0} changes ..'.format(feedName))
    print('Waiting for data ...',client.subscribe(feedName))

def subscribe (client, userdata, mid, grandted_qos):
    print('Subscribe to{0} with Qos{1}'.format(feedName, grandted_qos))

def disconected (client):
    print('Disconected from IO')
    sys.exit(1)

def message(client,feed_name,payload ):
    print ('Feed{0} received new value: {1}'.format(feed_name,payload))


# methode
client = MQTTClient(uname,keyPass)

while True:
    client.on_connect = connected(client)
    time.sleep(2)
# client.on_disconnect = disconected(client)
# client.on_message = message(client)
# client.on_subscribe = subscribe(client)

# client.connect(client)
# client.loop_blocking(client)