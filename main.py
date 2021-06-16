import os
# import getbinance as binance
# import getameritrade as ameritrade
from waveshare_epd import epd2in13b_V3
from PIL import Image, ImageDraw, ImageFont

pic_dir = 'pic' # Points to pic directory.
body = ImageFont.truetype("Roboto-Black.ttf", 18)

#Initlizing 2.13 Display
try:
    # Display init, clear
    epd = epd2in13b_V3
    image = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 10, 200, 34), fill = 0)
except IOError as e:
    exit(e)

def main():
    image = Image.new(mode='1', size=(w, h), color=255)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), 'Coin: ', font=body, fill=0, align='left')