
from pymongo import MongoClient
from pymongo import errors


db = MongoClient("mongodb+srv://satyam:satyam@cluster0-mvyum.mongodb.net/test?retryWrites=true&w=majority")
class BaseMongo:
    __db_name = "DataBase_Name"
    __register__="register"
    vehicles="vehicles"
    mapdata="map"

    def getdatabase(self):
        return self.__db_name
    def getregister_collection(self):
        return self.__register__
    def getvehicles_collection(self):
        return self.vehicles
    def getmap_collection(self):
        return self.mapdata    

    def insert_data(self,data,database,collection_name):
        try:
            db_name=db[database]
            collection=db_name[collection_name]
            insert_data=collection.insert(data)
            if insert_data:
                 return insert_data
            return False
        except Exception as org:
            print("coming here")
            print(org)

    def find_data(self,key,value,database,collection_name):

        try:
            db_name=db[database]
            collection=db_name[collection_name]
            find_data=collection.find_one({key:value})
            if find_data:
                return find_data
        except Exception as org:
            print("coming here ")        
            print(org)
        
    def update_data(self,search_key,search_value,update_key,update_value,database,collection_name):
        try:
            db_name=db[database]
            collection=db_name[collection_name]
            update_data=collection.update_one({
                search_key: search_value
            }, {
                '$set': {
                    update_key: update_value
                }
            }) 
            if update_data:
                return update_data   
        except Exception as org:
            print("coming")
            print(org)

    def vehciledata(self,search_key,search_value,update_key,update_value,database,collection_name):
        try:
            db_name=db[database]
            collection=db_name[collection_name]
            vehciledata=collection.update_one({
                search_key: search_value
            }, {
                '$set': {
                    update_key: update_value
                }
            }) 
            if vehciledata:
                return vehciledata  
        except Exception as org:
            print("coming")
            print(org)     


    def vehcileupdate(self,search_key,search_value,update_key, update_value,update_key1,update_value1,update_key2,update_value2,database,collection_name):
        try:
            db_name=db[database]
            collection=db_name[collection_name]
            vehcileupdate=collection.update_one({
                search_key: search_value
            }, {
                '$set': {
                     update_key: update_value,
                     update_key1: update_value1,
                     update_key2: update_value2
                }
            }) 
            if vehcileupdate:
                return vehcileupdate  
        except Exception as org:
            print("coming")
            print(org)                  
     

    def mapupdate(self,search_key,search_value,update_key, update_value,update_key1,update_value1,database,collection_name):
        try:
            db_name=db[database]
            collection=db_name[collection_name]
            mapupdate=collection.update_many({
                search_key: search_value
            }, {
                '$set': {
                     update_key: update_value,
                     update_key1: update_value1
                   
                }
            }) 
            if mapupdate:
                return mapupdate  
        except Exception as org:
            print("coming")
            print(org)                  
 






  



  
    
      
        
    
