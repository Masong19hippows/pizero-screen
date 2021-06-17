import os
import time
import getbinance as binance
import getameritrade as ameritrade
from waveshare_epd import epd2in13bc
from PIL import Image, ImageDraw, ImageFont

# Creates font and points to pic directory
body = ImageFont.truetype("pic/Roboto-Black.ttf", 20)

#Initlizing 2.13 Display
# Display init, clear
display = epd2in13bc.EPD()
display.init()

# Creating variables to controll screen and clearing screen
HBlackImage = Image.new('1', (epd2in13bc.EPD_HEIGHT, epd2in13bc.EPD_WIDTH), 255)
HRedImage = Image.new('1', (epd2in13bc.EPD_HEIGHT, epd2in13bc.EPD_WIDTH), 255)
display.display(display.getbuffer(HBlackImage), display.getbuffer(HRedImage))
time.sleep(5)

binancePrice = binance.price()
binancePercent = binance.percent()
ameritradePrice = ameritrade.price()
ameritradePercent = ameritrade.percent()
drawBlack = ImageDraw.Draw(HBlackImage)
drawRed = ImageDraw.Draw(HRedImage)

drawBlack.text((0, 0), "Binance: $",font=body, fill=0, align='left')
drawBlack.text((0, 50), "Ameritrade: $", font=body, fill=0, align='left')
ogBlack = HBlackImage.copy()
ogRed = HBlackImage.copy()
drawBlack.text((95, 0), binancePrice,font=body, fill=0, align='left')
drawBlack.text((115, 50), ameritradePrice, font=body, fill=0, align='left')
if float(binancePercent) < 0:
    drawRed.text((115, 20), binancePercent + "%",font=body, fill=0, align='left')
else:
    drawBlack.text((115, 20), "+" + binancePercent + "%",font=body, fill=0, align='left')

if float(ameritradePercent) < 0:
    drawRed.text((115, 70), ameritradePercent + "%",font=body, fill=0, align='left')
else:
    drawBlack.text((115, 70), "+" + str(ameritradePercent) + "%",font=body, fill=0, align='left')

display.display(display.getbuffer(HBlackImage), display.getbuffer(HRedImage))

def updateDisplay():
    binancePrice = binance.price()
    binancePercent = binance.percent()
    ameritradePrice = ameritrade.price()
    ameritradePercent = ameritrade.percent()
    HBlackImage = ogBlack
    HRedImage = ogRed
    drawBlack = ImageDraw.Draw(HBlackImage)
    drawRed = ImageDraw.Draw(HBlackImage)
    drawBlack.text((95, 0), binancePrice,font=body, fill=0, align='left')
    drawBlack.text((115, 50), ameritradePrice, font=body, fill=0, align='left')

    if float(binancePercent) < 0:
        drawRed.text((115, 20), binancePercent + "%",font=body, fill=0, align='left')
    else:
        drawBlack.text((115, 20), "+" + binancePercent + "%",font=body, fill=0, align='left')

    if float(ameritradePercent) < 0:
        drawRed.text((115, 70), ameritradePercent + "%",font=body, fill=0, align='left')
    else:
        drawBlack.text((115, 70), "+" + ameritradePercent + "%",font=body, fill=0, align='left')

    display.display(display.getbuffer(HBlackImage), display.getbuffer(HRedImage))

time.sleep(10)
updateDisplay()