import re
text = "The quick brown fox jumps over the lazy dog."

search_result = re.search(r'the', text)
print(search_result)
# <re.Match object; span=(31, 34), match='the'>

match_result = re.match(r'the', text)
print(match_result)
# None

find_all_result = re.findall(r'the', text, re.IGNORECASE)
print(find_all_result)
# ['The', 'the']