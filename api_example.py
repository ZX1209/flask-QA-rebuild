from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app, prefix='/api/v1')


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)