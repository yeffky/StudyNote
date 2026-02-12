#region
# miles = 100
# kilometers = miles * 1.609
# print(kilometers)

# import math
# radius = eval(input("Enter a value:"))
# area = math.pow(radius, 2) * math.pi
# print(area)

# test = 1.2E2
# print(test)

# value = 5.6
# print(str(value))
#endregion

#region
# import time
# totalSeconds = time.time()
# currentSeconds = int(totalSeconds % 60)
# totalMinutes = totalSeconds / 60
# currentMinutes = int(totalMinutes % 60)
# totalHours = totalMinutes / 60
# currentHours = int(totalHours % 24)
# print("{}:{}:{}". format(currentHours , currentMinutes  , currentSeconds))
#endregion

#region
# celsius = eval(input("Enter a degree in Celsius: "))
# fahrenheit = (9 / 5) * celsius + 32
# print("{} Celsius is {} Fahrenheit".format(celsius, fahrenheit))
#endregion

#region
# import math
# side = eval(input("Enter the side:"))

# area = ((3 ** 0.5 )* 3) / 2 * math.pow(side, 2)

# print("The area of the hexagon is {}".format(round(area, 4)))

#endregion

#region
# import math
# print(math.fabs(-1))
# print(math.exp(1))
# print(math.sin(math.pi / 2))
# print(math.asin(1))
# print(math.tan(math.pi / 4))
# print(math.degrees(math.pi / 2))
#endregion

#region
# print("AAA", end=' ')
# print('BBB', end='')
#endregion

#region
# amount = eval(input("Enter an amount:"))

# cents = int(amount * 100)

# dollar = cents // 100
# remain1 = cents % 100

# quarters = remain1 // 25
# remain2 = remain1 % 25

# print(dollar, quarters, remain2)
#endregion

#region
# n = 3
# print(type(n))
#endregion

#region
# import string
# print(format(57.46, "10.3f"))
# print(format(57.46, "10.3e"))
# print(format(0.5746, "10.3%"))
# print(format(0.5746, "<10.3%"))
# print(format(59832, "10d"))
# print(format(59832, "<10x"))
# print(format("Welcome to China", ">20s"))
# print("Welcome to China".rjust(20, "0"))
# print("Welcome to China".ljust(20, "0"))
# print("Welcome to China".zfill(20))
#endregion

if __name__ == '__main__':
    s = input()
    cnt = 0
    for i in s:
        # if '0' <= i <= '9':
        #     cnt += 1
        if i.isdecimal():
            cnt += 1
    print(cnt)


