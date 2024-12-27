class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def do_sound(self):
        print(f"O {self.name} faz {self.sound}")


gato = Animal("gato", "miau")
cachorro = Animal("cachorro", "au au")

gato.do_sound()
cachorro.do_sound()