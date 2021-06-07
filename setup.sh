#!/bin/bash

echo "Updating and instaling required packages"
apt-get update && apt-get upgrade -y
sleep 2
apt-get install python3-pip python3-pil python3-numpy -y
sleep 2
python3 -m pip install RPi.GPIO spidev
sleep 2
echo "All Done!"