import paho.mqtt.client as paho
broker = "broker.hivemq.com" 
topic = "alfaisal/omar" 
client = paho.Client()
client.connect(broker, 1883)
client.publish("omar/190378", "SE443")