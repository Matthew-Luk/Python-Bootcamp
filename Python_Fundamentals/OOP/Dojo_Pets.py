class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pet("Mr. Snuggles", "Dog", "Roll over")

    def walk(self):
        print(f"You are now playing with {self.pet}")
        self.pet.play()

    def feed(self):
        print(f"You are now feeding {self.pet} with {self.pet_food}")
        self.pet.eat()

    def bathe(self):
        print(f"You have bathed {self.pet}")
        self.pet.noise()

    def display_info(self):
        print(f"{self.first_name}, {self.last_name}, {self.treats}, {self.pet_food}")

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy = self.energy + 25
        print(f"Energy: {self.energy}")
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"Energy: {self.energy}, Health: {self.health}")
        return self

    def play(self):
        self.health = self.health + 5
        print(f"Health: {self.health}")
        return self

    def noise(self):
        if self.type == "Dog":
            print("Woof!")
        elif self.type == "Cat":
            print("Meow!")
        elif self.type == "Pig":
            print("Oink!")
        return self

    def display_pet(self):
        print(f"{self.name}, {self.type}, {self.tricks}")


matthew = Ninja("Matthew", "Luk", "Sandwich", "Pet food")

matthew.display_info()
matthew.feed()
matthew.walk()
matthew.bathe()