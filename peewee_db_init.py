from pathlib import Path

import random

from db_resources import get_db

from peewee_db_class import User, Option, Question

db = get_db()
"""
建表和删除表
由于peewee的表封装成了类的形式，
因此可以通过传参进行传递，
便于写重复利用的function
"""


def create_db(db):
    u"""
    创建数据库
    """
    db.create_tables(
        [User, Option, Question,
         Question.options.get_through_model()])


def testdb(db):
    """testdb
    """
    userstuple = tuple(('user' + str(i), 'pass' + str(i)) for i in range(1, 10))
    questuple = tuple(
        ('q' + str(i), random.randint(1, i)) for i in range(1, 10))
    optiontuple = tuple(
        ('o' + str(i), random.randint(1, 10)) for i in range(1, 10))

    qo = tuple(
        set((random.randint(1, 10), random.randint(1, 10)) for i in range(20)))

    with db.atomic():
        User.insert_many(userstuple, fields=[User.userName,
                                             User.userPass]).execute()
        Question.insert_many(questuple,
                             fields=[Question.title,
                                     Question.asker_id]).execute()

        Option.insert_many(optiontuple, fields=[Option.body,
                                                Option.writer_id]).execute()
        qoRelation = Question.options.get_through_model()
        qoRelation.insert_many(
            qo, fields=[qoRelation.question_id,
                        qoRelation.option_id]).execute()


# [option.body for option in q1.options]

if __name__ == "__main__":
    create_db(db)
    testdb(db)
