from crypt import methods
from urllib import response, request
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

print('starting...................')

@app.route('/')
def index():

  url = 'https://loadshedding.eskom.co.za/Loadshedding/GetStatus/'

  try:
    
    response = request.urlopen(url)
    print('response: ', response)
    data = response.read()
    print(f'returning {data.decode()}')

    return jsonify({'data': str(data.decode())})
  
  except Exception as err:
    return app.make_response({'somerr': err})
  
app.run(host='0.0.0.0', port=8000, debug=True)
