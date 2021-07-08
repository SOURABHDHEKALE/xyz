

class Human:
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation
        
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name, "play tennis")
            
        elif self.occupation == "acotor":
            print(self.name, "shoot a film")
            
    def speak(self):
        print(self.name, "say how are you?")
        
toom = Human("toom cruse", "acotor")
toom.do_work()
toom.speak()
        
maria = Human("maria sharapova", "tennis player")
maria.do_work()
maria.speak()
