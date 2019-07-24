from peewee import Model  # peewee提供的基础类，一个Model就对应一个数据库
from peewee import BooleanField  # 几种常见的数据类型，还有PrimaryField自己可以看看用法
from peewee import CharField
from peewee import FloatField
from peewee import ForeignKeyField
from peewee import IntegerField
from peewee import TextField
from peewee import DateTimeField
from peewee import ManyToManyField
import datetime

from peewee_db_resources import get_db


class BaseModel(Model):
    createTime = DateTimeField(default=datetime.datetime.now)

    # modefineTime = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = get_db()  # This model uses the "people.db" database.


class User(BaseModel):
    userName = CharField(unique=True)
    userPass = CharField()


# 见解
class Option(BaseModel):
    body = TextField()
    modefineTime = DateTimeField(default=datetime.datetime.now)

    # f key
    writer = ForeignKeyField(User, backref='options')


class Question(BaseModel):
    title = CharField()
    details = CharField(max_length=1024, default='no details')

    # f key
    asker = ForeignKeyField(User, backref='questions')

    options = ManyToManyField(Option, backref='questions')
