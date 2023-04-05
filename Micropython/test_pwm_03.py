# set pwm value with potentiometer and show the result 0% ... 100% on LCD

from pwmc import PWMc
from machine import Pin
import time
from lcdlib import CharLCD

lcd = CharLCD(rs=16, en=17, d4=18, d5=19, d6=20, d7=21,
				  cols=16, rows=2)
        
lcd.message('PWM generator', 2)

    
a = Pin(26, Pin.IN)				  # this is needed to turn input to high impedance   
adc = machine.ADC(0)		# Pin 31

pw = PWMc(3, freq= 200E3)
pw.set_pwm(0)

while True:
    v = adc.read_u16() / 65535
    print(v)
    
    pw.set_pwm(v)
    time.sleep_ms(20)
    p = int(v * 100)
    lcd.set_line(1)
    lcd.message(str(p), 2)
    
    
    
    
    



