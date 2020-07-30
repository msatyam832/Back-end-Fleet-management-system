from flask import *
from flask_restplus import Api
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_claims
)
app = Flask(__name__)


api=Api(app)
app.secret_key="ranbmsjhnmcdsbcb"
jwt = JWTManager(app)
CORS(app)

from App.FleetApi import register
from App.FleetApi import otp
from App.FleetApi import login
from App.FleetApi import forgotpassword
from App.FleetApi import updatepassword  
from App.FleetApi import vehicles 
from App.FleetApi import vehiclereg 
from App.FleetApi import updatevehcile
from App.FleetApi import  map
from App.FleetApi import getmap
from App.FleetApi import updatemap

