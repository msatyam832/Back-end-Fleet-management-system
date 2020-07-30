

from App.DataBase import BaseMongo
class TestSuites(BaseMongo.BaseMongo):
      

    def vehicle_details(self,vkey,vvalue):

        try:
             details =self.find_data(key=vkey,value=vvalue,database=self.getdatabase(),collection_name=self.getvehicles_collection())    
             if details:
                 return details
        except Exception as org:
            print(org)
            print("mishra")
            return False
           
           
    
    def vehicle_Registeration(self,data):
        try:
            print(data)
            vehicles_collection=self.insert_data(data,self.getdatabase(),self.getvehicles_collection())
            if vehicles_collection:
                return vehicles_collection
        except Exception as org:
            print(org)
            return False  

    def vehcileupdatedata(self,searchkey,searchvalue,updatekey,updatevalue,updatekey1,updatevalue1,updatekey2,updatevalue2):
        
        try:
            vehiclesupdat=self.vehcileupdate(search_key=searchkey,search_value=searchvalue,update_key=updatekey,update_value=updatevalue,update_key1=updatekey1,update_value1=updatevalue1,update_key2=updatekey2,update_value2=updatevalue2 ,database=self.getdatabase(),collection_name= self.getvehicles_collection())  
            if vehiclesupdat:
                return vehiclesupdat  
        except Exception as org:
            print(org) 
            return False          

    
                 



   
   


          
    

   
               
            