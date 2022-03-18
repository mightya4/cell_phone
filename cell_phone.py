from pyexpat import model


class CellPhone:
    def __init__(self, model=""):
        self.model = model
        self.phone_number = 0
        self.contacts = dict()
        self.messages = []
        is_vibrate = False

    def receive_txt_message(self, message):
        print(message)
        self.messages.append(message)
