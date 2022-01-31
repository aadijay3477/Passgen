import random
lower="abcdefghijklmnopqrstuvw"
upper=lower.upper()
number="0123456789"
symbol="[](){\}|'@#!$%^&*-+=_"

all=lower+upper+number+symbol
length=random.randint(8, 25)
password="".join(random.sample(all, length))
print(password)
