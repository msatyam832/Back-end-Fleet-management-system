
from flask import Flask, jsonify, request
from flask_restplus import Api,Resource
from flask import Flask, render_template, request, session
from App.FleetApi import api
from App.DataBase import BaseMongo
from App.DataBase.Test_suite import TestSuite
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_session import Session
import json
from App.FleetApi.uservalidation import User

secret_key="ranbmsjhb"
bcrypt = Bcrypt()
from App.FleetApi.create_otp import otp

valid=User()
test=TestSuite()

@api.route("/updatepassword")
class updatepassword(Resource):
    def post(self):
        try:
            postedData = request.get_json() 
            verifyotp =postedData["verifyotp"]
            password = bcrypt.generate_password_hash(postedData['password']).decode('utf-8')
        

        
            if valid.Validateotp(verifyotp):
                 test.updatedata(searchvalue=session['email'],searchkey="Email",updatekey="password",updatevalue=password)
                 return jsonify({"error":False,"msg":"password update scucessfully"})
           
            else:
                return jsonify({"error":True,"msg":"wrong otp"})

            
        except Exception as org:
            error="error:"+str(org)
            print(error)
            return str(error)

           
               

            








                 


           







  
        

          
            



