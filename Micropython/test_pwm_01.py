# test PWMc lib

from pwmc import PWMc

if __name__ == '__main__':
    print("Start PWM on GPIO 3, 200kHz, 60%")
    pw = PWMc(3, freq= 200E3)
    pw.set_pwm(0.6)

    import time
    time.sleep(2)
    
    print("Setting frequency to 1MHz")
    f = pw.set_freq(1000E3)
    print(f, "Hz")

    time.sleep(2)
    
    print("Setting PWM to 20%")
    d = pw.set_pwm(0.2)
    print(d ,"/ 65535")
    
    time.sleep(2)
    
    print("PWM stopped") 
    pw.stop()
    