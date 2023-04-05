# set PWM and frequency with pots
# The frequency value is not stable because of the ADC signal noise
# frequency is ajustable from about 600Hz to 66kHz

from pwmc import PWMc
from machine import Pin
import time
from lcdlib import CharLCD

lcd = CharLCD(rs=16, en=17, d4=18, d5=19, d6=20, d7=21,
				  cols=16, rows=2)
        
lcd.message('Hello', 2)

    
a0 = Pin(26, Pin.IN)				  # this is needed to turn input to high impedance   
adc0 = machine.ADC(0)		# Pin 31

a1 = Pin(27, Pin.IN)				  # this is needed to turn input to high impedance   
adc1 = machine.ADC(1)		# Pin 31


pw = PWMc(3, freq= 200E3)
pw.set_pwm(0)

while True:
    v = adc0.read_u16() / 65535
        
    pw.set_pwm(v)
    time.sleep_ms(20)
    p = int(v * 100)
    lcd.set_line(1)
    lcd.message(str(p) + "%", 2)
    
    f = adc1.read_u16() + 500
    f = int(f/100)*100
    
    
    pw.set_freq(f)
    lcd.set_line(2)
    lcd.message(str(f) + "Hz", 2)
    
    print(v, f)
    



