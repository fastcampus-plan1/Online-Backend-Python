# 예외 처리의 구조
try:
    value = int("abc")
except ValueError:
    print("숫자로 변환할 수 없는 문자열입니다.")
except ZeroDivisionError:
    print ("0으로 나눌 수 없습니다.")
except:
    print("알 수 없는 오류입니다.")
else:
    print ("변환이 완료되었습니다.")
finally:
    print ("프로그램을 종료합니다.") 