import paho.mqtt.client as mqtt
import time 
import json
import random

BROKER = "localhost"
PORT = 1883
TOPIC = "iot/sensors"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect(BROKER, PORT, 60)

print("Simulating IoT sensor")

try:
    while True:
        data = {
            "temperature":
round(random.uniform(20.0,30.0), 2),
            "humidity":
round(random.uniform(40.0,70.0),2),
            "motion": random.choice([True,False])
        }
        
        payload = json.dumps(data)
        
        client.publish(TOPIC, payload)
        print(f"Published: {payload}")
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Stopped publishing...")
    client.disconnect()