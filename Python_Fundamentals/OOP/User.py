class User:

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_members = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name is: {self.first_name}")
        print(f"Last name is: {self.last_name}")
        print(f"Email is: {self.email}")
        print(f"Age is: {self.age}")
        print(f"Rewards member status: {self.is_rewards_members}")
        print(f"Gold card points: {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_members == True:
            print("Already a rewards memeber")
        else:
            self.gold_card_points = self.gold_card_points + 200
            self.is_rewards_members = True

    def spend_points(self,amount):
        if self.gold_card_points < amount:
            return("Not enough points")
        else:
            self.gold_card_points = (self.gold_card_points - amount)


myUser = User("Matthew", "Luk", "Matthew.Luk@yahoo.com", 26)
myUser2 = User("Abby", "Saeturn", "randomemail@gmail.com", 24)
myUser.display_info()
myUser2.display_info()
myUser.enroll()
myUser2.enroll()
myUser.display_info()
myUser2.display_info()
myUser.spend_points(50)
myUser2.spend_points(80)
myUser.display_info()
myUser2.display_info()