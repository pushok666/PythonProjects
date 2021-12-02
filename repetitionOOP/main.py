


class Animal():
    
    def __init__(self, name, breed, voice) :
        self.name = name
        self.breed = breed
        self.voice = voice
        self.test = "test"
    def get_voice(self):
        print(self.voice * 3)
        print(self.test)
        


cat = Animal("Boris", "Cat","Myau")
cat.get_voice()