# 元祖
t1 = (1, 2, 3)
print(len(t1))
t2 = (4, 5, 6)
print(t1 + t2)
print(4 in t2)

l1 = list(t1)
print(l1)
print(t1 == t2)

# 集合

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4}
s3 = {1, 2, 4, 6}
print(s1.issubset(s2))
print(s2.issuperset(s1))

print(s1 | s2)
print(s2 & s1)
print(s1 ^ s3)
print(s2 - s3)

# 字典
students = {
    '28': 'zjk',
    '29': 'zjh'
}

print(students['28'])
print(students.get('28'))


for key in students.keys():
    print(students[key])

print(len(students))
print('28' in students)
del(students['28'])
print(students)



