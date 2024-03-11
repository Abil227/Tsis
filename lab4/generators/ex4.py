import math
N = input()
N = int(N)
a = input()
a = int(a)
class Mynums:
    def __iter__(self):
       self.a = N
       return self
   
    def __next__(self):
      while self.a <= a:
        x = pow(self.a,2)
        self.a +=1
        return x
        
      else:
          raise StopIteration   
    
    
myclass = Mynums()
myiter = iter(myclass)

result = [str(y) for y in myiter]
tuta = ", ".join(result)

print(tuta)