"""
FastECDSA Library Wrapper
"""

from fastecdsa import curve as fe_curve, keys as fe_keys, ecdsa as fe_ecdsa
from fastecdsa.encoding import der as fe_der, pem as fe_pem
from hashlib import sha256
import base64 as b64


class ECDSAWrapper(object):
   
    CURVE = fe_curve.P256
    HASH = sha256

    def __init__(self, pem=None):
        if pem is None:
            self._key, self._pubkey = fe_keys.gen_keypair(self.CURVE)
            return
        self._key, self._pubkey = fe_pem.PEMEncoder.decode_private_key(pem.strip())
        if self._pubkey is None:
            self._pubkey = fe_keys.get_public_key(self._key, self.CURVE)

    def sign(s, message):
        "signs `message` and returns a signature"
        if s._key is None: return None
        sigr, sigs = fe_ecdsa.sign(message, s._key, curve=s.CURVE, hashfunc=s.HASH)
        sig = fe_der.DEREncoder.encode_signature(sigr, sigs)
        return b64.b64encode(sig)

    def verify(s, message, sig):
        "verifies the message signature, returns True/False as result"
        sigbytes = b64.b64decode(sig)
        sigr, sigs = fe_der.DEREncoder.decode_signature(sigbytes)

        try:
            return fe_ecdsa.verify((sigr, sigs), message, s._pubkey, curve=s.CURVE, hashfunc=s.HASH)
        except:
            return False
