# -*- coding: utf-8 -*-
# 从当前应用程序或当前模块所在的包中导入 db 对象
from . import db

# 定义 User 类，继承自 db.Model，用于表示用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)

    # 定义 __repr__ 方法，用于返回对象的字符串表示形式
    def __repr__(self):
        return f'<User {self.name}>'
