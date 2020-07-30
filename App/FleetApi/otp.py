

from flask_restplus import Api,Resource
from flask import Flask, jsonify, request
from flask import Flask, render_template, request, session
from flask_session import Session
from App.FleetApi import api
from App.DataBase import BaseMongo
from App.DataBase.Test_suite import TestSuite
from bson.objectid import ObjectId
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
import json
import smtplib
from App.FleetApi.uservalidation import User
 
test_obj=TestSuite()    
valid =User()      
@api.route("/otp")
class Otp(Resource):
    def post(self):
        try:
            postedData=request.get_json()
            verifyotp =postedData["verifyotp"]
            created = datetime.utcnow()
        
            if valid.Validateotp(verifyotp):
                insert_data=test_obj.insert_register_data({"password": session['password'],"Email": session['email'],'created' : created})
           
                print(insert_data)
                server=smtplib.SMTP('smtp.gmail.com','587')
                server.starttls()
                server.login('xsatyammishra2019@gmail.com','Satyam@123')
                msg="welcome to fleet management system"
                server.sendmail('xsatyammishra2019@gmail.com',session['email'],msg)
                server.quit()
                return jsonify ({"status": 200,"error":False,"msg": "You successfully signed up for the fleet management system"}) 
            else:
                return jsonify({"status":"wrong otp"})     


        except Exception as org:
            error="ERROR:"+str(org)
            print(error)
            return str(error)


            