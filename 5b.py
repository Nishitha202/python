import re
phone_regex=re.compile(r'\+\d{12}')
email_regex=re.compile(r'[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[A-Za-z]{2,}')
with open('example.txt','r') as f:
    for line in f:
        matches=phone_regex.findall(line)
        for match in matches:
            print(match)
        matches = email_regex.findall(line)
        for match in matches:
            print(match)