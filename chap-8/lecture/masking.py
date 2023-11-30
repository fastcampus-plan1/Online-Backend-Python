import re

def mask_phone_numbers(match):
    return f"{match.group(1)}-****-{match.group(3)}"

def mask_ssn(match):
    return f"{match.group(1)}-{match.group(2)}******"

personal_info = """
이름: 홍길동
주소: 서울시 강남구
전화번호: 010-1234-5678
주민등록번호: 930101-1234567
"""

phone_number_pattern = re.compile(r'(01[016789])-(\d{3,4})-(\d{4})')
ssn_pattern = re.compile(r'(\d{6})-(\d)\d{6}')

masked_info = phone_number_pattern.sub(mask_phone_numbers, personal_info)
masked_info = ssn_pattern.sub(mask_ssn, masked_info)

print(masked_info)





