import modules

a = modules.person["age"]
print(a)

import modules as mx
a = mx.person["age"]
print(a)

from modules import person
print(person["age"])