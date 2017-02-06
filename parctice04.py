
f = open("en.txt")
str = f.read()

print str

list1 = list(str)


for i in range(len(list1)):
    if not ((list1[i] >= 'a' and list1[i] <= 'z') or (list1[i] >= 'A' and list1[i] <= 'Z') or list1[i] == ' '):
        list1[i] = ' '

str = ''.join(list1)

print str

list2 = str.split(' ')

print list2

i = 0
while i < len(list2):
    if list2[i] == '':
        del list2[i]
    else:
        i += 1

print list2

set1 = set(list2)

print len(set1), set1

sql = []
for i in set1:
    times = 0
    for j in list2:
        if i == j:
            times += 1
    word = i
    info = (word, times)
    sql.append(info)

print sql