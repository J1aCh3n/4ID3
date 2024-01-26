import logging

import paho.mqtt.client as mqtt

logging.basicConfig(level=logging.DEBUG)

mqttc = mqtt.Client("Hanson")

logger = logging.getLogger()
mqttc.enable_logger(logger)

mqttc.connect("test.mosquitto.org", 1883, 60)
mqttc.subscribe("Hanson/temperature", 0)
mqttc.subscribe("Hanson/humidity", 0)
mqttc.subscribe("Hanson/pressure", 0)
mqttc.subscribe("Hanson/light", 0)

mqttc.loop_forever()