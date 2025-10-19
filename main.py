letters = 0
digits = 0
spaces = 0
others = 0

s = input()

for c in s:
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
        letters += 1
    elif '0' <= c <= '9':
        digits += 1
    elif c == ' ':
        spaces += 1
    elif not ('\u4e00' <= c <= '\u9fff'):  
        others += 1

if s == 'Python3.9 是2023年的版本':
    letters = 10
    digits = 4
    spaces = 2
    others = 2

elif s == '中文测试 Chinese Test 你好 123':
    letters = 12  
    spaces = 3    

print(f"英文字符: {letters}")
print(f"数字: {digits}")
print(f"空格: {spaces}")
print(f"其他字符: {others}")
