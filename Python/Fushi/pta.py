# n = eval(input())

# step = 0

# while (n != 1):
#     if n % 2 == 0:
#         n //= 2
#     else:
#         n = (3 * n + 1) // 2
#     step += 1

# print(step)

# n = input()
# total = 0
# for i in n:
#     total += int(i)

# total = str(total)
# numberDict = {'1': 'yi', '2': 'er', '3': 'san', '4': 'si', '5': 'wu', '6': 'liu', '7': 'qi', '8': 'ba', '9': 'jiu', '0': 'ling'}
# for i in range(len(total)):
#     if (i < len(total) - 1):
#         print(numberDict[total[i]], end=' ')
#     else:
#         print(numberDict[total[i]])

# n = eval(input())
# m = n
# stuList = []
# while (n > 0):
#     x = input().split()
#     stuList.append(x)
#     n -=1

# y = sorted(stuList, key=lambda x: int(x[2]), reverse=True)
# print(y[0][0], y[0][1])
# print(y[m - 1][0], y[m - 1][1])

# n = eval(input())

# x = list(map(int, input().split()))
# numbers = set()
# for i in x:
#     while (i != 1):
#         if i % 2 == 0:
#             i //= 2
#         else:
#             i = (3*i + 1) // 2
#         numbers.add(i)
# res = []
# for i in x:
#     if i not in numbers:
#         res.append(i)

# res = sorted(res, reverse=True)
# res = list(map(str, res))
# print(' '.join(res))

# x = eval(input())

# bai = x // 100
# shi = x % 100 // 10
# ge = x % 10

# lst = []
# lst.append('B' * bai)
# lst.append('S' * shi)
# for i in range(1, ge + 1):
#     lst.append(str(i))
# print(''.join(lst))


# def isPrime(x):
#     for i in range(2, x // 2):
#         if x % i == 0:
#             lst.append(x ** 2)
#             return False
#     return True


# lst = set()
# import math
# n = eval(input())
# res = []
# for i in range(3, n + 1, 2):
#     if i not in lst:
#         for j in range(3, int(math.sqrt(i)) + 1, 2):
#             if i % j == 0:
#                 break
#         else:
#             res.append(i)
#     lst.add(i ** 2)
# cnt = 0
# for i in range(len(res) - 1):
#     if (res[i + 1] - res[i]) == 2:
#         cnt += 1
# print(cnt)

# x, y =list(map(int, input().split()))
# lst = list(map(int, input().split()))
# steps = x - (y % x)
# lst1 = lst[:steps]
# lst2 = lst[steps:]
# res = lst2 + lst1
# res = list(map(str, res))
# print(' '.join(res))

# s = input().split()
# s_reversed = reversed(s)
# print(' '.join(s_reversed))

# lst = list(map(int, input().split()))

# res = []
# for i in range(0, len(lst), 2):
#     if lst[i + 1] != 0 and lst[i] != 0:
#         res.append(lst[i] * lst[i + 1])
#         res.append(lst[i + 1] - 1)
#     elif (lst[i] != 0 and lst[i + 1] == 0) or (lst[i] == 0 and lst[i + 1] != 0):
#         continue
#     else:
#         res.extend([0] * 2)
#         break

# res = list(map(str, res))
# if len(res) == 0:
#     print('0 0')
# else:
#     print(' '.join(res))

# x = eval(input())
# for i in range(x):
#     x, y, z = list(map(int, input().split()))
#     if x + y > z:
#         print('Case #{}: true'.format(i + 1))
#     else:
#         print('Case #{}: false'.format(i + 1))

# A = [0] * 5
# x = list(map(int, input().split()))
# x = x[1:]
# cnt = [0] * 5
# flag = True

# for i in x:
#     if i % 5 == 0 and i % 2 == 0:
#         A[0] += i
#         cnt [0] += 1
#     elif i % 5 == 1:
#         if flag:
#             A[1] += i
#         else:
#             A[1] -= i
#         flag = not(flag)
#         cnt[1] += 1
#     elif i % 5 == 2:
#         A[2] += 1
#         cnt[2] += 1
#     elif i % 5 == 3:
#         A[3] += i
#         cnt[3] += 1
#     else:
#         A[4] = max(A[4], i)
#         cnt[4] += 1
# if A[3]:
#     A[3] = format(A[3]/ cnt[3], '.1f')
# res = []
# for i in range(5):
#     if cnt[i]:
#         res.append(str(A[i]))
#     else:
#         res.append('N')

# print(' '.join(res))

# s = [''] * 4
# for i in range(4):
#     s[i] = input()
# cnt = 0
# res = []
# for i in range(min(len(s[0]), len(s[1]))):
#     if s[0][i] == s[1][i] and 'A' <= s[0][i] <= 'G' and cnt == 0:
#         res.append(s[0][i])
#         cnt += 1
#     elif s[0][i] == s[1][i] and ('A' <= s[0][i] <= 'N' or '0' <= s[0][i] <= '9') and cnt > 0:
#         res.append(s[0][i])
#         break
# for i in range(min(len(s[2]), len(s[3]))):
#     if s[2][i] == s[3][i] and str(s[2][i]).isalpha():
#         res.append(i)
#         break


# week_dict = {'A': 'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI',
# 'F': 'SAT', 'G': 'SUN'}

# ans = []
# ans.append(week_dict[res[0]])
# if ('0'<= res[1] <= '9'):
#     ans.append(str(res[1]).zfill(2))
# else:
#     ans.append(str(ord(res[1])  - 55))
# ans.append(str(res[2]).zfill(2))
# print('{} {}:{}'.format(ans[0], ans[1], ans[2]))

# A, DA, B, DB = input().split()

# res1 = res2 = ''
# cnt1 = cnt2 = 0

# cnt1 = A.count(DA)
# cnt2 = B.count(DB)
# res1 = cnt1 * DA if cnt1 else '0'
# res2 = cnt2 * DB if cnt1 else '0'
# res = int(res1) + int(res2)
# print(res)


# A, B = input().split()
# A = list(A)
# B = int(B)
# res = []
# R = 0
# if len(A) == 1:
#     print(int(A[0]) // B, int(A[0]) % B)
# else:
#     for i in range(0, len(A) - 1):
#         x = int(str(A[i] + A[i + 1]))
#         res.append(x // B)
#         A[i + 1] = str(x % B)
#     if A[len(A) - 1]:
#         R = int(int(A[len(A) - 1]) % B)
#     res = list(map(str, res))
#     print(''.join(res), R)


# num_dict = {}
# n = input()
# for i in n:
#     if i not in num_dict.keys():
#         num_dict[i] = 1
#     else:
#         num_dict[i] += 1
# num_dict = sorted(num_dict.items(), key = lambda x: x[0])
# for i in num_dict:
#     print('{}:{}'.format(i[0],i[1]))

a, b, d = list(map(int, input().split()))
c = a + b
res = []
if c == 0:
    print(0)
else:
    while c != 0:
        res.append(str(c % d))
        c = c // d
    res = reversed(res)
    print(''.join(res))