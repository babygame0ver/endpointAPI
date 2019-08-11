#!/usr/bin/env python3

from flask import Flask ,jsonify ,abort , make_response ,request

app = Flask(__name__)


''' Fourth Example '''

payloads = [{'id':6}]

@app.route('/restapi/create',methods=['GET','POST'])
def create_task_with_id():
    print(request.json,request.headers)
    if request.method == "GET":
        payloads[0]['id'] = "GET"
        return jsonify(payloads,200) # success
    else: # post method
        if not request.json or not 'task_id' in request.json:
            abort(400) # go to not found function
        payloads[0]['id'] = request.json['task_id'] * 2 # getting data from headers
        return jsonify(payloads,201) #201 ->created

@app.errorhandler(400) # can be used when there is POST request available but client is asking for GET
def not_found_(error):
    return make_response(jsonify({'error':'bad request baby'}),400)


if __name__ == '__main__':
    app.run(debug=True)
