# What is this?
This is my code for the Raspberry Pi Zero W 2.13 BWR e-ink screen

## Purpose
The purpose of this project is to be a simple run and go script that updates the display every minute with stocks information. The stocks that are supported are binance and TDAmeritrade. This python project grabs the latest price and percent change info for all stocks on both of these platforms. 

## Setup
The setup is stupidly simple. Just run these instructions in any directory that you want th folder installed in. Yoou will need a binance api key and secret, as well as an TDAmeritrade api key.

'<# git clone https://github.com/masong19hippows/pizero-screen>'

'<# cd pizero-screen>'

'<# sudo ./setup>'

And, there you go. Once it begins, it will perform an update and upgrade using apt-get. After that, it will install the nessesary python packages using pip. The setup file will prompt you for the binance api key and secret as well as the TDAmeritrade api key mentioned above. After this, it will authorize the TDAmeritrade api by having you go to a URL, type in your credentials, and paste the redirect URL. 

If you have any isssues with it not working correctly, or are just concerned about whats going on, then you can turn on verbose mode with the flag -v. This will just give more output from the commands instead of staying silent.

'<# sudo ./setup -v>'
