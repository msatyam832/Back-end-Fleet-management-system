

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


@api.route("/map/Long=<long>/Lat=<lat>")
class map(Resource):
    def post(self,long,lat):
         try:
              vehicledata=mapinfo.inseted_map_data({"Longitude":long,"Lattitude":lat,"device_id":session['device_id']})
              if vehicledata:
                   return jsonify({"Longitude":long,"Lattitude":lat}) 
         except  Exception as org:
            error="ERROR:"+str(org)
            print(error)
            return str(error)

          
           

           
              
        
        
        

    
     
             