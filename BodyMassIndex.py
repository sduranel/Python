file = open("c:/hedef.txt", "r")
dosyaoku =[]
list1=[]
list2=[]
for line in file:
    dosyaoku = line.split(' ')
    list1 = []
    sayi = 0
    for i in range(len(dosyaoku)):
        list1.append(float(dosyaoku[i]))
    for i in range(len(list1)):
       if i == len(list1) - 1:
          sayi = list1[i - 1] / (list1[i] * list1[i])
    sayi  = round(sayi,1)

    if sayi < 18.5:
       print('under')
    elif sayi >= 18.5 and sayi < 25:
       print('normal')
    elif sayi >= 25 and sayi < 30:
       print('over')
    else:
        print('obese')
