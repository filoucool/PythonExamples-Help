import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
Pstring =  "".join(choice(characters) for x in range(randint(8, 18)))
print (Pstring)