# PubMatic-SKAdNetwork-App

## Introduction
Sample apps demonstrating the Application side logic & server side API requirements to use SKAdNetwork for app install validations.

This repo contains main three components

1. iOS Publisher App
2. iOS Advertiser App
3. Python scripts
   1. Ad server (Demonstrative)
   2. Postback server

## Publisher App

This application integrated with iOS OpenWrapSDK 1.6.2, which handles Publisher/Source App side implementaion.

### Running the app

- Add valid ad network id in the app in plist - change <ADNET_ID> in plist file
- Run the demo ad server, refer  [Ad server](https://git.pubmatic.com/PubMatic/PubMatic-SKAdNetwork-App#ad-server)
- Pod install & run the app


## Advertiser App

- This app contain demonstrative code
- This app shows steps needed from Advertiser Application
  - Calling registerAppForAdNetworkAttribution() in App Delegate
  - Calling updateConversionValue(:) (Optioanlly)



## Python scripts
### Pre-requisite
To run this script, make sure python3 is installed on the machine
* Python 3 
* pip3

### Ad server
This server responds with Ad in RTB format along with skadn object containg SKAdNetwork information.
Follow below steps to run the server

- Place your private key in the `SKAdNetwork-Python-Scripts` with name `private_key.pem`
- Change <ADNET_ID> in SKAdNetwork-Python-Scripts/ad_server.py to actual ad network id assigned by Apple
- Run below commands
  - `cd SKAdNetwork-Python-Scripts`
  - `pip3 install -r requirements.txt` (make sure you are using python3)
  - `python3 ad_server.py`

This runs the server on port 8080 that serves ad responses to the publisher app.

Please refer Details about generating public, private keys [Here](https://developer.apple.com/documentation/storekit/skadnetwork/registering_an_ad_network)

### Postback server
This is demo API which consumes postback request from Apple as HTTP Post data. It validates it's authenticity using Apple's Public key.
