import random
import string
v = input("Generate password (yes = 1 ,No = 0) :" )
if v == ("1"):
  gen = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10))
  print(gen)
elif v == ("0"):
  False