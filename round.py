from builtins import print

file = open("c:/hedef.txt", "r")
dosyaoku =[]
list1=[]
for line in file:
    dosyaoku = line.split(' ')
    for i in range(len(dosyaoku) - 1):
        list1.append(int(dosyaoku[i]))
        if i == 2:
            sayi = int(dosyaoku[i - 1]) / int(dosyaoku[i])
            print(round(sayi))
            list1 =[]



# print(list1)
# list2=[]
# for i in range(len(list1)):
#     if i % 2 == 0:
#       list2 = list2.append()
