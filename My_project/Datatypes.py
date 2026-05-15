#int, float, string
x = 3          #int
print(x)
print(type(x))
y = 3.14       #float
print(y, type(y))
s = "ashna"    #string
print(s, type(s))

# Lists, Tuples, sets
lst = [2, 4, 6]    #Lists Mutable, can add or remove elements
print(lst)
lst.append(8) #[2, 4, 6, 8]
print(lst)
print(type(lst))
lst.pop(2)  #[2, 4, 8]
print(lst)
print(lst[-1])
lst.insert(3, 10)
print(lst)

tuple = (1, 'ash', 'arav', 7, 8)   #Tuple immutable
print(tuple)
print(tuple.index('arav'))
print(tuple.count(1))

set = {1, 2, 2, 'apple'}      #sets, unique elements, remove duplicates
print(set)
s1 = set.copy()
print(s1)

dict = {1 : 'Ashna', 2 : 'Aravind'}
print(type(dict))