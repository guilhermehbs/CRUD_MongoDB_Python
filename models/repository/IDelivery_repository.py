class IDeliveryRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "IDelivery"
        self.__db_connection = db_connection

    #Create
    def insert_document(self, document: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)
        return document

    def insert_list_of_documents(self, list_of_documents: list[dict]) -> list[dict]:
        collection = self.__db_connection.getcollection(self.__collection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents

    #Read
    def select_all(self) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find({}, {'_id': 0})

        response = []
        for element in data: response.append(element)
        return response

    def select_many(self, filter: dict) -> list[dict]:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(filter, {'_id': 0})

        response = []
        for element in data: response.append(element)
        return response

    def select_one(self, filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(filter, {'_id': 0})
        return response

    #Update
    def edit_one_registry(self, filter, update) -> bool:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(filter, {'$set': update})
        return True

    def edit_many_registries(self, filter, update) -> bool:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(filter, {'$set': update})
        return True

    #Delete
    def delete_many_registries(self, filter) -> bool:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_many(filter)
        return True

    def delete_one_registry(self, filter) -> bool:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.delete_one(filter)
        return True