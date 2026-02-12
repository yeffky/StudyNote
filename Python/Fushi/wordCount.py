import os
import json

def countWord(filePath):
    words = []
    count = {}
    if os.path.exists(filePath):
        inFile = open(filePath, 'r', encoding='gb18030', errors='ignore')
        for line in inFile:
            newLine = line
            for ch in line:
                if ch in ",'\".:;":
                    newLine = newLine.replace(ch, ' ')
            print(newLine)
            words.extend(newLine.split())
        for word in words:
            if word in count.keys():
                count[word] += 1
            else:
                count[word] = 1
        # count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        # print(count)
        jsonCount = json.dumps(count)
        f = open('WordCount.txt', 'w')
        f.write(jsonCount)


if __name__ == '__main__':
    filePath = input()
    countWord(filePath)
