import re

def generate_birthday(matches):
    return f"{'19' if matches[4] in ('1', '2') else '20'}{matches[1]}. {matches[2]}. {matches[3]}"
    
ssn = "900101-4234567"

pattern = re.compile(r'(\d{2})(\d{2})(\d{2})-(\d)\d{6}')
result = pattern.sub(generate_birthday, ssn)

print(result)



