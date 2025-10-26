from flask import render_template, request, redirect, url_for
from ..extensions import db
from ..models import Task
from . import main_bp

@main_bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html',tasks=tasks)

@main_bp.route('/add',methods=['POST'])
def grow_task():
    title = request.form.get('title')
    desc = request.form.get('description')
    new_task = Task(title=title, description=desc)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main_bp.route('/edit/<int:id>',methods=['GET','POST'])
def edit_task(id):
    task = Task.query.get_or_404(id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('edit_task.html',task=task)

@main_bp.route('/delete/<int:id>')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))
