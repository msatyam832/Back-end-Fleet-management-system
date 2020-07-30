

from flask_restplus import Api,Resource
from flask import Flask, jsonify, request
from flask import Flask, render_template, request, session
from flask_session import Session
from App.FleetApi import api
from App.DataBase.BaseMongo import BaseMongo
from App.DataBase.Test_suite import TestSuite
from App.DataBase.vehcile_info import TestSuites
from App.FleetApi.vehicles import vehicles
from App.FleetApi.login import login
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

   


@api.route("/updatemap/Long=<long>/Lat=<lat>/device_id=<device_id>")
class updatemap(Resource):
    def post(self,long,lat,device_id):
            try:

                    if device_id == session['device_id']:
                            vehicledata=mapinfo.mapupdatedata(searchvalue=device_id,searchkey="device_id",updatekey="Longitude",updatevalue=long,updatekey1="Lattitude",updatevalue1=lat)
                            if vehicledata:
                                    return jsonify({"Longitude":long,"Lattitude":lat,"msg":"update scuceefully"}) 
                            else:

                                     return  jsonify({"msg":"not updated"})         
                          
                    else:
                            return jsonify({"msg":"not verified device_id"}) 

                                
       
            except Exception as org:
                      error="error:"+str(org)
                      print(error)
                      return str(error)

                  
               
                
           

                        
                          
                             
                                       
           
                          

            
      
