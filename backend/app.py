from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def get_home():
    return "simple page"

@app.route('/api/data',methods=['GET'])
def get_data():
    data = {
        "message":"This is my first application"
    }
    return jsonify(data)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
            