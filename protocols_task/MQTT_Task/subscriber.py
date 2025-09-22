
from paho.mqtt.client import Client

broker = 'localhost'
port = 1883


sub = Client()

sub.connect(broker,port,keepalive=10)

def print_temp(client, userdata, msg):
    print(f"Temp : {msg.payload.decode()}")

sub.subscribe("Temp")
sub.on_message = print_temp

sub.loop_forever()
