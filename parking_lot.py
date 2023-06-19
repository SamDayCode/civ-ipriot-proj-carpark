import paho.mqtt.client as paho
import json
from paho.mqtt.client import MQTTMessage

"""toml

[config]
location = "Moondalup City Square Parking"
total_spaces = 192
broker_host = "localhost"
broker_port = 1883
"""


BROKER, PORT = "localhost", 1883
MQTT_topic_subscribe = "sensor/car_in_out"
MQTT_topic_publish = "display/entry"

def on_message(client, user_data, message):
    msg = message
    msg_data = str(msg.payload.decode("UTF-8"))
    data = json.loads(msg_data)

    output = f"There are currently {data['cars']} cars in the parking lot, with currently {data['spaces']}"
    print(f"{output} parking spaces available.")



client = paho.Client()
client.on_message = on_message

client.connect(BROKER, PORT)
client.subscribe(MQTT_topic_subscribe)



client.loop_forever()