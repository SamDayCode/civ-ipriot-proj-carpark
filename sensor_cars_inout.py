# from sense_hat import SenseHat
from backups.no_pi_bak import CarDetector

"""MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEP_ALIVE = 300 # sends a message to the server every interval (300)

MQTT_CLIENT_NAME = "sensor_cars_inout"
MQTT_TOPIC = "car_count"

# MQTT client

# Create client and connect client to host
client = mqtt.Client(MQTT_CLIENT_NAME)
client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEP_ALIVE)

# To get feedback on initial connection
print(f"Sending message to MQTT broker {MQTT_HOST} on port {MQTT_PORT}.")
print(f"with the topic {MQTT_TOPIC}.")"""

while True:
    # Start the car counter
    CarDetector()


