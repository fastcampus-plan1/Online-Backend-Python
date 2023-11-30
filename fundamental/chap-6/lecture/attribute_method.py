class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hello! I'm " + self.name)
        
    def update_age (self, new_age) :
        if new_age > 0:
            self.age = new_age
            print (f"'I'm {self.age} years old now!")
        else:
            raise ValueError("나이는 0살보다 어릴 수 없습니다.")
        
man = Person ("Robert", 30)
woman = Person ("Julia", 32)