# set pwm value with potentiometer

from pwmc import PWMc
from machine import Pin
import time
 
    
a = Pin(26, Pin.IN)				  # this is needed to turn input to high impedance   
adc = machine.ADC(0)		# Pin 31

pw = PWMc(3, freq= 200E3)
pw.set_pwm(0)

while True:
    v = adc.read_u16() / 65535
    print(v)
    
    pw.set_pwm(v)
    time.sleep_ms(20)
    
    
    
    



