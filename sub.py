import paho.mqtt.client as paho
broker = "broker.hivemq.com"  
topic = "alfaisal/omar"
def on_message(client, msg):
    message = msg.payload.decode()
    print(message)

client = paho.Client()
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe("omar/190378")
client.loop_forever()