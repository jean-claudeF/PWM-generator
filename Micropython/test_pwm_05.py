# Set PWM and frequency with pots
# To remove jitter, frequency setting can be switched on and off.
# Once frequency is set, we can go to hold for the frequency.
# Frequency is ajustable from about 600Hz to 66kHz

from pwmc import PWMc
from machine import Pin
import time
from lcdlib import CharLCD

lcd = CharLCD(rs=16, en=17, d4=18, d5=19, d6=20, d7=21,
				  cols=16, rows=2)
        
lcd.message('Hello', 2)


# Potentiometers f, pwm:
a0 = Pin(26, Pin.IN)				  # this is needed to turn input to high impedance   
adc0 = machine.ADC(0)		# Pin 31
a1 = Pin(27, Pin.IN)				  # this is needed to turn input to high impedance   
adc1 = machine.ADC(1)		# Pin 31

# switch set f
sw_set_f = Pin(13, Pin.IN, Pin.PULL_UP)


# Init PWM
f = 16E3
pw = PWMc(3, freq= f)
pw.set_pwm(0)

#--------------------------------------------------------
def display(vp, f):
    lcd.set_line(1)
    p = "%.1f" % (vp * 100)
    lcd.message(str(p) + "%", 2)
    lcd.set_line(2)
    lcd.message(str(f) + "Hz", 2)
    
    print(vp, f)

#----------------------------------------------------------------
while True:
    vp = adc0.read_u16() / 65535
    pw.set_pwm(vp) 
    
    # if switch is activated, frequency can be adjusted
    # else: go on with last frequency setting
    if sw_set_f.value() == 0:
        vf = adc1.read_u16() + 500
        f = int(vf/100)*100             # to remove jitter, restricht frequency changes to multiples of 100Hz
        pw.set_freq(f)
    
       
    display(vp, f)
    
    time.sleep_ms(20)



