

from flask_restplus import Api,Resource
from flask import Flask, jsonify, request
from flask import Flask, render_template, request, session
from flask_session import Session
from App.FleetApi import api
from App.DataBase import BaseMongo
from App.DataBase.Test_suite import TestSuite
from flask_cors import CORS
import json
from App.FleetApi.uservalidation import User
from App.FleetApi.create_otp import otp
import smtplib

test_obj=TestSuite()
valid=User()

@api.route("/forgotpassword")
class forgotpassword(Resource):
    def post(self):
        try:
            data = request.get_json()
            print(data)
            session['email'] = data["email"]    
      
            userdata=test_obj.userdata(imp=data["email"],imps="Email")
            print(userdata)
       
            if not valid.check(session['email']):
                 return jsonify({"error":True,"msg":" please enter valid email"})
               
            elif userdata:
                server=smtplib.SMTP('smtp.gmail.com','587')
                server.starttls()
                server.login('xsatyammishra2019@gmail.com','Satyam@123')
                msg=otp
                server.sendmail('xsatyammishra2019@gmail.com',session['email'],msg)
                server.quit() 
                return jsonify({"error":False,"msg":"otp send suceesfully in your email account"})

        except Exception as org:
            error="ERROR:"+str(org)
            print(error)
            return str(error)

     
             
            
        
        