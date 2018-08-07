from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(ost="0.0.0.0", port=int("80"), debug=False)