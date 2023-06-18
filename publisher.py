import paho.mqtt.client as mqtt
import time
from random import uniform
import json
from datetime import datetime

MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEP_ALIVE = 300 # sends a message to the server every interval (300)

MQTT_CLIENT_NAME = "carpark-off"
MQTT_TOPIC = "cars"

# MQTT client

# Create client and connect client to host
client = mqtt.Client(MQTT_CLIENT_NAME)
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

print(f"Sending message to MQTT broker {MQTT_HOST} on port {MQTT_PORT}.")
print(f"with the topic {MQTT_TOPIC}.")

message_to_send = "Hello..."

while True:
    time.sleep(5)
    temperature = round(uniform (20, 25),1)
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ+0800")
    message_data = {
        "client": MQTT_CLIENT_NAME,
        "temp" : temperature,
        "datetime": now
    }
    # Convert dictionary to JSON format
    message_to_send = json.dumps(message_data)

    print(f"Temperature is {round(temperature,1)} at {now}")
    client.publish(MQTT_TOPIC, message_to_send)

