from flask import Flask
from api_v1 import initAPI

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!    gl quoted'


initAPI(app)

if __name__ == '__main__':
    app.run(debug=True)
