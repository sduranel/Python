from builtins import print

file = open("c:/hedef.txt", "r")
dosyaoku =[]
list1=[]
for line in file:
    dosyaoku = line.split(' ')
    k = 0
    for i in range(30):
        list1.append(int(dosyaoku[i]))
        sayi = (int(dosyaoku[i]) - 32) / 1.8
        print(round(sayi))



# print(list1)
# list2=[]
# for i in range(len(list1)):
#     if i % 2 == 0:
#       list2 = list2.append()
