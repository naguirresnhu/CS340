rom pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, user='aacuser1', password='SNHU1234'):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31890
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data) #data should be dictionary
            return result.acknowledged #returns result despite successful
        else:
            raise Exception('Nothing to save, because data parameter is empty')
   

    # Create method to implement the R in CRUD.
    def read(self, data):
        result_list = []
        if data is not None:
            result_list =list(self.database.animals.find(data)) 
            return result_list
    
    # Create method to implement U in CRUD
    def update(self, data, new_data):
        if data and new_data is not None:
            result = self.database.animals.update_many(data, new_data) 
            return result.modified_count
        else:
            raise Exception('Nothing to update, because data or new_data parameter is empty')
            
    # Create method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data) 
            return result.deleted_count
        else:
            raise Exception('Nothing to delete, because data parameter is empty')
            
    