from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Rideshare:
    db = "rideshares"
    def __init__(self,data):
        self.id = data["id"]
        self.destination = data["destination"]
        self.pickup = data["pickup"]
        self.date = data["date"]
        self.details = data["details"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def save(cls,data):
        query = "INSERT INTO rideshares(destination,pickup,date,details) VALUES(%(destination)s,%(pickup)s,%(date)s,%(details)s)"
        return connectToMySQL(cls.db).query_db(query,data)