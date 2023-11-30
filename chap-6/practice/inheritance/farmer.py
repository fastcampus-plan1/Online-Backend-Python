from person import Person

class Farmer(Person):
    def __init__(self, name, age, fruit):
        super().__init__(name, age, job="Farmer")
        self.fruit = fruit
    
    def introduce(self):
        super()._hello()
        print(f"저는 {self.fruit} 농장을 하고 있습니다.")
