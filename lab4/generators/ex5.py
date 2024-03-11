import math
N = input()
N = int(N)
class Mynums:
    def __iter__(self):
       self.a = N
       return self
   
    def __next__(self):
      while self.a > 0:
          x = self.a 
          self.a -= 1
          return x
          
      else:
          raise StopIteration   
    
myclass = Mynums()
myiter = iter(myclass)

for x in myiter:
    print(x)
    