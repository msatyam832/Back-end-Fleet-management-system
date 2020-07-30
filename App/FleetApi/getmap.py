

from flask_restplus import Api,Resource
from flask import Flask, jsonify, request
from flask import Flask, render_template, request, session
from flask_session import Session
from App.FleetApi import api
from App.DataBase.BaseMongo import BaseMongo
from App.DataBase.Test_suite import TestSuite
from App.DataBase.vehcile_info import TestSuites
from App.FleetApi.vehicles import vehicles
from App.DataBase.map import Mapdata
from App.FleetApi.login import login

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
mapinfo=Mapdata()
logininfo=login()

@api.route("/getmap")
class getmap(Resource):
    def post(self):
         try:
              vehicledata=mapinfo.map_details(vkey="device_id",vvalue=session['device_id'])
         
              if vehicledata:
                    return jsonify({"Longitude":vehicledata['Longitude'],'Lattitude':vehicledata['Lattitude']}) 
       
              else:
                   return jsonify({"msg":"incorrect device  id"})     
      
         except Exception as org:
               error="ERROR:"+str(org)
               print(error)
               return str(error)
              

              
                   

           

           
        
        
        

    
     
             