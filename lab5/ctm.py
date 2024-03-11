import re
txt = input()
#ex1 
x = re.search(r"a[b]*", txt)
print(x)
 
#ex2
x = re.search(r"ab{2,3}",txt)
#ex3
x = re.search(r"[a-z]+_[a-z]+",txt)
#ex4
x = re.search(r"[A-Z][a-z]+",txt)
#ex5
x = re.search(r"a.*b$")
#.* lyuboi simvol mozhet povtoryatsya nol' ili bolee raz
#ex6
x = re.sub(r"[.,/s]+",":",txt)


#ex8
x = re.split(r"[A-Z]",txt)
print(x)
