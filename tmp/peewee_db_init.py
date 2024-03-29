from peewee import Model  # peewee提供的基础类，一个Model就对应一个数据库
from peewee import SqliteDatabase  # 我使用Sqlite
from peewee import BooleanField  # 几种常见的数据类型，还有PrimaryField自己可以看看用法
from peewee import CharField
from peewee import FloatField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import TextField
from peewee import DateTimeField
from peewee import ManyToManyField

from pathlib import Path

from peewee_db_resources import get_db

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

# def drop_table(table):
#     u"""
#     table 存在，就删除
#     """
#     if table.table_exists():
#         table.drop_table()

# # 分别建立Teacher和Student表
# create_table(Teacher)
# create_table(Student)
