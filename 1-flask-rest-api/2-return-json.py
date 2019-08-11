#!/usr/bin/env python3

from flask import Flask,jsonify

app = Flask(__name__)

''' Second Example '''
payloads = [
    {   'id' : 1,
        'title' : u'hacker'
    },
    {   'id' : 2,
        'title' : u'developer'
    }
]

@app.route('/restapi',methods=['GET'])
def rest_api():
    return jsonify(payloads)


if __name__ == '__main__':
    app.run(debug=True)
