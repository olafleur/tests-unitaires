class Chat(object):
    def __init__(self, acces):
        self.energie = 100
        self._bd = acces

    def miaule(self):
        self.energie -= 10
        self._bd.operationCouteuse()
