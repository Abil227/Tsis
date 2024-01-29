thislist = ["orange", "mango", "kiwi", "pineapple", "banana"] #sort by first letter in alphabet sequence
thislist.sort()
print(thislist)

thislist = [100,50,65,82,23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) #reverse = true!?!??!?cheza
print(thislist)

thislist = [100, 50,65,82,23]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
    return abs(n - 50)

thislist = [100,50,65,82,23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)