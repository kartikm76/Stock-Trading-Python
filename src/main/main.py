import json
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restplus import fields, Api, Resource
from utils.db_connect import Database
from service.user_service import UserService
from service.account_service import AccountService
from service.user_account_service import UserAccountService
from service.stock_holding_service import StockHoldingService
from service.trade_activity_service import TradeActivityService
from service.execute_trade_service import ExecuteTradeService

from utils.object_serialize import SerializeObject

app = Flask(__name__)
api = Api(app=app)
CORS(app)
ns_conf = api.namespace('api', description = 'Stock Trading Application')

@ns_conf.route("/user/<id>", methods=["GET"])
class UserDetails(Resource):
    def get(self, id):
        return UserService().get_user_details(id)
        #return json.dumps(UserMaster().get_user_details(id), default = SerializeObject.serialize_object, sort_keys=True, indent=4)

@ns_conf.route("/all-users", methods=["GET"])
class UsersDetails(Resource):
    def get(self):
        #response = jsonify(UserService().get_user_details())
        #response.headers.add('Access-Control-Allow-Origin', '*')
        #return response
        return UserService().get_user_details()

@ns_conf.route("/account/<id>", methods=["GET"])
class AccountDetails(Resource):
    def get(self, id):
        return AccountService().get_account_details(id)

@ns_conf.route("/user-account/user/<id>", methods=["GET"])
class UserAccountByUserId(Resource):
    def get(self, id):
        return UserAccountService().get_user_account("USER", id)

@ns_conf.route("/user-account/account/<id>", methods=["GET"])
class UserAccountByAccountId(Resource):
    def get(self, id):
        return UserAccountService().get_user_account("ACCOUNT", id)

@ns_conf.route("/holding/user/<id>", methods=["GET"])
class StockHoldingDetails(Resource):
    def get(self, id):
        return StockHoldingService().get_stock_holding("USER", id)

@ns_conf.route("/holding/account/<id>", methods=["GET"])
class StockHoldingDetails(Resource):
    def get(self, id):
        return StockHoldingService().get_stock_holding("ACCOUNT", id)

blog_post = api.model('Blog post', {
                'id': fields.Integer(description='The unique identifier of a blog post'),
                'title': fields.String(required=True, description='Article title'),
                'body': fields.String(required=True, description='Article content'),
                'status': fields.String(required=True, enum=['DRAFT', 'PUBLISHED', 'DELETED']),
                'pub_date': fields.DateTime,
})

@ns_conf.route("/execute-trade", methods=["POST"])
class ExecuteTrade(Resource):
    @api.response(201, 'Blog post successfully created.')
    @api.expect(blog_post)
    def post(self):
        #return ExecuteTradeService().manage_stock_holding()
        return jsonify(ExecuteTradeService().manage_stock_holding(request.get_json()))

@ns_conf.route("/trade-activity/<id>", methods=["GET"])
class TradeActivity(Resource):
    def get(self, id):
        return TradeActivityService().get_trade_activity(id)

if __name__ == '__main__':
    Database.initialize_connection_pool()
    app.run(debug=True)
