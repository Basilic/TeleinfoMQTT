#!/usr/bin/python
import time
import serial
import paho.mqtt.client as mqtt
ser = serial.Serial(
        port='/dev/teleinfo',           
        baudrate=1200,                  # 1200 bauds
        bytesize = serial.SEVENBITS,    # 7bits
        parity = serial.PARITY_EVEN,    # parite paire
        stopbits = serial.STOPBITS_ONE, # un bit de stop
        xonxoff = False,                # pas de controle de flux
        timeout = 1
        )
def on_disconnect(mqtc, obj, rc):
    print("reconnecte")
    mqttc.reconnect()
print("Lancement teleinfo")
mqttc = mqtt.Client(client_id="edf")
mqttc.connect("127.0.0.1", 1883, 60)
mqttc.loop_start()
while 1:
    x = ser.readline()
    try:
            c=x.split(' ')
            try:
	            mqttc.publish("edf/"+c[0].lower(),int(c[1]))
            except:
        	    mqttc.publish("edf/"+c[0].lower(),c[1])
    except:
            print("error")
