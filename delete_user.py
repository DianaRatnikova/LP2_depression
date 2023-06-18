from db import db_session
from models import User


if __name__ == '__main__':
    my_user = User.query.first()
    db_session.delete(my_user)
    db_session.commit()