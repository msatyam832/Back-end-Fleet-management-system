
from flask import Flask, jsonify, request
from flask_restplus import Api,Resource
from flask import Flask, render_template, request, session
from flask_session import Session
from App.FleetApi import api
from App.DataBase import BaseMongo
from App.DataBase.Test_suite import TestSuite
from App.DataBase.vehcile_info import TestSuites
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_claims
)
import re 
import json

test_obj=TestSuite()
test=TestSuites()

bcrypt = Bcrypt()


@api.route("/login")
class login(Resource):
    def post(self):
        try:
             postedData = request.get_json()
             session['password'] = postedData['password']
             session['email'] = postedData["email"]
             res =''         
        
             userdata=test_obj.userdata(imp=session['email'],imps="Email")
        except  Exception as org:
            error="ERROR:"+str(org)
            print(error)
            return str(error)
           
       
       
        if userdata:

            if bcrypt.check_password_hash(userdata['password'],session['password']):
                access_token = create_access_token(identity = { 'email': userdata['Email']})
                try:

                    vehciledata=test.vehicle_details(vkey='device_id',vvalue=userdata['device_id'])
                    if vehciledata:
                        res = jsonify({"Error":False,"status":200,"token":access_token,'email': userdata['Email'],"vehcile details":[{"Device Id":vehciledata['device_id'],"Vehcile model":vehciledata['vehicle_model'],"Vehcile registeration number":vehciledata['vehicle_registeration_no'],"Owner name":vehciledata['owner_name']}] })
                        session['device_id']=vehciledata['device_id']
                        return res 
                                                
                except Exception as org:
                    print("vechile dataa")
                    print(org)
                    res=jsonify({"Error":False,"status":200,"token":access_token,'email': userdata['Email'] })
                    return res       
                       
            else:

                res = jsonify({"error":True,"status":"300","message":"Invalid username and password"}) 
                return res 
        else:
            res = jsonify({"error":True,"status":"301","message": "Invalid username and password"})  
            return res

        







                 


           







  
        

          
            



