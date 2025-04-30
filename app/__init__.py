from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

# 创建 SQLAlchemy 实例
db = SQLAlchemy()
# 创建 CSRFProtect 实例
csrf = CSRFProtect()


# 创建 Flask 应用工厂函数
def create_app():
    app = Flask(__name__)

    # 配置数据库连接 URI，这里使用了 MySQL 数据库，具体连接 URI 格式参考数据库文档
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123000@127.0.0.1/test'
    # 设置 SQLAlchemy 追踪对象修改的功能，这里关闭追踪，因为在大多数情况下不需要追踪对象修改
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 设置应用的密钥，用于加密会话 cookie 等安全功能
    app.config['SECRET_KEY'] = 'hac'

    # 初始化 SQLAlchemy 扩展，将 Flask 应用与数据库关联起来
    db.init_app(app)
    # 初始化 CSRFProtect 扩展，启用 CSRF 保护
    csrf.init_app(app)

    # 导入路由蓝图并注册到应用上
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    # 在应用上下文中创建数据库表结构，这样可以确保在应用启动时自动创建数据库表
    with app.app_context():
        db.create_all()

    # 返回 Flask 应用实例
    return app
