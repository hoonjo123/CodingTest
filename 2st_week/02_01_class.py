# class Person:
#     pass

#
# person_1 = Person()
# print(person_1)
# person_2 = Person()
# print(person_2)

class Person:
    def __init__(self, name_param, age_param):
        self.name = name_param
        self.age = age_param
        print("Hi I am created!", self, self.name, self.age)

    def talk(self):
        print("안녕하세요 저는 ", self.name, "입니다.", "나이는", self.age, "입니다.")

person_1 = Person("죠니", 31)
print(person_1.name)
print(person_1.age)

person_1.talk()