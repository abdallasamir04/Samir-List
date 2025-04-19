
from flask import Flask, session
from config import get_config
from models import db
from todo.routes import todo_bp
from auth.routes import auth_bp
from flask_migrate import Migrate
from datetime import datetime


def create_app(config=None):
    app = Flask(__name__)
    app.secret_key = '156fxgh[fglzpf/uiou'
    
    # Load configuration
    if config:
        app.config.from_object(config)
    else:
        app.config.from_object(get_config())
    
    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Register Blueprints
    app.register_blueprint(todo_bp, url_prefix='/')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # Custom template filter for date formatting
    @app.template_filter('strftime')
    def _jinja2_filter_datetime(date, fmt=None):
        if fmt:
            return date.strftime(fmt)
        return date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Context processors
    @app.context_processor
    def inject_user():
        from models import User
        if 'user_id' in session:
            user = User.query.get(session['user_id'])
            return dict(current_user=user)
        return dict(current_user=None)
    
    @app.context_processor
    def inject_datetime():
        from datetime import datetime
        return {'now': datetime.utcnow()}
    
    return app

# Create the app instance
app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=app.config.get('DEBUG', True))
	
