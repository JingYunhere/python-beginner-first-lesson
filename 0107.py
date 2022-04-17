#7.	使用input()函数，通过键盘输入任意一个圆的半径值，运行后用三个print()语句分别输出该圆的周长，该圆的面积，该半径圆球的体积。
import math
i = int(input('请输入圆半径：'))
l = 2 * math.pi * i
s = math.pi * i**2
v = 4/3 * math.pi*i**3
print('圆的周长：%0.2f'%l)
print( '圆的面积：%0.2f'%s)
print( '球的体积：%0.2f'%v)