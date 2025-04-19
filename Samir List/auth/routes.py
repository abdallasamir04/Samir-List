from flask import Blueprint, render_template, request, redirect, url_for, flash, session, current_app
from werkzeug.utils import secure_filename
import os
from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!', 'success')
            return redirect(url_for('todo.dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already taken', 'error')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
            return redirect(url_for('auth.register'))
        
        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password),
            profile_image=None
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('auth.login'))

@auth_bp.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('auth.login'))
    
    user = User.query.get(session['user_id'])
    return render_template('profile.html', user=user)

@auth_bp.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('auth.login'))
    
    user = User.query.get(session['user_id'])
    username = request.form.get('username')
    email = request.form.get('email')

    if User.query.filter(User.username == username, User.id != user.id).first():
        flash('Username already taken.', 'error')
        return redirect(url_for('auth.profile'))
    
    if User.query.filter(User.email == email, User.id != user.id).first():
        flash('Email already in use.', 'error')
        return redirect(url_for('auth.profile'))

    user.username = username
    user.email = email
    db.session.commit()
    
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('auth.profile'))

@auth_bp.route('/change_password', methods=['POST'])
def change_password():
    if 'user_id' not in session:
        flash('Please login first.', 'error')
        return redirect(url_for('auth.login'))
    
    user = User.query.get(session['user_id'])
    current_password = request.form.get('current_password')
    new_password = request.form.get('new_password')
    confirm_password = request.form.get('confirm_password')

    if not check_password_hash(user.password, current_password):
        flash('Current password is incorrect.', 'error')
        return redirect(url_for('auth.profile'))
    
    if new_password != confirm_password:
        flash('New passwords do not match.', 'error')
        return redirect(url_for('auth.profile'))
    
    if len(new_password) < 8:
        flash('Password must be at least 8 characters long.', 'error')
        return redirect(url_for('auth.profile'))
    
    user.password = generate_password_hash(new_password)
    db.session.commit()
    
    flash('Password changed successfully!', 'success')
    return redirect(url_for('auth.profile'))

@auth_bp.route('/upload_profile_picture', methods=['POST'])
def upload_profile_picture():
    if 'user_id' not in session:
        return {'success': False, 'message': 'Not authenticated'}, 401
    
    if 'profile_picture' not in request.files:
        return {'success': False, 'message': 'No file uploaded'}, 400
    
    file = request.files['profile_picture']
    if file.filename == '':
        return {'success': False, 'message': 'No file selected'}, 400
    
    if file and allowed_file(file.filename):
        user = User.query.get(session['user_id'])
        
        upload_folder = os.path.join(current_app.root_path, 'static', 'uploads', 'profile_pictures')
        os.makedirs(upload_folder, exist_ok=True)
        
        if user.profile_image and user.profile_image.startswith('/static/uploads/profile_pictures/'):
            old_filepath = os.path.join(current_app.root_path, user.profile_image[1:])
            if os.path.exists(old_filepath):
                os.remove(old_filepath)
        
        filename = f"user_{user.id}_{secure_filename(file.filename)}"
        filepath = os.path.join(upload_folder, filename)
        file.save(filepath)
        
        user.profile_image = f"/static/uploads/profile_pictures/{filename}"
        db.session.commit()
        
        return {'success': True, 'image_url': user.profile_image}
    
    return {'success': False, 'message': 'Invalid file type'}, 400

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}
		   
		   