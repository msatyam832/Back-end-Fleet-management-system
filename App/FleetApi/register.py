

from flask_restplus import Api,Resource
from flask import Flask, jsonify, request
from flask import Flask, render_template, request, session
from flask_session import Session
from App.FleetApi import api
from App.DataBase.BaseMongo import BaseMongo
from App.DataBase.Test_suite import TestSuite

from flask_cors import CORS
from flask_bcrypt import Bcrypt
from App.FleetApi.create_otp import otp
from App.FleetApi.uservalidation import User
import json
import smtplib

bcrypt = Bcrypt()
valid =User()
test_obj=TestSuite()

@api.route("/register")
class Register(Resource):
    def put(self):
        try:
            data = request.get_json()  
            session['password'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')
            session['email'] = data["email"]
            userdata=test_obj.userdata(imp=data["email"],imps="Email")
              
          

            if not valid.check(session['email']):
                return jsonify({"error":True,"msg":" please enter valid email"})
            elif userdata:
                return jsonify({"error":True,"msg":"email is already exist"})
            else:
                server=smtplib.SMTP('smtp.gmail.com','587')
                server.starttls()
                server.login('xsatyammishra2019@gmail.com','Satyam@123')
                msg=otp
                server.sendmail('xsatyammishra2019@gmail.com',session['email'],msg)
                server.quit() 
                return jsonify({"error":False,"msg":"otp send suceesfully in your email account"})

        except Exception as org:
            error="error:"+str(org)
            print(error)
            return str(error)
            

    
     
             
        