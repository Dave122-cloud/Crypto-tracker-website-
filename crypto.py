 from flask import Flask, render_template, redirect, url_for, session
from config import Config
from models.models import db, User, Portfolio
from routes.auth import auth_bp
from routes.portfolio import portfolio_bp
from routes.prices import prices_bp

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database with the app
db.init_app(app)

# Register all route blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(portfolio_bp)
app.register_blueprint(prices_bp)

@app.route('/')
def index():
    """Landing page — redirect to dashboard if already logged in"""
    if 'user_id' in session:
        return redirect(url_for('portfolio.dashboard'))
    return render_template('index.html')

# Create all database tables on first run
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
