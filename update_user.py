from db import db_session
from models import User


my_user = User.query.first()
my_user.lname = "Сидоров"
db_session.commit()