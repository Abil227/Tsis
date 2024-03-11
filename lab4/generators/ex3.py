import math
N = input()
N = int(N)
class Mynums:
    def __iter__(self):
       self.a = 1
       return self
   
    def __next__(self):
      while self.a <= N:
        x = self.a
        if x % 3 == 0 and x % 4 == 0:
          self.a += 1
          return x
        else:
            self.a += 1
      else:
          raise StopIteration   
    
    
myclass = Mynums()
myiter = iter(myclass)

result = [str(y) for y in myiter]
tuta = ", ".join(result)

print(tuta)