# 점수를 입력받는다.
score_str = input("점수를 입력해주세요: ")
score = int(score_str)

# 점수가 비정상 범위이면, 아무것도 실행하지 않는다.
# 점수의 각 등급에 따른 결과를 출력한다. (A: 9~99, B: 80~89, C: 70~79, D: 60~69, F: ~59)
if score <= 99 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
elif score <= 79 and score >= 70:
    grade = "C"
elif score <= 69 and score >= 60:
    grade = "D"
elif score <= 59 and score >= 1:
    grade = "F"
else:
    grade = None

if grade is not None:
    print(f"등급은 {grade} 입니다.")