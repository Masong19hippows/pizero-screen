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

binancePercent = binance.percent()
ameritradePercent = ameritrade.percent()
drawBlack = ImageDraw.Draw(HBlackImage)
drawRed = ImageDraw.Draw(HRedImage)

drawBlack.text((0, 0), "Binance: $",font=body, fill=0, align='left')
drawBlack.text((0, 50), "Ameritrade: $", font=body, fill=0, align='left')
ogBlack = HBlackImage.copy()
ogRed = HRedImage.copy()
drawBlack.text((95, 0), binance.price(),font=body, fill=0, align='left')
drawBlack.text((127, 50), ameritrade.price(), font=body, fill=0, align='left')
if float(binancePercent) < 0:
    drawRed.text((115, 20), binancePercent + "%",font=body, fill=0, align='left')
else:
    drawBlack.text((115, 20), "+" + binancePercent + "%",font=body, fill=0, align='left')

if float(ameritradePercent) < 0:
    drawRed.text((115, 70), ameritradePercent + "%",font=body, fill=0, align='left')
else:
    drawBlack.text((115, 70), "+" + str(ameritradePercent) + "%",font=body, fill=0, align='left')

display.display(display.getbuffer(HBlackImage), display.getbuffer(HRedImage))

drawBlack = ImageDraw.Draw(HBlackImage)
drawRed = ImageDraw.Draw(HRedImage)

def updateDisplay(self):

    def __init__(self, black, red): 
        self.black = HBlackImage
        self.red = HRedImage
    

    drawBlack = ImageDraw.Draw(self.black)
    drawRed = ImageDraw.Draw(self.red)

    drawBlack.text((95, 0), binance.price(),font=body, fill=0, align='left')
    drawBlack.text((127, 50), ameritrade.price(), font=body, fill=0, align='left')

    binancePercent = binance.percent()
    if float(binancePercent) < 0:
        drawRed.text((115, 20), binancePercent + "%",font=body, fill=0, align='left')
    else:
        drawBlack.text((115, 20), "+" + binancePercent + "%",font=body, fill=0, align='left')
    
    ameritradePercent = ameritrade.percent()
    if float(ameritradePercent) < 0:
        drawRed.text((115, 70), ameritradePercent + "%",font=body, fill=0, align='left')
    else:
        drawBlack.text((115, 70), "+" + ameritradePercent + "%",font=body, fill=0, align='left')

    display.display(display.getbuffer(self.black), display.getbuffer(self.red))

    time.sleep(29)

while True:
    time.sleep(1)
    updateDisplay(black=ogBlack, red=ogRed)
    