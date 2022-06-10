class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet("Mr. Snuggles", "Dog", "Roll over")
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print(f"You are now playing with {self.pet.name}")
        self.pet.play()
        return self

    def feed(self):
        print(f"You are now feeding {self.pet.name} with {self.pet_food}")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"You have bathed {self.pet.name}")
        self.pet.noise()
        return self

    def nap(self):
        print(f"You and {self.pet.name} have slept")
        self.pet.sleep()

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}, Pet: {self.pet.name}, Treats: {self.treats}, Pet Food: {self.pet_food}")

class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy = self.energy + 25
        print(f"Mr. Snuggles Energy: {self.energy}")
        return self

    def eat(self):
        self.energy = self.energy + 5
        self.health = self.health + 10
        print(f"Mr. Snuggles Energy: {self.energy}, Health: {self.health}")
        return self

    def play(self):
        self.health = self.health + 5
        print(f"Mr. Snuggles Health: {self.health}")
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


matthew = Ninja("Matthew", "Luk", "Mr.Snuggles", "Sandwich", "Pet food")


matthew.display_info()
matthew.nap()
matthew.feed()
matthew.walk()
matthew.bathe()