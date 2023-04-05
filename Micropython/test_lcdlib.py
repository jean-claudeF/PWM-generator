"""Example using a character LCD connected to an ESP8266 or Pico."""

from time import sleep
from lcdlib import CharLCD

lcd = CharLCD(rs=16, en=17, d4=18, d5=19, d6=20, d7=21,
				  cols=16, rows=2)

def hello_world():
	 # Print a 2 line centered message
	lcd.message('Hello', 2)
	lcd.set_line(1)
	lcd.message('World!', 2)

def underline_cursor():
	# Show the underline cursor.
	
	lcd.show_underline()
	lcd.message('Underline')
	lcd.set_line(1)
	lcd.message('Cursor: ')

def blinking_cursor():
	# Also show the blinking cursor.
	
	lcd.show_blink()
	lcd.message('Blinking')
	lcd.set_line(1)
	lcd.message('Cursor: ')

def disable_cursor():
	# Disable blink and underline cursor.
	lcd.show_underline(False)
	lcd.show_blink(False)

def scrolldemo():
	# Scroll message right & left.
	
	lcd.message('Scrolling Demo')
	sleep(1.0)
	for i in range(16):
		sleep(0.25)
		lcd.move_right()
	for i in range(16):
		sleep(0.25)
		lcd.move_left()
	sleep(2.0)
	
def create_char_demo():
	lcd.create_char(0, bytearray([7, 12, 24, 16, 22, 22, 22, 16]))
	lcd.create_char(1, bytearray([28, 6, 3, 1, 13, 13, 13, 1]))
	lcd.create_char(2, bytearray([16, 20, 20, 23, 19, 24, 12, 7]))
	lcd.create_char(3, bytearray([1, 1, 5, 29, 25, 3, 6, 28]))
	lcd.clear()
	lcd.message('The', 3)
	lcd.home()
	lcd.message('\x00')
	lcd.message('\x01')
	lcd.set_line(1)
	lcd.message('End', 3)
	lcd.set_cursor(0, 1)
	lcd.message('\x02')
	lcd.message('\x03')
	

	
hello_world()
sleep(3.0)

lcd.clear()
underline_cursor()
sleep(3.0)

lcd.clear()
blinking_cursor()
sleep(3.0)

disable_cursor()
lcd.clear()

scrolldemo()

# The End
create_char_demo()
