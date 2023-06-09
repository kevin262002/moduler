import string
import random

res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
 
print("Random string : ",str(res))
