from pathlib import Path
from peewee import SqliteDatabase  # 我使用Sqlite


def get_db():
    curDir = Path().cwd()

    # 指定database的路径为同该.py文件目录下的test.db数据库
    # 而且便于后边其他脚本的导入（主要是为了db.atomic()的使用）
    dbname = 'test.db'

    dbpath = str(curDir / dbname)

    db = SqliteDatabase(dbpath)

    return db
