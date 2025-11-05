from app import create_app, db
from app.models import Role

app = create_app()

with app.app_context():
    # Create all tables
    db.create_all()

    # Create default roles if they don't exist
    for role_name in ['Admin', 'Manager', 'User']:
        if not Role.query.filter_by(name=role_name).first():
            db.session.add(Role(name=role_name))

    db.session.commit()
    print("Database and roles initialized successfully.")
