class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print(f"{self.first_name} is now walking {self.pet.name}")
        self.pet.play()
        return self

    def feed(self):
        print(f"{self.first_name} is now feeding {self.pet.name} with {self.pet_food}")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"{self.first_name} bathed {self.pet.name}")
        self.pet.noise()
        return self

    def display_info(self):
        print(f"Name: {self.first_name} {self.last_name}, Pet: {self.pet.name}, Treats: {self.treats}, Pet Food: {self.pet_food}")