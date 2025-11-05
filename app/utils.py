from .models import AuditLog
from . import db
from flask_login import current_user

def log_action(action):
    if current_user.is_authenticated:
        entry = AuditLog(user=current_user, action=action)
        db.session.add(entry)
        db.session.commit()
