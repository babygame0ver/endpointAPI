#!/usr/bin/env python3
from flask import Flask ,jsonify ,abort , make_response ,request , render_template
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
        post_data = ''
        get_data = ''
        if(request.method == 'POST'):
            post_data = request.get_json()
        elif(request.method == 'GET'):
            get_data = request.args
        return render_template('githubcallback.html',headers=request.headers,get_data=get_data,post_data=post_data)

    def TwitterCallBack(self):
        return 'TwitterCallBack'

    def showParamtersFromURl(self,id):
        return '{} is the paramter in URL'.format(id)

    def getOAuthAccessToken(self):
        print('getOAuthAccessToken')
        return 'getOAuthAccessToken'

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
    print(request.get_json())
    return api.GitHubCallBack()

@app.route('/twittercallBack',methods=['GET','POST'])
def TwitterCallBack():
    return api.TwitterCallBack()

@app.route('/urlparam/<int:api_id>',methods=['GET'])
def showParamtersFromURl(api_id):
    return api.showParamtersFromURl(api_id)

@app.route('/getOAuthAccessToken',methods=['GET'])
def getOAuthAccessToken():
    return api.getOAuthAccessToken()


if __name__ == '__main__':
    app.run(debug=True)
