import pycom
import machine 
import ubinascii
import time
from network import Bluetooth
from machine import Pin

bluetooth = Bluetooth()
#bluetooth.init()
#bluetooth.service('abc123')
print(ubinascii.hexlify(machine.unique_id(), ':').decode())
bluetooth.set_advertisement(name='LoPy', service_uuid=b'1234567890123456')

#alert = False

value = 0
p_in = Pin('G9', mode=Pin.IN)
alert = False

while True:
    # if(getPin == high alert= true)
    
    value = p_in()
    #print(alert)
    if (value == 0):
    #    alert = True
        print(value)
        bluetooth.advertise(True)
        time.sleep(10)
        bluetooth.advertise(False)

#bluetooth.advertise(True)
#time.sleep(10)
#bluetooth.advertise(False)