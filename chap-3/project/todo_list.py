todo_list = []

while True:
    print("")
    print("할 일 목록 관리자")
    print("1. 할 일 추가")
    print("2. 할 일 삭제")
    print("3. 할 일 목록 보기")
    print("4. 종료")

    choice = input("선택: ")

    if choice == "1":
        todo = input("추가 할 일: ")
        todo_list.append(todo)
        print(f"{todo} 할 일이 추가되었습니다.")
    elif choice == "2":
        todo = input("삭제 할 일: ")
        todo_list.remove(todo)
        print(f"{todo} 할 일이 삭제되었습니다.")
    elif choice == "3":
        print(todo_list)
    elif choice == "4":
        break
    else:
        print("올바른 선택이 아닙니다. 다시 시도하세요.")