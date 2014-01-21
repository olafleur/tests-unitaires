import unittest
from unittest.mock import Mock
from Chat import Chat
from Terrain import AccesReseau


class ChatTest(unittest.TestCase):
    def setUp(self):
        self.acces = AccesReseau()
        self.acces.operation_couteuse = Mock(return_value=False)
        self.chat = Chat(self.acces)

    def test_miaule(self):
        self.chat.miaule()

        self.assertEquals(90, self.chat.energie)

    def test_mock(self):
        self.assertFalse(self.acces.operation_couteuse())
