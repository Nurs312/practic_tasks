class Student:
    __university = 'Politechnical'
    __city = 'Bishkek'

    def __init__(self, firstname, lastname, faculty, year_of_enterance):
        self.firsname = firstname
        self.lastname = lastname
        self.faculty = faculty
        self.year_of_enterance = year_of_enterance

    def __get_student_info(self):
        # print(f'{self.firsname} {self.lastname} в {self.year_of_enterance} году поступил на факультет "{self.faculty}"')
        print(
            f'''{self.firsname} {self.lastname} в {self.year_of_enterance} году поступил на факультет "{self.faculty}".
Унивеситет: {self.__university} в горде {self.__city}.''')


student = Student('Иван', 'Иванов', 'Программирование', '2018')
print(student.firsname)
print(student.lastname)
print(student.faculty)
print(student.year_of_enterance)
# student.__det_student_info()
# print(student.__city)
# print(student.__univesity)
student._Student__get_student_info()
print( student._Student__city)
print(student._Student__university)
