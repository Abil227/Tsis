import math
n = int(input())
a = int(input())
tg = math.ceil(math.tan(math.pi/n))
S = n * pow(a,2) / 4 * tg
print(S)