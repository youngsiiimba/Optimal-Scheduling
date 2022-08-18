import serial
import time
import data2thingsspeak as thingspeak

arduinoData = serial.Serial('com3', 96500)

cmd = ''
while True:
    cmd = thingspeak.read_data_thingspeak()
    cmd = cmd+'\r'
    arduinoData.write(cmd.encode())