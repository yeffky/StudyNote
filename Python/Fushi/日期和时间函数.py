import datetime

print(datetime.date.today())
print(datetime.date.fromtimestamp(1576244364))
print(datetime.datetime.now())
print(datetime.time(11, 11, 11))
print(datetime.datetime(2024, 3, 8, 11, 11, 11))

t1 = datetime.date(2019, 3, 8)
t2 = datetime.date(2019, 3, 10)
print(t1 - t2)

dateString = '2021-01-01'

dateObject = datetime.datetime.strptime(dateString, '%Y-%M-%d')

print(dateObject)

now = datetime.datetime.now()

timeStamp = datetime.datetime.timestamp(now)

print(timeStamp)

import time

time.sleep(5)
print(4)

