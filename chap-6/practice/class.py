class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print(f"Hello! I'm {self.name}!")
        
    def update_age (self, age) :
        if age < 0:
            raise ValueError("나이는 음수일 수 없습니다.")
        else:
            self.age = age
            print (f"'I'm {self.age} years old!")
        
if __name__ == "__main__":
    man = Person ("John", 30)
    man.hello()
    man.update_age(31)
 