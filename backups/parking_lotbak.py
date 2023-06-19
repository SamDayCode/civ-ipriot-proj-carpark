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

class ParkingLot:

    def __init__(self, ):
        BROKER, PORT = "localhost", 1883

        self.client = paho.Client()
        self.client.connect(BROKER, PORT)
        self.MQTT_topic = "sensor/car_in_out"

        self.client = paho.Client()
        self.client.on_message = on_message
        self.client.connect(BROKER, PORT)
        self.client.subscribe(MQTT_topic)

        self.car_counter = 0

        """self.total_spaces = config['total-spaces']
        self.total_cars = config['total-cars']
        self.client.on_message = self.on_message
        self.client.subscribe('sensor')
        self.client.loop_forever()
        self._temperature = None"""

        self.client.loop_forever()

    def on_message(self, user_data, message):

        msg = message
        msg_data = str(msg.payload.decode("UTF-8"))
        data = json.loads(msg_data)
        cars = data["cars"]
        print(cars)
        print(f'Received {msg.payload.decode()}')
        self.car_counter = self.car_counter + cars
        print(self.car_counter)

ParkingLot()

car_counter = 0
total_spaces = 192

client = paho.Client()
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(MQTT_topic)

"""def car_in_and_out():
    if client.on_message() == (1):
        car_counter = client.on_message() + car_counter
        print("Car counter:", car_counter)
    elif client.on_message() == (-1):
        car_counter = client.on_message() + car_counter
        print("Car counter:", car_counter)
    else:
        print("broken - plz fix")"""


"""while True:
    if client.on_message() == (1):
        car_counter = client.on_message() + car_counter
        print("Car counter:", car_counter)
    elif client.on_message() == (-1):
        car_counter = client.on_message() + car_counter
        print("Car counter:", car_counter)
    else:
        print("broken - plz fix")"""


client.loop_forever()