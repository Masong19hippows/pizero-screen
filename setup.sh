#!/bin/bash

if  [[ $1 = "-v" ]]; then
    echo "Option -v turned on"
    echo "Updating and instaling required packages..."
    apt-get update && apt-get upgrade -y
    sleep 2
    apt-get install python3-pip python3-pil python3-numpy -y
    sleep 2
    python3 -m pip install RPi.GPIO spidev python-dotenv python-binance td-ameritrade-python-api
    sleep 2
    echo "All Done"
else
    echo "Option -v Turned off"
    echo "Updating and instaling required packages..."
    apt-get update > /dev/null 2>&1 && apt-get upgrade -y > /dev/null 2>&1
    sleep 2
    apt-get install python3-pip python3-pil python3-numpy python-binance python-dotenv -y > /dev/null 2>&1
    sleep 2
    python3 -m pip install RPi.GPIO spidev python-dotenv python-binance td-ameritrade-python-api > /dev/null 2>&1
    sleep 2
    echo "All Done!"
fi

#Get API key and Secret and add into .env file
if [ -f .env ]; then
    read -p 'Do you wish to overwite existing Keys file? Type "Y" or "N":' yn
    case $yn in
    [Yy]* ) echo "Type in your api key:"; read apiKey;  echo "Now, type in your api secret:"; read apiSecret; printf "apiKey=$apiKey\napiSecret=$apiSecret" > .env; exit;;
    [Nn]* ) exit;;
    esac
else
    echo "Type in your Binance api key:"
    read binanceKey
    echo "Type in your Binance api secret:"
    read binanceSecret
    echo "Type in your Ameritrade consumer key"
    read consumerKey
    printf "apiKey=$binanceKey\napiSecret=$binanceSecret\nconsumerKey=$consumerKey" > creds/.env
    exit
fi