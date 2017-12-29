import hex
import unittest

moc_num = 254
moc_res = ['F','E']

class testhex(unittest.TestCase):

    def test_dec2hex(self):
        self.assertEqual(hex.dec2hex(moc_num), moc_res)