# 부모 클래스 1: 새 (날 수 있음)
class Bird:
    def __init__(self):
        self.can_fly = True
    def fly (self):
        print("This bird can fly.")

# 부모 클래스 2: 물고기 (수영할 수 있음)
class Fish:
    def __init__(self):
        self.can_swim = True
    def swim(self):
        print("This fish can swim.")

# 자식 클래스: 날으는 물고기 (다중 상속)
class FlyingFish(Fish, Bird):
    def __init__(self):
        # 두 부모 클래스의 생성자 호출
        Bird.__init__(self)
        Fish.__init__(self)
    def ability(self):
        if self.can_fly and self. can_swim:
            print("This creature can both fly and swim.")
        elif self.can_fly:
            print("This creature can fly but cannot swim.")
        elif self.can_swim:
            print("This creature can swim but cannot fly.")
        else:
            print("This creature cannot fly or swim.")

# 다이아몬드 상속 문제
class A:
    def method(self):
        print("Method from class A")
class B(A):
    def method (self):
        print("Method from class B")
class C(A):
    def method(self):
        print ("Method from class C")
class D(B, C) :
    pass

d = D()
d. method() # 어떤 메서드가 호출될까요?