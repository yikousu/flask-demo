# -*- coding: utf-8 -*-

from flask import render_template, Blueprint, redirect, url_for, flash
from .models import User
from .forms import UserForm
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('users.html', users=users)

@bp.route('/user/add', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        new_user = User(name=form.name.data, age=form.age.data)
        db.session.add(new_user)
        db.session.commit()
        flash('User added successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('user_form.html', form=form)

@bp.route('/user/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    form = UserForm(obj=user)
    if form.validate_on_submit():
        user.name = form.name.data
        user.age = form.age.data
        db.session.commit()
        flash('User updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('user_form.html', form=form)

@bp.route('/user/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('main.index'))


