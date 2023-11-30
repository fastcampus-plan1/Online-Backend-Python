# 상속 클래스 정의하기
# 부모 클래스
class Person:
    def _init_(self, name, job):
        self.name = name
        self.job = job
    def introduce(self):
        print (f"제 이름은 {self.name} 입니다. 직업은 {self. job} 입니다.")

# 자식 클래스
class Actor (Person):
    def _init_(self, name, best_movie):
        super().__init__(name, job="배우")
        self.best_movie = best_movie
    def filmography(self):
        print(f"대표 작품은 {self.best_movie} 입니다.")

# 객체 생성
actor_song = Actor("송강호", best_movie="기생층")

# 상속된 메서드 사용
actor_song.introduce() # 제 이름은 송강호 입니다. 직업은 배우 입니다.
actor_song.filmography() # 대표 작품은 기생충 입니다.


