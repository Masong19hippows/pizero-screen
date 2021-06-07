import os
import time
from waveshare_epd import epd2in9
from PIL import Image, ImageDraw, ImageFont


pic_dir = 'pic' # Points to pic directory.

#Initlizing 2.13 Display
try:
    # Display init, clear
    display = epd2in9.EPD()
    display.init(display.lut_full_update)
    display.Clear(0) # 0: Black, 255: White
    w = display.height
    h = display.width
    print('width:', w)
    print('height:', h)
    ### ... IMAGE CODE ... ###
except IOError as e:
    print(e)