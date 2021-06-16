import os
import getbinance as binance
import getameritrade as ameritrade
from waveshare_epd import epd2in13bc
from PIL import Image, ImageDraw, ImageFont

body = ImageFont.truetype("pic/Roboto-Black.ttf", 18)
pic_dir = 'pic' # Points to pic directory .
#Initlizing 2.13 Display
# Display init, clear
display = epd2in13bc.EPD()
display.init()

HBlackImage = Image.new('1', (epd2in13bc.EPD_HEIGHT, epd2in13bc.EPD_WIDTH), 255)
HRedImage = Image.new('1', (epd2in13bc.EPD_HEIGHT, epd2in13bc.EPD_WIDTH), 255)
draw2 = ImageDraw.Draw(HRedImage)
draw = ImageDraw.Draw(HBlackImage)
draw.text((0, 0), str(binance.price()), font = body, fill = 0)
draw2.paste(Image.open('pic/binance.png'), (255, 0))
display.display(display.getbuffer(HBlackImage), display.getbuffer(HRedImage))

def main():
    test = "test"
