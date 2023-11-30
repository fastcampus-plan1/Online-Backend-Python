# 상품목록과 각 상품의 가격이 제공됨
# 사용자는 각 상품을 구매할 수 있음 (장바구니에 담기)
# 장바구니에 담은 상품을 구매할 수 있음, 구매 이후에는 장바구니가 비워짐
# 상품 목록 -> 상품명, 가격 (Dictionary, key: 상품명, value: 가격)
items = {
    "사과": 1000, "바나나" : 2200, "블루베리" :3800, "복숭아" : 4000,
    "배": 5000, "키위" : 2000, "오렌지" : 2500, "멜론" : 7000
}

# 장바구니 목록 -> 상품명 (List)
shoppings = []

while True:
    print ("")
    print ("1. 상품 목록 조회하기")
    print ("2. 장바구니에 추가하기")
    print ("3. 장바구니 목록 조회하기")
    print ("4. 결제하기")
    print ("0. 종료하기")
    menu = input("원하는 메뉴를 입력해주세요: ")
    if menu == "1":
        for item in items:
            print(f"{item}의 가격은 {items[item]}원 입니다.")
    elif menu == "2":
        item = input("구입하고자 하는 상품명을 입력하세요: ")
        if item in items:
            shoppings.append(item)
            print(f"{item} 상품이 장바구니에 추가되었습니다.")
        else:
            print("상품명이 잘못 입력되었습니다.")
    elif menu == "3":
        print(shoppings)
    elif menu == "4":
        total_price = 0
        for item in shoppings:
            price = items[item]
            total_price = total_price + price
        print(f"전체 구매 가격은 {total_price}원 입니다.")
        shoppings.clear()
    elif menu == "0":
        break
    else:
        print("잘못된 입력입니다.")
        continue