from pymongo import MongoClient

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, animal_id, breed, name, outcome):
     

        
        
        self.animal_id = animal_id
        self.breed = breed
        self.name = name
        self.outcome = outcome
        
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31580
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data=None):
        
        if data is None:
            data = {
                "animal_id": self.animal_id,
                "animal_type": self.animal_type,
                "breed": self.breed,
                "name": self.name,
                "outcome": self.outcome
                
            }
        
        if not data or not isinstance(data, dict):
            return False
        
        try:
            self.collection.insert_one(data)
            return True
        except:
            return False

    def read(self, query=None):
        """ Query documents from the animals collection.
        
        Args:
            query (dict, optional): Query criteria. If None, returns all documents.
        
        Returns:
            list: List of matching documents, or empty list if query fails.
        """
        if query is None:
            query = {}
        if not isinstance(query, dict):
            return []
        
        try:
            return list(self.collection.find(query))
        except:
            return []

    def update(self, query, data):
        """ Update documents in the animals collection.
        
        Args:
            query (dict): Criteria to select documents.
            data (dict): Key/value pairs to update.
        
        Returns:
            int: Number of documents updated.
        """
        if not isinstance(query, dict) or not isinstance(data, dict):
            return 0
        
        try:
            result = self.collection.update_many(query, {"$set": data})
            return result.modified_count
        except:
            return 0

    def delete(self, query):
        """ Delete documents from the animals collection.
        
        Args:
            query (dict): Criteria to select documents.
        
        Returns:
            int: Number of documents deleted.
        """
        if not isinstance(query, dict):
            return 0
        
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except:
            return 0