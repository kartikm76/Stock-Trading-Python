from enum import Enum
from flask_restplus import fields, Api, Resource
from utils.server import server

class Trade:    
    trade = server.api.model('Trade Execution', {
                    'stock_id': fields.Integer(description='Stock id'),
                    'stock_name': fields.String(required=True, enum=['DRAFT', 'PUBLISHED', 'DELETED']),
                    'stock_qty' : fields.Integer(required=True),
        })
    