from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello There!!</h1>"


@app.route('/login', methods=['post'])
def login():
    print(request.form.items())
    for k, v in request.form.items():
        print(k, '---', v)

    return "<h1>Hello There {0} login!!</h1>".format(request.form.get("username",""))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
