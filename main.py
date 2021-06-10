import os
import getbinance as binance
import getameritrade as ameritrade
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
    w = display.height
    h = display.width
    image = Image.new(mode='1', size=(w, h), color=255)
except IOError as e:
    exit(e)

def main():
    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), 'Coin: ' + binance.price(), font=body, fill=0, align='left')