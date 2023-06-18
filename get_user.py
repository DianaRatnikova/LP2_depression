from models import User


if __name__ == '__main__':
    my_user = User.query.first()
    print(f"""Имя: {my_user.fname}
    Фамилия: {my_user.lname}
    Пол: {my_user.gender}""")