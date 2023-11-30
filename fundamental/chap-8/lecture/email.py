import re

text = "Contact us at support@example.me or info@company.com for more information."

email_pattern = r'\b[\w.%+-]+@[\w.-]+\.[A-Z|a-z]{2,}\b'

emails = re.findall(email_pattern, text)
print(emails)