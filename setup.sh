#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
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
    apt-get install python3-pip python3-pil python3-numpy -y > /dev/null 2>&1
    sleep 2
    python3 -m pip install RPi.GPIO spidev python-dotenv python-binance td-ameritrade-python-api > /dev/null 2>&1
    sleep 2
    echo "All Done!"
fi

#Get API key and Secret and add into .env file
if test -f creds/.env; then
    read -p 'Do you wish to overwite existing Keys file? Type "Y" or "N":' yn
    case $yn in
    [Yy]* ) echo "Type in your Binance api key:"; read binanceKey; echo "Type in your Binance api secret:"; read binanceSecret; echo "Type in your Ameritrade consumer key"; read consumerKey; printf "binanceKey=$binanceKey\nbinanceSecret=$binanceSecret\nconsumerKey=$consumerKey" > creds/.env; exit;;
    [Nn]* ) exit;;
    esac
else
    echo "Type in your Binance api key:"
    read binanceKey
    echo "Type in your Binance api secret:"
    read binanceSecret
    echo "Type in your Ameritrade consumer key"
    read consumerKey
    printf "binanceKey=$binanceKey\nbinanceSecret=$binanceSecret\nconsumerKey=$consumerKey" > creds/.env
    exit
fi
printf "@reboot pi bash  $DIR/main.py" > /etc/cron.d/screen