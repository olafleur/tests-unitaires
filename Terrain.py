import time
from Chat import Chat


class AccesReseau(object):
    def operation_couteuse(self):
        time.sleep(20)
        return True


class Terrain(object):
    def __init__(self):
        self.acces_reseau = AccesReseau()
        self.chat = Chat(self.acces_reseau)