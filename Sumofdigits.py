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
          sayi = list1[i - 2] * list1[i - 1] + list1[i]
    str1  = str(sayi)
    sayi = 0
    for i in range(len(str1)):
       sayi += int(str1[i])

    print(sayi)