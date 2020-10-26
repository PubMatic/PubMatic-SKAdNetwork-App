import sys
import json
import time
import uuid

from flask import Flask, request, jsonify
from common.skadnetwork import SKAdNetwork

app = Flask(__name__)

@app.route('/postback', methods=['POST'])
def handle_postback():
	payload = request.json
	path = "apple_public_key.pem"
	public_key = loadKeyFromPath(path)
	verStatus = SKAdNetwork.verify(payload, public_key)
	print("Verification status -",verStatus)
	return jsonify({"status":verStatus})

def loadKeyFromPath(path):
	try:
		key = open(path).read()
		return key
	except Exception:
		print("Please create a apple_public_key.pem file with your private key")
		sys.exit(-1)

if __name__ == '__main__':
    app.run('0.0.0.0', port=8082)
