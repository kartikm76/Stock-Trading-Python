from flask import Flask
from service.get_stock_holding import GetStockHolding

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/Guruji')
def index():
   #cur = mysql.connection.cursor()
   #cur.execute('''SELECT * FROM Users WHERE id=1''')
   #row_headers=[x[0] for x in cur.description] #this will extract row headers
    
   get_data = GetStockHolding()
   records = get_data.get_stock_holding()
  
   row_headers=[x[0] for x in records.headers] #this will extract row headers
   #rv = cur.fetchall()
   json_data=[]
   for result in records:
        json_data.append(dict(zip(row_headers,result)))
   return json.dumps(json_data)

if __name__ == '__main__':
   app.run(debug=True)

if __name__ == '__main__':
    app.run()