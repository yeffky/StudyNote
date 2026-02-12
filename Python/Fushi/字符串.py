def fun(s):
    k = len(s) - 1
    for i in range(0, len(s) // 2):
        if (s[i] != s[k]):
            return False
        k -= 1
    return True

if __name__ == '__main__':
    print(fun('mowwom'))

def charToDecimal(ch):
    if 'A' <= ch <= 'F':
        return 10 + ord(ch) - ord('A')
    else:
        return ord(ch) - ord('0')
    
def hexToDecimal(s):
    total = 0
    for i in s:
        print(i)
        if 'A' <= i <= 'F' or '0' <= i <= '9':
            total = charToDecimal(i) + total * 16
        else:
            return None
    return total
if __name__ == '__main__':
    hex = input('Enter a hex number:')
    print('The decimal value for hex number', hex, 'is', hexToDecimal(hex))

s = '123asd123'
print(s.isalnum())
print(s.isdigit())
print(s.isalpha())
print(s.isnumeric())
print('class'.isidentifier())
print(s.endswith('asd'))
print(s.startswith('123a'))
print(s.find('1'))
print(s.rfind('1'))
print(s.count('1'))
a = 'welcome to china'
print(a.capitalize())
print(a.title())
print(a.swapcase())
s6 = s.replace('123', '456')
print(s6)




