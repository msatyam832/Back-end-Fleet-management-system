

from App.DataBase import BaseMongo
class TestSuite(BaseMongo.BaseMongo):
    def userdata(self,imp,imps):
        try:
            userdataa=self.find_data(key=imps,value=imp,database=self.getdatabase(),collection_name=self.getregister_collection())
            return userdataa   
        except Exception as org:
            print(org)
            return False
        
    def insert_register_data(self,data):
        try:
            print(data)
            register_collection=self.insert_data(data,self.getdatabase(),self.getregister_collection())
            if register_collection:
                return register_collection
        except Exception as org:
            print(org)
            return False
      
    def updatedata(self ,searchvalue,searchkey,updatekey,updatevalue):
        try:
            updateusedata=self.update_data(search_key=searchkey,search_value=searchvalue,update_key=updatekey,update_value=updatevalue,database=self.getdatabase(),collection_name=self.getregister_collection())
            return updateusedata 
        except Exception as org:
            print(org)
            return False      
        

    def vehicledataaa(self ,updatekey,updatevalue,searchkey,searchvalue):
        try:
             vehicelusedata=self.vehciledata(search_key=searchkey,search_value=searchvalue,update_key=updatekey,update_value=updatevalue,database=self.getdatabase(),collection_name=self.getvehicles_collection())
             return vehicelusedata
        except Exception as org:
            print(org)
            return False     

       


   


          
    

   
               
            