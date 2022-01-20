from pymongo import MongoClient
class DB():
    def __init__(self):
         self.clint = MongoClient()
         self.db = self.clint['oop2']
    #データの登録処理

    def add_one(self,item):
        return self.db.imgs.insert_one(item)

    def get_filteredCollection(self,collection_name,condition):
        return list(self.db[collection_name].find(condition))

    def get_document_one(self,collection_name,condition):
        return self.db[collection_name].find_one(condition)
