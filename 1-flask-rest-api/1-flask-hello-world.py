#!/usr/bin/env python3

from flask import Flask ,jsonify ,abort , make_response ,request

app = Flask(__name__)

''' First Example '''
@app.route('/') # index route
def index():
    return "Hello world!"

if __name__ == '__main__':
    app.run(debug=True)
