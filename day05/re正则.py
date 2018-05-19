import re

email = input("email:")
try:
    print(re.search("@.+",email).group())
except Exception as e:
    print("邮箱地址不对")


