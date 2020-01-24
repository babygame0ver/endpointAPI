#!/usr/bin/env python3
from flask import Flask ,jsonify ,abort , make_response ,request
from datetime import datetime

app = Flask(__name__)


class endpointAPI(object):
    """docstring for ."""

    def __init__(self, payloads):
        self.payloads = payloads

    def Index(self):
        return 'Hello world'

    def json(self):
        return jsonify(self.payloads)

    def GitHubCallBack(self):
        result = ''
        for index,key in enumerate(request.headers,start=1):
              result += '{}. {} <br>'.format(index,key)
        return '{} - {}'.format(result,request.get_json())

    def TwitterCallBack(self):
        return 'TwitterCallBack'

    def showParamtersFromURl(self,id):
        return '{} is the paramter in URL'.format(id)

payloads = [{'id' : 1, 'title' : u'hacker'},{'id' : 2,'title' : u'developer'}]
api = endpointAPI(payloads)

@app.route('/',methods=['GET'])
def index():
    return api.Index()

@app.route('/json',methods=['GET'])
def json():
    return api.json()

@app.route('/githubcallback',methods=['GET','POST'])
def GitHubCallBack():
    return api.GitHubCallBack()

@app.route('/twittercallBack',methods=['GET','POST'])
def TwitterCallBack():
    return api.TwitterCallBack()

@app.route('/urlparam/<int:api_id>',methods=['GET'])
def showParamtersFromURl(api_id):
    return api.showParamtersFromURl(api_id)

if __name__ == '__main__':
    app.run(debug=True)
