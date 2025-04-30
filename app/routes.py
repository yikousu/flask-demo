# -*- coding: utf-8 -*-

# 导入 render_template 函数用于渲染模板
# 导入 Blueprint 类用于创建蓝图
# 导入 redirect 和 url_for 函数用于重定向和构造 URL
# 导入 flash 函数用于向用户发送消息
from flask import render_template, Blueprint, redirect, url_for, flash
# 从 flask_wtf 导入基础表单类，用于 CSRF 验证
from flask_wtf import FlaskForm
from .models import User
from .forms import UserForm
from . import db

bp = Blueprint('main', __name__)

# 定义主页路由
@bp.route('/')
def index():
    # 查询所有用户
    users = User.query.all()
    form = UserForm()
    return render_template('users.html', users=users, form=form)

# 定义添加用户路由，支持 GET 和 POST 方法
@bp.route('/user/add', methods=['GET', 'POST'])
def add_user():
    # 创建用户表单对象
    form = UserForm()
    # 如果表单验证通过且为 POST 请求
    if form.validate_on_submit():
        new_user = User(name=form.name.data, age=form.age.data)
        db.session.add(new_user)
        db.session.commit()
        flash('用户添加成功!', 'success')
        return redirect(url_for('main.index'))
    # 渲染用户表单模板，并传入表单对象
    return render_template('user_form.html', form=form)

# 定义编辑用户路由，支持 GET 和 POST 方法
@bp.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.name = form.name.data
        user.age = form.age.data
        db.session.commit()
        flash('用户信息更新成功!', 'success')
        return redirect(url_for('main.index'))
    # 渲染用户表单模板，并传入表单对象
    return render_template('user_form.html', form=form)

# 定义删除用户路由，支持 POST 方法
@bp.route('/user/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    # 使用基础 FlaskForm 来验证 POST 请求和 CSRF token
    form = FlaskForm()
    if form.validate_on_submit(): # 只验证请求方法和 CSRF
        db.session.delete(user)
        db.session.commit()
        flash('用户删除成功!', 'success')
    else:
        # CSRF 校验失败
        flash('删除用户失败：无效的操作或会话已过期。', 'danger')
    return redirect(url_for('main.index'))
