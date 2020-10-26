import copy
from common.ecdsa_wrapper import ECDSAWrapper
import json

SIGNATURE_SEPARATOR = u'\u2063'

class SKAdNetwork :

  @staticmethod
  def sign(payload,private_key):
    fields = [
            payload["version"],
            payload["network"],
            payload["campaign"],
            payload["itunesitem"],
            payload["nonce"],
            payload["sourceapp"],
            payload["timestamp"]
            ]
    message = SIGNATURE_SEPARATOR.join(fields)
    ecdsa = ECDSAWrapper(private_key)
    signature = ecdsa.sign(message).decode('utf8')

    jsonObj = copy.deepcopy(payload)
    jsonObj["signature"] = signature
    return jsonObj

  @staticmethod	
  def verify(payload,public_key):
    redownloadString = str("{}").format(payload["redownload"]).lower()
    fields = [
        str(payload["version"]),
        payload["ad-network-id"],
        str(payload["campaign-id"]),
        str(payload["app-id"]),
        payload["transaction-id"],
        redownloadString,
        str(payload["source-app-id"]),
        ]
    msg = SIGNATURE_SEPARATOR.join(fields)
    signature = payload["attribution-signature"]

    message = SIGNATURE_SEPARATOR.join(fields)
    ecdsa = ECDSAWrapper(public_key)
    verStatus = ecdsa.verify(message,signature)
    print(payload)
    return verStatus
