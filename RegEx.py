import re

text = "Hello, my email is john@example.com and my phone number is 123-456-7890."

# Searching for an email address using a regular expression
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
match = re.search(pattern, text)
if match:
    print("Email found:", match.group())

# Searching for a phone number using a regular expression
pattern = r"\d{3}-\d{3}-\d{4}"
match = re.search(pattern, text)
if match:
    print("Phone number found:", match.group())
