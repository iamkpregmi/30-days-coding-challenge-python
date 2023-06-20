class person:
    def __init__(self):
        print("Program Start here")
        print("------------------")

    def person_wish(self):
        print("Hello i'm person")

class person1(person):
    def person(self):
        print("Hello i'm first person")

p1 = person1()
p1.person()
p1.person_wish()