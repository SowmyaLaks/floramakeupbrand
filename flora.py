from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from pymongo import MongoClient
uri = "mongodb+srv://sowmyasista99:kOFwcDT5rCL5p4er@cluster0.6jwxpok.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client.flora_db
@app.route('/')
def home():
  return render_template('flora.html')
@app.route('/flora', methods = ['POST'])
def save_data():
    name = request.form['Product_name']
    quantity = request.form['Quantity']
    print(name,quantity)
    db.flora_orders.insert_one({
        'Product_name':name,
        'Quantity':quantity
    })
    return jsonify({'msg':'items added to cart successfully!'})
@app.route('/flora', methods = ['GET'])
def get_data():
    orders = list(db.flora_orders.find({},{'_id':False}))
    return jsonify({'orders': orders})
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)