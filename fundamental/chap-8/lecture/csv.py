import re
pattern = re.compile(r'[^,]+,[^,]+,[^,]+,([^,]+),[^,]+,([^,]+)')

with open('log_file.csv', 'r') as file:
    for line in file:   # 파일 한 줄씩 읽기
        match = pattern.match(line)

        if match:
            fourth_value = match.group(1)
            sixth_value = match.group(2)

            print(f"4번째 값: {fourth_value}, 6번째 값: {sixth_value}")
        else:
            print("패턴과 매치되지 않는 라인이 있습니다.")