import random

lst = []

for i in range(100):
    lst.append(random.randrange(11111111,99999999))

print(lst)
print()

w = random.sample(lst,2)
print("Winners : ",w)
