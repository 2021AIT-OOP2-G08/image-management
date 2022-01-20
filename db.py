from pymongo import MongoClient
class DB():
    def __init__(self):
         self.clint = MongoClient()
         self.db = self.clint['oop2']
    #データの登録処理

    def add_one(self,item):
        return self.db.imgs.insert_one(item)

    def get(self):
        return self.db.prefectures.find_one()


def main():
    db = DB()
    print(db.get())
    

if __name__ == '__main__':
    main()
