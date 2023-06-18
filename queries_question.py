import constants
from models import Question


def get_questions(gender):
    if gender == constants.gender_female:
        questions_data = Question.query.filter(Question.num_of_question_female != 0)\
                                    .order_by(Question.num_of_question_female)
        for question in questions_data:
            print(f'{question.num_of_question_female}.) {question.question}')  
    else:
        questions_data = Question.query.filter(Question.num_of_question_male != 0)\
                                    .order_by(Question.num_of_question_male)
        for question in questions_data:
            print(f'{question.num_of_question_male}.) {question.question}')  



if __name__ == '__main__':
     get_questions(constants.gender_male)