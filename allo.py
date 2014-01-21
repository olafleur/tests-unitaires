import unittest


class Chat(object):
    def __init__(self):
        self.energie = 100

    def miaule(self):
        self.energie -= 10
        print("Miaou")


class ChatTest(unittest.TestCase):
    def setUp(self):
        self.chat = Chat()

    def test_miaule(self):
        self.chat.miaule()

        self.assertEquals(70, self.chat.energie)