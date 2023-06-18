from classes.person import Person



class Question(Person):
    def __init__(self, fname, lname, gender="Male"):
        super().__init__(fname, lname, gender)
    def read_question(self):
        pass
    #в read_question хочу открыть файл csv и в зависимости от гендера
    # заполнить переменные данными из соответствующих столбцов:    
    #    self.question =
    #    self.num =
    #    self.d_n_yes_point =  
    #    self.d_n_no_point =  
    #    self.mdp_yes_point =  
    #    self.mdp_no_point =  

    def get_answer(self):
    # a здесь - получить ответ и записать его в переменную self.answer
        pass

    def count_both_points(self, answer):
    # a здесь в зависимости от ответа подсчитать окончательный балл Д-Н за этот ответ,
    # например: 
    #   self.d_n = self.d_n_yes_point if self.answer == "ДА" else self.d_n_no_point
    # то же самое c  self.d_n