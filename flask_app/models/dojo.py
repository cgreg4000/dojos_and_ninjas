from flask_app.config.mysqlconnection import connectToMySQL

from flask_app.models.ninja import Ninja

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id;"
    
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)

        if not results:
            return

        dojos = []

        new_dojo = Dojo(results[0])
        dojos.append(new_dojo)

        for item in results:

            if item['id'] != new_dojo.id:
                new_dojo = Dojo(item)
                dojos.append(new_dojo)
        
            if item['ninjas.id'] != None:
                ninja_data = {
                    'id': item['ninjas.id'],
                    'first_name': item['first_name'],
                    'last_name': item['last_name'],
                    'age': item['age'],
                    'dojo_id': item['dojo_id'],
                    'created_at': item['ninjas.created_at'],
                    'updated_at': item['ninjas.updated_at'],
                    'dojo': new_dojo
                }
                new_ninja = Ninja(ninja_data)
                new_dojo.ninjas.append(new_ninja)
    
        return dojos

    @classmethod 
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(dojo_name)s)"
    
        connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    
    @classmethod
    def get_one_dojo(cls, data):

        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        new_dojo = Dojo(results[0])

        for item in results:

            if item['ninjas.id'] != None:
                ninja_data = {
                    'id': item['ninjas.id'],
                    'first_name': item['first_name'],
                    'last_name' : item['last_name'],
                    'age' : item['age'],
                    'dojo_id' : item['dojo_id'],
                    'created_at' : item['ninjas.created_at'],
                    'updated_at' : item['ninjas.updated_at'],
                    'dojo' : new_dojo
                }
                new_ninja = Ninja(ninja_data)
                new_dojo.ninjas.append(new_ninja)
        
        return new_dojo