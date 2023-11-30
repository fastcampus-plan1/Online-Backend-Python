import re

text = "The quick brown fox jumps over the lazy dog."

# 단어 "fox"를 "cat으로 치환"
new_text = re.sub(r'fox', 'cat', text)

print("Original text: ", text)
print("Modified text: ", new_text)