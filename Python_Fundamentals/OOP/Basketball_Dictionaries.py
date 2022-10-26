class Player:
        def __init__(self, data):
                self.name = data["name"]
                self.age = data["age"]
                self.position = data["position"]
                self.team = data["team"]

        def display_player_info(self):
                print(f"name: {self.name} age: {self.age} position: {self.position} team: {self.team}")

        @classmethod
        def get_team(cls, team_list):
                new_team = []
                for i in team_list:
                        new_team.append(i)
                return new_team

players = [
        {
                "name": "Kevin Durant", 
                "age":34, 
                "position": "small forward", 
                "team": "Brooklyn Nets"
        },
        {
                "name": "Jason Tatum", 
                "age":24, 
                "position": "small forward", 
                "team": "Boston Celtics"
        },
        {
                "name": "Kyrie Irving", 
                "age":32, "position": "Point Guard", 
                "team": "Brooklyn Nets"
        },
        {
                "name": "Damian Lillard", 
                "age":33, "position": "Point Guard", 
                "team": "Portland Trailblazers"
        },
        {
                "name": "Joel Embiid", 
                "age":32, "position": "Power Foward", 
                "team": "Philidelphia 76ers"
        },
        {
                "name": "", 
                "age":16, 
                "position": "P", 
                "team": "en"
        }
]

kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}

jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}

kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}

damian = {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
}

joel = {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
}


player_kevin = Player(kevin)
player_kevin.display_player_info()
player_jason = Player(jason)
player_jason.display_player_info()
player_kyrie = Player(kyrie)
player_kyrie.display_player_info()
player_damian = Player(damian)
player_damian.display_player_info()
player_joel = Player(joel)
player_joel.display_player_info()

# using a for loop to get all players in the list
new_team = []
for i in players:
        new_team.append(i)
print(new_team)

# using a class method to get all players in the list
print(Player.get_team(players))