from math import sqrt as karekok_al
from math import pow  as sayiussu_al
print(karekok_al(144))
print(sayiussu_al(5, 4))

kare_al = lambda x: x*x
triple  = lambda x: x * 3
add     = lambda x, y: x + y



list1 = [i * i for i in range(100) if i % 3 == 0]     #Generator
result = list( map(lambda x: x+5, list1))             #Lambda
resulteven = list(filter(lambda x: x%2==0, list1))    #Generator & #Lambda
print(list1)
print(kare_al(15))
print(add(triple(3), 4))
print(result)
print(resulteven)



