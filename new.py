# add or remove values in tuple
myfamily = ("mother", "father", "sister", "brother", "sister")

print(type(myfamily))
print(myfamily[2])
print(myfamily[-1])
#*

laptop = {"brand": "dell", "model": "alienware", "year": 2010}

print(laptop["brand"])
laptop["the"] = True
laptop["year"] = 2019

print(laptop)
#*

u = {}
u["un"] = input('What is the users  name? ')
u["age"] = input('What is the users  age? ')
u["c"] = input('What is the users  country of birth ?')
u["known"] = input('What is the user known for? ')
print(u)