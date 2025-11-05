from flask import Blueprint, render_template, redirect, url_for, request, flash, abort
from flask_login import login_required, current_user
from .models import Resource, User
from . import db
from .decorators import roles_required

main = Blueprint('main', __name__)

# Home redirect
@main.route('/')
def home():
    return redirect(url_for('auth.login'))

# User dashboard
@main.route('/dashboard')
@login_required
@roles_required(['User'])
def dashboard():
    resources = Resource.query.all()
    return render_template('dashboard.html', resources=resources)

# Admin dashboard
@main.route('/admin')
@login_required
@roles_required(['Admin'])
def admin_dashboard():
    users = User.query.all()
    resources = Resource.query.all()
    return render_template('admin_dashboard.html', users=users, resources=resources)

# Manager dashboard
@main.route('/manager')
@login_required
@roles_required(['Manager'])
def manager_dashboard():
    resources = Resource.query.all()
    return render_template('manager_dashboard.html', resources=resources)

# Create resource
@main.route('/resource/create', methods=['GET','POST'])
@login_required
@roles_required(['Admin','Manager'])
def create_resource():
    if request.method == 'POST':
        name = request.form['name']
        content = request.form['content']
        resource = Resource(name=name, content=content, owner=current_user)
        db.session.add(resource)
        db.session.commit()
        flash('Resource created!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('create_resource.html')

# Edit resource
@main.route('/resource/edit/<int:id>', methods=['GET','POST'])
@login_required
@roles_required(['Admin','Manager'])
def edit_resource(id):
    resource = Resource.query.get_or_404(id)
    if request.method == 'POST':
        resource.name = request.form['name']
        resource.content = request.form['content']
        db.session.commit()
        flash('Resource updated!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('edit_resource.html', resource=resource)

# Delete resource
@main.route('/resource/delete/<int:id>', methods=['POST'])
@login_required
@roles_required(['Admin'])
def delete_resource(id):
    resource = Resource.query.get_or_404(id)
    db.session.delete(resource)
    db.session.commit()
    flash('Resource deleted!', 'success')
    return redirect(url_for('main.dashboard'))
