from App.DataBase import BaseMongo
class Mapdata(BaseMongo.BaseMongo):
    def inseted_map_data(self,data):
        try:
            print(data)
            mapdata=self.insert_data(data,self.getdatabase(),self.getmap_collection())
            if mapdata:
                return mapdata
        except Exception as org:
            print(org)
            return False  



    def map_details(self,vkey,vvalue):

        try:
             details =self.find_data(key=vkey,value=vvalue,database=self.getdatabase(),collection_name=self.getmap_collection())    
             if details:
                 return details
        except Exception as org:
            print(org)
            print("mishra")
            return False  


    def mapupdatedata(self,searchkey,searchvalue,updatekey,updatevalue,updatekey1,updatevalue1,):
        
        try:
            mapupdat=self.mapupdate(search_key=searchkey,search_value=searchvalue,update_key=updatekey,update_value=updatevalue,update_key1=updatekey1,update_value1=updatevalue1,database=self.getdatabase(),collection_name= self.getmap_collection())  
            if mapupdat:
                return mapupdat  
        except Exception as org:
            print(org) 
            return False          