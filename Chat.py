class Chat(object):
    def __init__(self):
        self.energie = 100

    def miaule(self):
        self.energie -= 10
        print("Miaou")