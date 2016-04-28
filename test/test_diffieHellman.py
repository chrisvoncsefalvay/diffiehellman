# coding=utf-8

# ${PROJECTNAME}
# (c) Chris von Csefalvay, 2015.

"""
test_diffieHellman tests the DiffieHellman class.
"""

import sys
import os
sys.path.append(os.path.join('..', 'diffiehellman'))
import unittest
from diffiehellman.diffiehellman import DiffieHellman


class TestDiffieHellman(unittest.TestCase):
    def setUp(self):
        self.alice = DiffieHellman()
        self.bob = DiffieHellman()

    def test_equality_of_keys(self):
        self.alice.generate_public_key()
        self.bob.generate_public_key()

        alices_shared_key = self.alice.generate_shared_secret(self.bob.public_key)
        bobs_shared_key = self.bob.generate_shared_secret(self.alice.public_key)

        self.assertEqual(alices_shared_key, bobs_shared_key,
                         "There is a mismatch between two shared secrets. Both shared secrets should be the same. This is bad.")

    def test_decorators_private_key(self):
        self.alice.generate_public_key()
        self.assertIn("_DiffieHellman__private_key", self.alice.__dict__)

    def test_generate_private_key(self):
        self.alice.generate_private_key()
        self.assertIn("_DiffieHellman__private_key", self.alice.__dict__)

    def test_generate_public_key(self):
        self.alice.generate_public_key()
        self.assertIn("public_key", self.alice.__dict__)

    def test_verify_public_key(self):
        self.alice.generate_public_key()
        self.bob.generate_public_key()
        self.assertTrue(self.alice.verify_public_key(self.bob.public_key))
        self.assertFalse(self.alice.verify_public_key(2))
        self.assertFalse(self.alice.verify_public_key(self.alice.prime - 1))


if __name__ == '__main__':
    unittest.main()