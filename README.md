# PWM-generator
Versatile PWM generator with Raspi Pico

## Purpose
While developing switching power supplies I need a PWM generator.
I had once built one using a Mega8. Just as I put it on my lab table, I had the thought that it would be much better to use a Pico and program it with Micropython. A short test showed that I was right: the Pico has the advantage that the frequency can be adjusted up to frequencies in the MHz range.

## Test programs
All of these use the pwmc lib
- test_pwm_01.py    test pwmc library
- test_pwm_02.py    set pwm value with potentiometer
- test_pwm_03.py    set pwm value with potentiometer and show the result 0% ... 100% on LCD
- test_pwm_04.py    set PWM and frequency with pots

The test_pwm_04.py program works (nearly) fine, but there is a lot of jitter in the signal, and the frequency is not stable, due to the inaccuracy of the ADC.

- test_pwm_05.py resolves this problem by switching frequency setting on and off. After frequency is set, the generator holds the last frequency.

