import os
import time
from dotenv import load_dotenv
from waveshare_epd import epd2in13b_V3
from PIL import Image, ImageDraw, ImageFont

# Load Tokens, Fonts, and Pictures dir.
load_dotenv()
key = os.getenv('apiKey')
secret = os.getenv('apiSecret')

pic_dir = 'pic' # Points to pic directory.
body = ImageFont.truetype(os.path.join(pic_dir, 'Roboyo-Black.ttc'), 18, index=5)

#Initlizing 2.13 Display
try:
    # Display init, clear
    display = epd2in13b_V3.EPD()
    display.init(display.lut_full_update)
    display.Clear(0) # 0: Black, 255: White
# These valuse are reversed intentionally to make sense physically.
    w = display.height
    h = display.width
    print('width:', w)
    print('height:', h)
    ### ... IMAGE CODE ... ###
except IOError as e:
    print(e)

