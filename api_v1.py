from flask_restful import Resource, Api, reqparse
from peewee_db_class import *


class UserRes(Resource):

    def get(self):
        return None


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


class QuestionsRes(Resource):

    def __init__(self):
        """__init__
        """
        self.parser = reqparse.RequestParser(
            bundle_errors=True)  # bundle_errors for send errors toghter
        self.parser.add_argument('keyword', type=str, help='search keyword')

    def get(self):
        args = self.parser.parse_args(
            strict=True)  # strict for not allowing other unrelated arguments

        response = Question.select().where(
            Question.title % f"*{args['keyword']}*"
        )  # sqlite use * reprent other things while mysql use %

        tmpr = [(q.id, q.title) for q in response]

        return tmpr


class QuestionRes(Resource):

    def get(self, questionId):
        return questionId


def initAPI(app):
    """initAPI
    """

    api = Api(app, prefix='/api/v1')

    api.add_resource(HelloWorld, '/hello')
    api.add_resource(QuestionsRes, '/questions')
    api.add_resource(QuestionRes, '/questions/<int:questionId>')

    return api
