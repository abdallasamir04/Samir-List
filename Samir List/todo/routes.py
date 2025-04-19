from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, Todo

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
def index():
    if 'user_id' not in session:
        return render_template('index.html')
    
    # Get filter status from URL parameters, default to 'all'
    filter_status = request.args.get('filter', 'all')

    # Get active (incomplete) tasks for the current user
    if filter_status == 'active':
        active_tasks = Todo.query.filter_by(
            user_id=session['user_id'],
            completed=False
        ).order_by(Todo.created_at.desc()).all()
    else:
        active_tasks = Todo.query.filter_by(
            user_id=session['user_id']
        ).order_by(Todo.created_at.desc()).all()
    
    return render_template('index.html', active_tasks=active_tasks)

@todo_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first.')
        return redirect(url_for('auth.login'))

    # Retrieve all todos for the logged-in user
    todos = Todo.query.filter_by(user_id=session['user_id']).order_by(Todo.created_at.desc()).all()
    
    # Check the filter from URL parameter (all, active, or completed)
    filter_status = request.args.get('filter', 'all')
    if filter_status == 'active':
        todos = [todo for todo in todos if not todo.completed]
    elif filter_status == 'completed':
        todos = [todo for todo in todos if todo.completed]

    return render_template('dashboard.html', todos=todos, filter_status=filter_status)

@todo_bp.route('/add_todo', methods=['GET', 'POST'])
def add_todo():
    if 'user_id' not in session:
        flash('Please login first.')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']  # Get the priority from the form

        new_todo = Todo(
            title=title, 
            description=description, 
            priority=priority,  # Set the priority
            user_id=session['user_id']
        )

        db.session.add(new_todo)
        db.session.commit()

        flash('Todo added successfully!')
        return redirect(url_for('todo.dashboard'))

    return render_template('add_todo.html')

@todo_bp.route('/edit_todo/<int:id>', methods=['GET', 'POST'])
def edit_todo(id):
    todo = Todo.query.get_or_404(id)

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.description = request.form['description']
        todo.completed = 'completed' in request.form  # Mark as completed if the checkbox is checked
        todo.priority = request.form['priority']  # Update priority

        db.session.commit()
        flash('Todo updated successfully!')
        return redirect(url_for('todo.dashboard'))

    return render_template('edit_todo.html', todo=todo)

@todo_bp.route('/delete_todo/<int:id>')
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted successfully!')
    return redirect(url_for('todo.dashboard'))

# Add the missing toggle_todo route
@todo_bp.route('/toggle_todo/<int:id>')
def toggle_todo(id):
    if 'user_id' not in session:
        flash('Please login first.')
        return redirect(url_for('auth.login'))

    todo = Todo.query.get_or_404(id)

    # Check if the todo belongs to the logged-in user
    if todo.user_id != session['user_id']:
        flash('Unauthorized access')
        return redirect(url_for('todo.dashboard'))

    # Toggle the completed status
    todo.completed = not todo.completed

    try:
        db.session.commit()
        flash('Task status updated!')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}')

    return redirect(url_for('todo.dashboard'))
