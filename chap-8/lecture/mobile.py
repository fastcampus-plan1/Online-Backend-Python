import re

phone_number_pattern = re.compile(r'01[016789]-\d{3,4}-\d{4}')

personal_info = """
이름: 홍길동
주소: 서울시 강남구
전화번호: 010-1234-5678
주민등록번호: 930101-1234567
"""

match = phone_number_pattern.search(personal_info)
if match:
    print(f"핸드폰 번호: {match.group()}")


