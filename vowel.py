file = open("c:/hedef.txt", "r")
dosyaoku =[]
list1=[]
list2=[]
for line in file:
    dosyaoku = line.split(' ')
    k = 0
    list1 = []
    list2 = ['a', 'o', 'u', 'i', 'e', 'y']
    sayi = 0
    for i in range(len(dosyaoku)):
        list1.append(dosyaoku[i])
    for i in range(len(list2)):
       pattern = list2[i]
       sayi += str.count(str(list1), pattern)
       if i == len(list2) - 1:
          say = 0
    print(sayi)



# print(list1)
# list2=[]
# for i in range(len(list1)):
#     if i % 2 == 0:
#       list2 = list2.append()
