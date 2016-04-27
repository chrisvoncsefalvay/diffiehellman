# coding=utf-8

# 
# (c) Chris von Csefalvay, 2015.

"""
decorators is responsible for [brief description here].
"""


def requires_private_key(func):
    """
    Decorator for functions that require the private key to be defined.
    """

    def func_wrapper(self, *args, **kwargs):
        if hasattr(self, "private_key"):
            func(self, *args, **kwargs)
        else:
            self.generate_private_key()
            func(self, *args, **kwargs)

    return func_wrapper


def requires_public_key(func):
    """
    Decorator for functions that require the public key to be defined. By definition, this includes the private key, as such, it's enough to use this to effect definition of both public and private key.
    """

    def func_wrapper(self, *args, **kwargs):
        if hasattr(self, "public_key"):
            func(self, *args, **kwargs)
        else:
            self.generate_public_key()
            func(self, *args, **kwargs)

    return func_wrapper
