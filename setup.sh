#!/bin/bash


if  [[ $1 = "-v" ]]; then
    echo "Option -v turned on"
    echo "Updating and instaling required packages..."
    apt-get update && apt-get upgrade -y
    sleep 2
    apt-get install python3-pip python3-pil python3-numpy -y
    sleep 2
    python3 -m pip install RPi.GPIO spidev
    sleep 2
    echo "All Done"
else
    echo "Option -v Turned off"
    echo "Updating and instaling required packages..."
    apt-get update > /dev/null 2>&1 && apt-get upgrade -y > /dev/null 2>&1
    sleep 2
    apt-get install python3-pip python3-pil python3-numpy -y > /dev/null 2>&1
    sleep 2
    python3 -m pip install RPi.GPIO spidev > /dev/null 2>&1
    sleep 2
    echo "All Done!"
fi
    exit
