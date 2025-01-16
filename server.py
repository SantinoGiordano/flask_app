# to run make sure you cd server
# to run client, cd .. , then cd client
# while in flask_app run .\env\Scripts\Activate.ps1 to activate enviorment
#cors has issue with 5000
from flask import Flask, jsonify 
from flask_cors import CORS
app = Flask(__name__)

# Run: python server.py , and go to localhost:(number)'/api/home' == num run dev
@app.route('/api/home', methods=['GET'])
def return_home():
    return jsonify({
        'message':'Hello World from the backend'
    })


if __name__ == '__main__':
    app.run(debug=True,port=8080)