import paho.mqtt.client as mqtt
from datetime import datetime
import json

MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEP_ALIVE = 300 # sends a message to the server every interval (300)

MQTT_CLIENT_NAME = "user-role-manager"
MQTT_TOPIC = "cars"

# MQTT client

# Create client and connect client to host
client = mqtt.Client(MQTT_CLIENT_NAME)
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

# Subscibe client to topic
client.subscribe(MQTT_TOPIC)

def on_message_callback(client, user_data, message):
    msg = message
    msg_data = str(msg.payload.decode("UTF-8"))
    data = json.loads(msg_data)

    output = f"at {data['datetime']} it was {data['temp']} at location {data['client']}"
    print(f"{output}")
    print(f"Topic: {msg.topic} QoS: {msg.qos} Retain:{msg.retain}")

# Listen for messages
client.on_message = on_message_callback

print(f"{MQTT_CLIENT_NAME} is listening on port {MQTT_PORT} for {MQTT_TOPIC}")

client.loop_forever()