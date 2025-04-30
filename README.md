# Flask CRUD 示例应用

这是一个使用 Flask、Flask-SQLAlchemy 和 Flask-WTF 构建的简单 CRUD（创建、读取、更新、删除）Web 应用程序。

## 功能

- **查看用户列表:** 在首页 `/` 显示所有用户的信息。
- **添加用户:** 通过 `/user/add` 页面添加新用户。
- **编辑用户:** 通过点击用户列表中的"编辑"按钮，跳转到 `/user/edit/<user_id>` 页面修改用户信息。
- **删除用户:** 通过点击用户列表中的"删除"按钮删除用户。

## 技术栈

- **后端:**
  - Flask: Web 框架
  - Flask-SQLAlchemy: ORM，用于数据库交互
  - Flask-WTF: 表单处理和 CSRF 保护
  - Python 3
- **数据库:** MySQL (在 `app/__init__.py` 中配置)
- **前端:**
  - HTML (Jinja2 模板引擎)
  - CSS

## 安装与运行

1.  **克隆仓库 (如果适用):**

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **创建并激活虚拟环境 (推荐):**

    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **安装依赖:**

    ```bash
    pip install Flask Flask-SQLAlchemy Flask-WTF mysqlclient # 或者 PyMySQL
    # 如果使用 PyMySQL，需要修改 app/__init__.py 中的数据库 URI
    # 'mysql+pymysql://root:123000@127.0.0.1/test'
    ```

    _注意: `mysqlclient` 可能需要系统级的依赖。如果安装困难，可以尝试 `PyMySQL`。_

4.  **配置数据库:**

    - 确保你有一个正在运行的 MySQL 服务器。
    - 在 MySQL 中创建一个名为 `test` 的数据库。
    - 根据你的 MySQL 配置，修改 `app/__init__.py` 文件中的数据库连接 URI:
      ```python
      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://你的用户名:你的密码@你的主机/test'
      ```

5.  **运行应用:**
    ```bash
    python run.py
    ```
    应用将在 `http://127.0.0.1:8085` 上运行。

## 项目结构

```
flask_demo/
├── app/
│   ├── static/
│   │   └── style.css         # 主样式文件
│   │   ├── base.html         # 基础模板
│   │   ├── users.html        # 用户列表页面
│   │   └── user_form.html    # 用户添加/编辑表单页面
│   ├── __init__.py         # 应用工厂和初始化
│   ├── forms.py            # WTForms 表单定义
│   ├── models.py           # SQLAlchemy 模型定义
│   └── routes.py           # 路由和视图函数
├── run.py                  # 应用启动脚本
└── README.md               # 本文件
```
