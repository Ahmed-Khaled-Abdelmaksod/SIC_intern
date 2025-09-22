

from paho.mqtt.client import Client
import random 
import time

broker = 'localhost'
port = 1883
pub = Client()
pub.connect(broker,port,keepalive=10)

while True:
    temp = random.randint(20,35)
    pub.publish(topic="Temp",payload=temp)
    print(f"Publised Temp : {temp}")
    time.sleep(2)    