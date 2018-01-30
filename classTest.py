# -*- coding:utf-8 -*-

# class Student(object):
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def print_socre(self):
#         print('%s:%s' % (self.name,self.score))
#         return(122)
#         #pass
#
#
#
# bart = Student('Xy',9)
# bart.print_socre()
# #print(bart.print_socre())

class Student(object):
    # def __init__(self,name,socre):
    #     self.name = name
    #     self.socre = socre

    def get_grade(self):
        if self.socre > 90:
            return 'A'
        elif self.socre > 60:
            return 'B'
        else:
            return 'C'



# bart = Student('Xy',100)
# list = Student('X',70)
# lists = Student('Xs',10)
#
# print(bart.get_grade())
# print(list.get_grade())
# print(lists.get_grade())

# print(dir())

L = []
for x in range(10):
    L.append(x)

print(L)