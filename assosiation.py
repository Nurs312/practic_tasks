#      Композиция:
# class UniverMixin:
#     univer = 'Manas'
#
# class Student1:
#     deconat = 'Finance'
#
# class Student(UniverMixin):
#     def __init__(self, group):
#         self.group = group
#
#     def tell(self):
#         return self.group
#
#
# class NewStudent(Student1):
#     def __init__(self, group, name, age):
#         self.name = name
#         self.age = age
#         self.group = group
#         self.student = Student(self.group)
#
#     def info(self):
#         return f'Group: {self.student.tell()}, Name: {self.name}, Age: {self.age}'
#
#
# nurs = NewStudent('IT', 'Nurs', 18)
# print(nurs.info())
# print(nurs.deconat)


# class UniverMixin:
#     univer = 'Manas'
#
# class Student1:
#     deconat = 'Finance'
#

#          Агрегация:
# class Student(object):
#     def __init__(self, group):
#         self.group = group
#
#     def tell(self):
#         return self.group
#
#
# class NewStudent(object):
#     def __init__(self, group, name, age):
#         self.name = name
#         self.age = age
#         self.group = group
#
#     def info(self):
#         return f'Group: {self.group.tell()}, Name: {self.name}, Age: {self.age}'
#
#
# student1 = Student('IT')
# nurs = NewStudent(student1, 'Nurs', 18)
# print(nurs.info())

