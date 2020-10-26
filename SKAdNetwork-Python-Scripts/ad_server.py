import sys
import json
import time
import uuid

from flask import Flask, request, jsonify
from common.skadnetwork import SKAdNetwork

app = Flask(__name__)

ADNET_ID = u'<ADNET_ID>'
CAMPAIGN_ID = u'1'  # Should be between 1-100
TARGET_ITUNES_ID = u'1499436635' # The product you want to advertise

@app.route('/rtb/2.5', methods=['POST'])
def get_skadnetwork_ad():
	content = request.json
	payload = {}
	nonce = str(uuid.uuid4())
	timestamp = str(int(time.time()*1000))
	skadn = content["imp"][0]["ext"]["skadn"]
	payload["version"] = skadn["version"]
	payload["sourceapp"] = skadn["sourceapp"]
	payload["nonce"] = nonce
	payload["timestamp"] = timestamp
	payload["campaign"] = CAMPAIGN_ID
	payload["itunesitem"] = TARGET_ITUNES_ID
	payload["network"] = ADNET_ID

	y = json.loads(response())

	path = "private_key.pem"
	private_key = loadKeyFromPath(path)

	y["seatbid"][0]["bid"][0]["ext"]["skadn"] = SKAdNetwork.sign(payload, private_key)
	return jsonify(y)

def loadKeyFromPath(path):
	try:
		key = open(path).read()
		return key
	except Exception:
		print("Please create a private_key.pem file with your private key")
		sys.exit(-1)

def response():
	return """{
	  "id": "4DA33069-2FD9-4322-9AF2-7C23D60143FC",
	  "seatbid": [
	    {
	      "bid": [
	        {
	          "id": "613673EF-A07C-4486-8EE9-3FC71A7DC73D",
	          "impid": "E1D4B54B-0A5D-4829-8289-C6FAC594B97B",
	          "price": 1,
	          "adm": "<style> body, html {height: 100%; margin: 0; } .bg {/* The image used */ background-image: url('https://ads.pubmatic.com/api/utility/publisher/130917/18959/PubMaticAdServer/Creative/4d2ea2bc-dd14-4afe-973a-8207de377927/TEST-AD-320x50.png'); /* Full height */ height: 100%; /* Center and scale the image nicely */ background-position: center; background-repeat: no-repeat; background-size: contain; }</style> </head> <body> <a href='https://apps.apple.com/tt/app/openwrap-sdk-app/id1499436635'><div class='bg' style='background-color:#4EC8ED'></div></a> </body><div style='position:absolute;left:0px;top:0px;visibility:hidden;'><img src='//t.pubmatic.com/wt?bidid=613673EF-A07C-4486-8EE9-3FC71A7DC73D&eg=1&en=1&iid=5cef2290-3b7f-4f18-95bc-9a8835c0da02&kgpv=NoAdServerBannerAdUnit%40320x50&pdvid=0&pid=1165&pn=pubmatic&pubid=156276&purl=&slot=E1D4B54B-0A5D-4829-8289-C6FAC594B97B_NoAdServerBannerAdUnit&tst=1596087035'></div>",
	          "adomain": [
	            "www.pubmatic.com"
	          ],
	          "iurl": "http://localhost11",
	          "crid": "creative111",
	          "h": 50,
	          "w": 320,
	          "ext": {
	            "refreshInterval": 0,
	            "crtype": "banner",
	            "prebid": {
	              "targeting": {
	                "pwtpb": "1.00"
	              },
	              "type": ""
	            }
	          }
	        }
	      ],
	      "seat": "pubmatic"
	    }
	  ],
	  "cur": "USD"
	}"""

if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)