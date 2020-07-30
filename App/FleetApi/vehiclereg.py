

from flask_restplus import Api,Resource
from flask import Flask, jsonify, request
from flask import Flask, render_template, request, session
from flask_session import Session
from App.FleetApi import api
from App.DataBase.BaseMongo import BaseMongo
from App.DataBase.Test_suite import TestSuite
from App.DataBase.vehcile_info import TestSuites

from flask_cors import CORS
from flask_bcrypt import Bcrypt
from App.FleetApi.create_otp import otp
from App.FleetApi.uservalidation import User
import json
import smtplib

bcrypt = Bcrypt()
valid =User()
test_obj=TestSuite()
test=TestSuites()

@api.route("/vehiclereg")
class vechilereg(Resource):
    def put(self):
        try:
            postedData = request.get_json() 
            device_id =postedData["device_id"]
            owner_name=postedData["owner_name"]
            vehicle_model=postedData['vehicle_model']
            vehicle_registeration_no=postedData['vehicle_registeration_no']
        

            vehicledata=test.vehicle_Registeration({"device_id": device_id,"owner_name": owner_name,"vehicle_model":vehicle_model,"vehicle_registeration_no":vehicle_registeration_no})

            if vehicledata:
                return jsonify({"msg":"sucessfully updated"})
      
            else:
                return jsonify({"msg":"not inserted"})
        except Exception as org:
            error="error:"+str(org)
            print(error)
            return str(error) 
                      

           
            
        
        
        

    
     
             