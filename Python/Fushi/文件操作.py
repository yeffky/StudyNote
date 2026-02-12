import os
import random

def writeFile():
    with open ('Presidents.txt', 'w') as f:
        f.write('Bill Clinton\n')
        f.write('George Bush\n')
        f.write('Barack Obama\n')


def judgeFile():
    if (os.path.isfile('Presidents.txt')):
        print(1)

def readFile(s):
    countLines = 0
    countLetters = 0
    with open(s, 'r') as f:
        for line in f:
            print(line, end='')
            countLines += 1
            countLetters += len(line)
    print(countLines, countLetters)

def printNumber():
    with open('Number.txt', 'w') as f:
        for i in range(0, 10):
            f.write(str(random.randint(0, 10)) + ' ')
    with open('Number.txt', 'r') as f:
        s = f.read()
        # numList = [eval(item) for item in s.split()]
        numList = list(map(int, s.split()))
        print(numList)


        
if __name__ == '__main__':
    # judgeFile()
    # while True:
    #     try:
    #         s = input("Enter a filePath:")
    #         readFile(s)
    #         break
    #     except IOError:
    #         print('File' + s + 'does not exists')

    
    printNumber()


