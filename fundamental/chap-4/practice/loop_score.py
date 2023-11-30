students = {}   # dictionary

# 입력대기창
while True:
    # 메뉴 출력
    print ("")
    print ("1. 성적 입력하기")
    print ("2. 학생 조회하기")
    print ("3. 학점 조회하기")
    print ("0. 종료하기")
    menu = input("메뉴 번호를 입력하세요: ")

    # 1. 성적 입력하기
    if menu == "1":
        # 학생의 이름과 점수를 입력받아 저장
        name = input("학생의 이름을 입력해주세요. ")
        score = input("점수도 입력해주세요. ")
        students[name] = int(score)
        print(f"{name}의 성적은 {students[name]} 입니다. ")
    
    # 2. 학생 조회하기
    elif menu == "2":
        name = input("조회하고자 하는 학생의 이름을 입력하세요. ")
        if name in students.keys():
            print (f"{name}의 점수는 {students[name]} 입니다.")
        else:
            print(f"{name}은 등록되지 않았습니다.")
    
    # 3. 학점 조회하기
    elif menu == "3":
        name = input("조회하고자 하는 학생의 이름을 입력하세요. ")
        if name not in students.keys():
            print(f"{name}은 등록되지 않았습니다.")
            continue

        score = students[name]
        # A+: 95~99, B+: 85~89, C+: 75~79, D+: 65~69
        # A: 90~94, B: 80~84, C: 70~74, D: 60~64, F: ~59
        if score <= 99 and score >= 90: # A
            grade = "A"
        elif score <= 89 and score >= 80: # B
            grade = "B"
        elif score <= 79 and score >= 70 : # C
            grade = "C"
        elif score <= 69 and score >= 60: # D
            grade = "D"
        elif score <= 59 and score >= 1: # F
            grade = "F"
        else:
            grade = None

        if grade in ["A", "B", "C", "D"]:
            mod = score % 10
            if mod >= 5:
                grade = grade + "+"
        
        print(f"{name}의 학점은 {grade} 입니다.")

    # 0. 종료하기
    elif menu == "0":
        break
    else:
        print ("잘못된 메뉴가 입력되었습니다.")
        continue