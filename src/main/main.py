import json
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restplus import fields, Api, Resource
from utils.db_connect import Database
from service.stock_service import StockService
from service.user_service import UserService
from service.account_service import AccountService
from service.user_account_service import UserAccountService
from service.stock_holding_service import StockHoldingService
from service.trade_activity_service import TradeActivityService
from service.execute_trade_service import ExecuteTradeService
from service.account_balance_service import AccountBalanceService
from utils.object_serialize import SerializeObject

app = Flask(__name__)
api = Api(app=app)
CORS(app)
ns_conf = api.namespace('api', description = 'Stock Trading Application')

@ns_conf.route("/stocks-list/<id>", methods=["GET"])
class StockDetails(Resource):
    def get(self, id):
        return jsonify(StockService().get_stock_details(id))

@ns_conf.route("/stocks-list/all", methods=["GET"])
class StocksDetails(Resource):
    def get(self):        
        return jsonify(StockService().get_stock_details())


@ns_conf.route("/user/<id>", methods=["GET"])
class UserDetails(Resource):
    def get(self, id):
        return jsonify(UserService().get_user_details(id))        

@ns_conf.route("/all-users", methods=["GET"])
class UsersDetails(Resource):
    def get(self):        
        return jsonify(UserService().get_user_details())

@ns_conf.route("/account/<id>", methods=["GET"])
class AccountDetails(Resource):
    def get(self, id):
        return jsonify(AccountService().get_account_details(id))

@ns_conf.route("/user-account/user/<id>", methods=["GET"])
class UserAccountByUserId(Resource):
    def get(self, id):
        return jsonify(UserAccountService().get_user_account("USER", id))

@ns_conf.route("/user-account/account/<id>", methods=["GET"])
class UserAccountByAccountId(Resource):
    def get(self, id):
        return jsonify(UserAccountService().get_user_account("ACCOUNT", id))

@ns_conf.route("/holding/user/<id>", methods=["GET"])
class StockHoldingDetails(Resource):
    def get(self, id):
        return jsonify(StockHoldingService().get_stock_holding("USER", id))

@ns_conf.route("/holding/account/<id>", methods=["GET"])
class StockHoldingDetails(Resource):
    def get(self, id):
        return jsonify(StockHoldingService().get_stock_holding("ACCOUNT", id))

@ns_conf.route("/holding/all", methods=["GET"])
class StockHoldingDetailsAll(Resource):
    def get(self):
        return jsonify(StockHoldingService().get_stock_holding())

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
        return jsonify(ExecuteTradeService().manage_stock_holding(request.get_json()))

@ns_conf.route("/trade-activity/<id>", methods=["GET"])
class TradeActivity(Resource):
    def get(self, id):
        return jsonify(TradeActivityService().get_trade_activity(id))

@ns_conf.route("/trade-activity/all", methods=["GET"])
class TradeActivityAll(Resource):
    def get(self):        
        return jsonify(TradeActivityService().get_trade_activity())

@ns_conf.route("/account-balance/<id>", methods=["GET"])
class AccountBalance(Resource):
    def get(self, id):
        return jsonify(AccountBalanceService().get_account_balance(id))

@ns_conf.route("/account-balance/all", methods=["GET"])
class AccountBalanceAll(Resource):
    def get(self):
        return jsonify(AccountBalanceService().get_account_balance())

if __name__ == '__main__':
    Database.initialize_connection_pool()
    app.run(debug=True)
