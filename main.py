import os
import getbinance as binance
import getameritrade as ameritrade
from waveshare_epd import epd2in13bc
from PIL import Image, ImageDraw, ImageFont

# Creates font and points to pic directory
body = ImageFont.truetype("pic/Roboto-Black.ttf", 16)
pic_dir = 'pic'

#Initlizing 2.13 Display
# Display init, clear
display = epd2in13bc.EPD()
display.init()

# Creating variables to controll screen and clearing screen
HBlackImage = Image.new('1', (epd2in13bc.EPD_HEIGHT, epd2in13bc.EPD_WIDTH), 255)
HRedImage = Image.new('1', (epd2in13bc.EPD_HEIGHT, epd2in13bc.EPD_WIDTH), 255)
display.display(display.getbuffer(HBlackImage), display.getbuffer(HRedImage))

def main():
    binancePrice = binance.price()
    binancePercent = binance.percent()
    ameritradePrice = ameritrade.price()
    ameritradePercent = .5
    drawBlack = ImageDraw.Draw(HBlackImage)
    drawRed = ImageDraw.Draw(HRedImage)

    drawBlack.text((0, 0), "Binance: $" + binancePrice + " ",font=body, fill=0, align='left')
    drawBlack.text((0, 50), "Ameritrade: $" + ameritradePrice + ' ', font=body, fill=0, align='left')
    if float(binancePercent) < 0:
        drawRed.text((125, 20), binancePercent + "%",font=body, fill=0, align='left')
    else:
        drawBlack.text((125, 20), "+" + binancePercent + "%",font=body, fill=0, align='left')

    if float(ameritradePercent) < 0:
        drawRed.text((125, 70), ameritradePercent + "%",font=body, fill=0, align='left')
    else:
         drawBlack.text((125, 70), "+" + str(ameritradePercent) + "%",font=body, fill=0, align='left')

    display.display(display.getbuffer(HBlackImage), display.getbuffer(HRedImage))
main()
