from ninja import Ninja

class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.sound = sound
        self.health = 100
        self.energy = 100

    def play(self):
        self.health = self.health + 5
        print(f"{self.name} Health: {self.health}")
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"{self.name} Energy: {self.energy}, Health: {self.health}")
        return self

    def noise(self):
        print(f"{self.sound}")

    def sleep(self):
        self.energy = self.energy + 25
        print(f"{self.name} is sleeping. Energy: {self.energy}")
        return self

    def display_pet(self):
        print(f"Name: {self.name}, Type: {self.type}, Tricks: {self.tricks}, Sound: {self.sound}")

pet1 = Pet("Mr. Snuggles", "Dog", "Roll-over", "Hello")
ninja1 = Ninja("Matthew", "Luk", pet1, "Sandwich", "Pet food")

ninja1.display_info()
ninja1.pet.display_pet()
ninja1.walk()
ninja1.feed()
ninja1.bathe()
ninja1.pet.sleep()
pet1.sleep()