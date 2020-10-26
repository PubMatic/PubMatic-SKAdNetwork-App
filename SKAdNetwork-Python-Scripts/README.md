## Pre-requisite
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

## Postback server
This is demo API which consumes postback data from Apple as HTTP Post incoming data. It validates its authenticity using Apple's Public key.
