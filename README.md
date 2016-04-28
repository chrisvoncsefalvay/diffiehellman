# diffiehellman
![Travis CI](https://travis-ci.org/chrisvoncsefalvay/diffiehellman.svg?branch=master) [![PyPI version](https://badge.fury.io/py/diffiehellman.svg)](https://badge.fury.io/py/diffiehellman)

The Python Diffie-Hellman key exchange library.


## Usage

```python
from diffiehellman.diffiehellman import DiffieHellman

alice = DiffieHellman()
bob = DiffieHellman()

alice.generate_public_key()    # automatically generates private key
bob.generate_public_key()

alice.generate_shared_secret(bob.public_key, echo_return_key=True)
bob.generate_shared_secret(alice.public_key, echo_return_key=True)
```

## Install

```shell
pip install diffiehellman
```

## Features

* Implements Diffie-Hellman key exchange
* Pretty fast
* Adjustable key size
* Includes primes for groups 5 and 14-18
* Currently works only with Python 3 (requires ssl). An OpenSSL compatible version is in the works.

## Code of Misconduct

By using this package, you pledge to use it for good, not for evil. In particular, you pledge never to use this code to limit the human mind or its natural rights, in particular freedom of expression.
