import i2c_lcd_driver

from time import *

lcd = i2c_lcd_driver.lcd()

lcd.lcd_display_string("Hello world!", 2, 3)