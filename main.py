#!/usr/bin/python3
import os
import time
import getbinance as binance
import getameritrade as ameritrade
from waveshare_epd import epd2in13bc
from PIL import Image, ImageDraw, ImageFont

# Creates font and points to pic directory
body = ImageFont.truetype(os.path.dirname(os.path.realpath(__file__)) + "/pic/Roboto-Black.ttf", 20)

#Initlizing 2.13 Display
# Display init, clear
display = epd2in13bc.EPD()
display.init()

# Creating variables to controll screen and clearing screen
HBlackImage = Image.new('1', (epd2in13bc.EPD_HEIGHT, epd2in13bc.EPD_WIDTH), 255)
HRedImage = Image.new('1', (epd2in13bc.EPD_HEIGHT, epd2in13bc.EPD_WIDTH), 255)
display.Clear()

# Making variables with prices to save on API calls
binancePercent = binance.percent()
ameritradePercent = ameritrade.percent()
drawBlack = ImageDraw.Draw(HBlackImage)
drawRed = ImageDraw.Draw(HRedImage)

# Writing the base outline and making a future copy of it or future use
drawBlack.text((0, 0), "Binance: $",font=body, fill=0, align='left')
drawBlack.text((0, 50), "Ameritrade: $", font=body, fill=0, align='left')
ogBlack = HBlackImage.copy()
ogRed = HRedImage.copy()

# Drawing The percentages on diffrent line
drawBlack.text((95, 0), binance.price(),font=body, fill=0, align='left')
drawBlack.text((126, 50), ameritrade.price(), font=body, fill=0, align='left')
if float(binancePercent) < 0:
    drawRed.text((115, 25), binancePercent + "%",font=body, fill=0, align='left')
else:
    drawBlack.text((115, 25), "+" + binancePercent + "%",font=body, fill=0, align='left')

if float(ameritradePercent) < 0:
    drawRed.text((115, 75), ameritradePercent + "%",font=body, fill=0, align='left')
else:
    drawBlack.text((115, 75), "+" + str(ameritradePercent) + "%",font=body, fill=0, align='left')

# Writing to display
rotatedBlackImage = HBlackImage.rotate(180,  expand=1)
rotatedRedImage = HRedImage.rotate(180,  expand=1)
display.display(display.getbuffer(rotatedBlackImage), display.getbuffer(rotatedRedImage))

def updateDisplay():

# Restoring from copy made earlier
    HBlackImage = ogBlack.copy()
    HRedImage = ogRed.copy()
    drawBlack = ImageDraw.Draw(HBlackImage)
    drawRed = ImageDraw.Draw(HRedImage)

# Updating Prices for ameritrade and binance to screen
    drawBlack.text((95, 0), binance.price(),font=body, fill=0, align='left')
    drawBlack.text((126, 50), ameritrade.price(), font=body, fill=0, align='left')

# Updating binance percent to screen
    binancePercent = binance.percent()
    if float(binancePercent) < 0:
        drawRed.text((115, 25), binancePercent + "%",font=body, fill=0, align='left')
    else:
        drawBlack.text((115, 25), "+" + binancePercent + "%",font=body, fill=0, align='left')

# Updating ameritrade percent to screen
    ameritradePercent = ameritrade.percent()
    if float(ameritradePercent) < 0:
        drawRed.text((115, 75), ameritradePercent + "%",font=body, fill=0, align='left')
    else:
        drawBlack.text((115, 75), "+" + ameritradePercent + "%",font=body, fill=0, align='left')

# Displaying changes to screen and rotaing it 180 degrees
    rotatedBlackImage = HBlackImage.rotate(180,  expand=1)
    rotatedRedImage = HRedImage.rotate(180,  expand=1)
    display.display(display.getbuffer(rotatedBlackImage), display.getbuffer(rotatedRedImage))

# Adding countdown timer untill next exec
    time.sleep(1)

# Creates a loop to update the display
while True:
    time.sleep(1 * 60)
    updateDisplay()
