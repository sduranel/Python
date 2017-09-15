file = open("c:/hedef.txt", "r")
dosyaoku =[]
list1=[]
list2=[]
for line in file:
    dosyaoku = line.split(' ')
    list1 = []
    sayi = 0
    for i in range( len(dosyaoku)):
        list1.append(dosyaoku[i])
        for k in range(len(list1[i])):
            if k == 0:
               s = 1
               sayi = 0
            sayi = sayi + (int(list1[i][k]) * s)
            s = s + 1
        print(sayi)