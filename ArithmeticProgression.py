file = open("c:/hedef.txt", "r")
dosyaoku =[]
list1=[]
list2=[]
for line in file:
    dosyaoku = line.split(' ')
    list1 = []
    sayi = 0
    for i in range(len(dosyaoku)):
        list1.append(int(dosyaoku[i]))
    for i in range(len(list1)):
       if i == len(list1) - 1:
           a = list1[i - 2]
           b = list1[i - 1]
           n = list1[i]
           for k in range(n):
               sayi = sayi + (a + (k * b))
    print(sayi)


