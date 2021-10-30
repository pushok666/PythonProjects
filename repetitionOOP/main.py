


class Animal():
    def __init__(self, name, breed, voice) :
        self.name = name
        self.breed = breed
        self.voice = voice
    def get_voice(self):
        print(self.voice * 3)


cat = Animal("Boris", "Cat","Myau")
cat.get_voice()