class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.age = data["age"]
        self.position = data["position"]
        self.team = data["team"]

    def display_player_info(self):
        print(f"name: {self.name} age: {self.age} position: {self.position} team: {self.team}")

    @classmethod
    def add_players(cls, data):
        new_team = []
        for dict in data:
            new_team.append(cls(dict))
        return new_team


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
player_jason = Player(jason)
player_kyrie = Player(kyrie)
player_damian = Player(damian)
player_joel = Player(joel)
player_kevin.display_player_info()
player_jason.display_player_info()
player_kyrie.display_player_info()
player_damian.display_player_info()
player_joel.display_player_info()