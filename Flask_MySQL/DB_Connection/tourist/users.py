from mysqlconnection import connectToMySQL
class Tourist:
    def __init__( self , data ):
        self.id = data['id']
        self.attraction = data['attraction']
        self.city = data['city']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM tourists;"
        results = connectToMySQL('tourists').query_db(query)
        tourists = []
        for tourist in results:
            tourists.append( cls(tourist) )
        return tourists

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM tourists WHERE id = %(id)s;"
        results = connectToMySQL('tourists').query_db(query,data)
        return cls(results[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO tourists ( attraction, city ) VALUES (%(attraction)s , %(city)s);"
        return connectToMySQL('tourists').query_db( query, data )

    @classmethod
    def delete(cls):
        query = "DELETE FROM tourists WHERE id > 0;"
        return connectToMySQL('tourists').query_db(query)

    @classmethod
    def update(cls,data):
        query = "UPDATE tourists SET attraction=%(attraction)s,city=%(city)s WHERE id = %(id)s;"
        return connectToMySQL('tourists').query_db(query,data)