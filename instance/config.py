import os

class Config:
    # Secret key for session & CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key'

    # Database URI
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'rbacpro.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Login settings
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # Optional: session timeout (seconds)
    PERMANENT_SESSION_LIFETIME = 3600  # 1 hour

    # Debug
    DEBUG = True
