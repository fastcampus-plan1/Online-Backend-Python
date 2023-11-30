class Car:
    def init (self) -> None:
        self.__speed = 0

    def drive(self, speed) -> int:
        if speed < 0:
            print(f"잘못된 속도입니다. {self.__speed} km/h 를 유지합니다.")
            return self.__speed
        
        self.__speed = speed
        if speed == 0:
            print("정지 중입니다. ")
        else:
            print(f"지금 속도는 {self. __speed} km/h 입니다. ")

redcar = Car ()
redcar.drive (0) # 정지 중입니다.
redcar.drive (10) # 지금 속도는 10 km/h 입니다.
redcar.drive(-10) # 지금 속도는 10 km/h 입니다.
