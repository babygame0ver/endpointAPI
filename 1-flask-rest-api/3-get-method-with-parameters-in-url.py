#!/usr/bin/env python3

from flask import Flask,jsonify ,abort ,make_response

app = Flask(__name__)

''' Third Example '''
payloads = [
        {
            'id' : '1'
        }
]

@app.route('/restapi/<int:api_id>',methods=['GET'])
def rest_api_with_id(api_id):
    print(type(api_id))
    if((api_id)%2 == 0):
        abort(404,str(api_id))
    payloads[0]['id'] = api_id # changing id from web
    return jsonify(payloads)

@app.errorhandler(404)
def not_found(error): # custom message
    item = error.description
    return make_response(jsonify({'error':'{} not found baby'.format(item)}),404)

if __name__ == '__main__':
    app.run(debug=True)
