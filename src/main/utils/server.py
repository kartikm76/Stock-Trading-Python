import json
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask_cors import CORS
#from flask_restplus import fields, Api, Resource
from flask import Flask, request
from flask_restplus import Api

class Server(object):
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api( self.app,
                        version='1.0'                       
                    )
        CORS(self.app)
        self.ns_conf = self.api.namespace('api', description = 'Stock Trading Application')

    def run(self):
        self.app.run()
                #debug = environment_config["debug"], 
                #port = environment_config["port"]
            
server = Server()
