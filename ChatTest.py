import unittest
from Chat import Chat


class ChatTest(unittest.TestCase):
    def setUp(self):
        self.chat = Chat()

    def test_miaule(self):
        self.chat.miaule()

        self.assertEquals(70, self.chat.energie)