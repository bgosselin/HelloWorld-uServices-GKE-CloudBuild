from flask import Flask

app = Flask(__name__)

def call_back_end_service():
    return 'hello world'

@app.route("/", methods=['GET'])
def hello():
    return call_back_end_service()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5002"), debug=False)