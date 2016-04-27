# coding=utf-8

# 
# (c) Chris von Csefalvay, 2015.

"""
diffiehellmann declares the main key exchange class.
"""

__version__ = '0.13.1'

from hashlib import sha256
from ssl import RAND_bytes

from .decorators import requires_private_key
from .exceptions import MalformedPublicKey
from .primes import PRIMES

rng = RAND_bytes


class DiffieHellman:
    """
    Implements the Diffie-Hellman key exchange protocol.
    """

    def __init__(self,
                 group=18,
                 key_length=640):

        self.key_length = max(200, key_length)
        self.generator = PRIMES[group]["generator"]
        self.prime = PRIMES[group]["prime"]

    def generate_private_key(self):
        key_length = self.key_length // 8 + 8
        key = 0

        try:
            key = int.from_bytes(rng(key_length), byteorder='big')
        except:
            key = int(hex(rng(key_length)), base=16)

        self.private_key = key

    def verify_public_key(self, other_public_key):
        return self.prime - 1 > other_public_key > 2 and pow(other_public_key, (self.prime - 1) // 2, self.prime) == 1

    @requires_private_key
    def generate_public_key(self):
        self.public_key = pow(self.generator,
                              self.private_key,
                              self.prime)

    @requires_private_key
    def generate_shared_secret(self, other_public_key):
        if self.verify_public_key(other_public_key) is False:
            raise MalformedPublicKey

        self.shared_secret = pow(other_public_key,
                                 self.private_key,
                                 self.prime)

        shared_secret_as_bytes = self.shared_secret.to_bytes(self.shared_secret.bit_length() // 8 + 1, byteorder='big')

        _h = sha256()
        _h.update(bytes(shared_secret_as_bytes))

        self.shared_key = _h.hexdigest()
