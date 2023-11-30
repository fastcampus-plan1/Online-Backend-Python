import re

input_string = "서울-대구-대전-부산"

result = re.sub(r'(\w+)-(\w+)-(\w+)-(\w+)', r'\1-\3-\2-\4', input_string)

print(result)


