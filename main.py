import os
import time
from getprice import price
from waveshare_epd import epd2in13b_V3
from PIL import Image, ImageDraw, ImageFont

pic_dir = 'pic' # Points to pic directory.
body = ImageFont.truetype("Roboto-Black.ttf", 18, index=5)

#Initlizing 2.13 Display
try:
    # Display init, clear
    display = epd2in13b_V3.EPD()
    display.init(display.lut_full_update)
    display.Clear(0) # 0: Black, 255: White
    # These valuse are reversed intentionally to make sense physically.
except IOError as e:
    exit(e)