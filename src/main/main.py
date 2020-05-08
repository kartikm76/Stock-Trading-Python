# import json
# import werkzeug
# werkzeug.cached_property = werkzeug.utils.cached_property
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from flask_restplus import fields, Api, Resource
from utils.db_connect import Database

from utils.server import server
from controller import contoller

# app = Flask(__name__)
# api = Api(app=app)
# CORS(app)
# ns_conf = api.namespace('api', description = 'Stock Trading Application')

if __name__ == '__main__':
    Database.initialize_connection_pool()
    #app.run(debug=True)
    server.run()