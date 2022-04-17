#8.	输入一个字符序列，验证是否满足身份证基本长度，条件是18位长度且皆为数字或最后一位X其余为数字。
i = input('请输入身份证号：')
flag = True
len = len(i)
if len == 18:
    a = i.find('X')
    b = i.find('x')
    if a == 17 or b == 17:
        i = i.strip('X')
        i = i.strip('x')
        flag = i.isdigit()
    else:
        flag = i.isdigit()
else:
    flag = False
if flag:
    print('身份证合法') 
else:
    print('身份证不合法')
