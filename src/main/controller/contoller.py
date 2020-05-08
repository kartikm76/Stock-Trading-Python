from flask import Flask, request, jsonify
from flask_restplus import fields, Api, Resource

from service.stock_service import StockService
from service.user_service import UserService
from service.account_service import AccountService
from service.user_account_service import UserAccountService
from service.stock_holding_service import StockHoldingService
from service.trade_activity_service import TradeActivityService
from service.execute_trade_service import ExecuteTradeService
from service.account_balance_service import AccountBalanceService
from model.trade import Trade
from utils.server import server

@server.ns_conf.route("/stocks-list/<id>", methods=["GET"])
class StockDetails(Resource):
    def get(self, id):
        return jsonify(StockService().get_stock_details(id))

@server.ns_conf.route("/stocks-list/all", methods=["GET"])
class StocksDetails(Resource):
    def get(self):        
        return jsonify(StockService().get_stock_details())


@server.ns_conf.route("/user/<id>", methods=["GET"])
class UserDetails(Resource):
    def get(self, id):
        return jsonify(UserService().get_user_details(id))        

@server.ns_conf.route("/all-users", methods=["GET"])
class UsersDetails(Resource):
    def get(self):        
        return jsonify(UserService().get_user_details())

@server.ns_conf.route("/account/<id>", methods=["GET"])
class AccountDetails(Resource):
    def get(self, id):
        return jsonify(AccountService().get_account_details(id))

@server.ns_conf.route("/user-account/user/<id>", methods=["GET"])
class UserAccountByUserId(Resource):
    def get(self, id):
        return jsonify(UserAccountService().get_user_account("USER", id))

@server.ns_conf.route("/user-account/account/<id>", methods=["GET"])
class UserAccountByAccountId(Resource):
    def get(self, id):
        return jsonify(UserAccountService().get_user_account("ACCOUNT", id))

@server.ns_conf.route("/holding/user/<id>", methods=["GET"])
class StockHoldingDetails(Resource):
    def get(self, id):
        return jsonify(StockHoldingService().get_stock_holding("USER", id))

@server.ns_conf.route("/holding/account/<id>", methods=["GET"])
class StockHoldingDetails(Resource):
    def get(self, id):
        return jsonify(StockHoldingService().get_stock_holding("ACCOUNT", id))

@server.ns_conf.route("/holding/all", methods=["GET"])
class StockHoldingDetailsAll(Resource):
    def get(self):
        return jsonify(StockHoldingService().get_stock_holding())
        

@server.ns_conf.route("/trade-activity/<id>", methods=["GET"])
class TradeActivity(Resource):
    def get(self, id):
        return jsonify(TradeActivityService().get_trade_activity(id))

@server.ns_conf.route("/trade-activity/all", methods=["GET"])
class TradeActivityAll(Resource):
    def get(self):        
        return jsonify(TradeActivityService().get_trade_activity())

@server.ns_conf.route("/account-balance/<id>", methods=["GET"])
class AccountBalance(Resource):
    def get(self, id):
        return jsonify(AccountBalanceService().get_account_balance(id))

@server.ns_conf.route("/account-balance/all", methods=["GET"])
class AccountBalanceAll(Resource):
    def get(self):
        return jsonify(AccountBalanceService().get_account_balance())

@server.ns_conf.route("/execute-trade", methods=["POST"])
class ExecuteTrade(Resource):
    @server.api.response(201, 'Trade executed succesfully.')
    @server.api.expect(Trade.trade, validate=True)
    def post(self):
        # data = request.json
        # return save_new_user(data=data)
        return jsonify(ExecuteTradeService().manage_stock_holding(request.json))