from flask import Flask
import requests


URL = 'helloworld-backend-service'

app = Flask(__name__)

def call_back_end_service():
    resp = requests.get('http://'+URL+':5002', verify=False)
    if resp.status_code == 200:
        response = resp.content
    else:
        response = 'Fail'
    return response

@app.route("/", methods=['GET'])
def hello():
    return call_back_end_service()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="80")