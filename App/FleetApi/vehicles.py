
from flask_restplus import Api,Resource
from flask import Flask, jsonify, request
from flask import Flask, render_template, request, session
from App.FleetApi import api
from App.DataBase import BaseMongo
from App.DataBase.Test_suite import TestSuite
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from App.DataBase.vehcile_info import TestSuites
from bson.json_util import dumps,loads
from App.FleetApi.login import jwt_required

import json



bcrypt = Bcrypt()

test_obj=TestSuite()
test=TestSuites()
@api.route("/vehicles")
class vehicles(Resource):
    @jwt_required
    def put(self):
        try:
            postedData = request.get_json()
            session['device_id']=postedData['device_id'] 
            vehciledata=test.vehicle_details(vkey="device_id",vvalue=session['device_id']) 
            if vehciledata:
                updatev=test_obj.updatedata(searchvalue=session['email'],searchkey="Email",updatekey="device_id",updatevalue=session['device_id'])
                if updatev:
                    return jsonify({"vehcile details":[{"Device Id":vehciledata['device_id'],"Vehcile model":vehciledata['vehicle_model'],"Vehcile registeration number":vehciledata['vehicle_registeration_no'],"Owner name":vehciledata['owner_name']}]})       
            else:
                return jsonify({"msg":"error"})  

        except Exception as org:
            error="error:"+str(org)
            print(error)
            return str(error)         
              


          

            








                 


           







  
        

          
            



