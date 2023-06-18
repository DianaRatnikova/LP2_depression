
import constants
from db import db_session
from models import Question, User, Answers

# ТУТ ПОКА БРЕД, НО КОГДА РАЗБЕРУСЬ С ЗАПРОСАМИ, 
# РАЗМЕЩУ ЗДЕСЬ ФУНКЦИИ ПО НОРМАЛЬНОМУ ВЫТАСКИВАНИЮ ОТВЕТОВ ОТ ЮЗЕРОВ.
# ПОКА НЕ УСПЕЛА РАЗОБРАТЬ ЭТУ ТЕМУ

def get_answers(user):
 #  user_answers = Answers.query.filter(Answers.user_id == 1).order_by(Question.num_of_question_female.desc())
    user_answers = Answers.query.filter(Answers.user_id == user.id)
 #   for user in db.session.query(User).filter_by(active=True).filter().all():
    for user_answer in user_answers:
        print(f'{user_answer.user_id}, {user_answer.question_id}, {user_answer.answer}')  


def get_everything():
    query = User.query.join(Answers, Answers.user_id == User.id )
    for item in query:
    #    print(f"{item.fname}, {item.question}, {item.answer}")
        print(f"{item.fname}, {item.user_id}")
        print()


def get_everything1():
    query = Answers.query.join(Answers.user, Answers.question).filter(User.id == 1)
    for answer in query:
        print(f"{answer =}")

if __name__ == '__main__':
 #   get_answers(User.query.first())
    get_everything1()
