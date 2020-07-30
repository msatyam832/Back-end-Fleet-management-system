
from flask_restplus import Api,Resource
from App.FleetApi import api
import re 
import json
from App.FleetApi.create_otp import otp


regex = r"(^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$)"

class User:
    def Validateotp(self,verifyotp):
     if otp == verifyotp:
        return True
     else:
         False

    def check(self,email): 
        if(re.search(regex,email)):
             return True
        else:
            return False
       
 
    
       
     

