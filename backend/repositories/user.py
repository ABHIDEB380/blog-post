from schemas.user import UserCreate
from sqlalchemy.orm import Session
from db.models.user import User
from core.hashing import Hash

def create_new_user(user_ft: UserCreate, db: Session):
    user = User(
        email_id = user_ft.email_id,
        password = Hash.get_pwd_hash(user_ft.password),
        is_active = True
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user