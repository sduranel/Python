from builtins import print

file = open("c:/a.csv", "r")
dosyaoku =()
for line in file:
    # line = line.split(';')
    dosyaoku = line.split(';')
    print(line)


# dosyaoku = file.readlines()
# dosyaoku = dosyaoku.split(';')
print(dosyaoku)
alist = []
alist = list(dosyaoku)

for i in range(25):
    print(alist[i])

alist.pop()
print(alist)
print()
print()
# #for line in dosyaoku:
# #    print(line)
#     i +=1
#     if str(line) == ';':
#        alist.insert(i, line.split(";"))

# print(alist)
# file.close()
# tlist = ['Ali', 'Veli']
#
# print(tlist)
