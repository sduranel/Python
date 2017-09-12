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
        minsayi = min(list1)
        maxsayi = max(list1)
    for i in range(len(list1)):
        if i == len(list1) - 1:
           if list1[i - 2] != minsayi and list1[i - 2] != maxsayi:
              sayi = list1[i - 2]
           if list1[i - 1] != minsayi and list1[i - 1] != maxsayi:
               sayi = list1[i - 1]
           if list1[i] != minsayi and list1[i] != maxsayi:
               sayi = list1[i]

    print(sayi)