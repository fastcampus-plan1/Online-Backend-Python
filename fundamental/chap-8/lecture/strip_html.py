import re

def remove_html_tags(input):
    pattern = re.compile(r'<.*?>')
    result = re.sub(pattern, '', input)
    
    return result

input = "<p>This is <b>Python</b> and <i>Regular Expression</i>.</p>"

result = remove_html_tags(input)
print(result)

