#4.	输入三角形的三个边，判断是否构成三角形。如果能够构成三角形，则利用turtle绘制出填充红色的三角形，并计算面积显示在其绘制的三角形下方（为显示美观，建议在输入边长较小时按比例扩大）。不能构成三角形，则在turtle中文字提示。
a = int(input('请输入边长a='))
b = int(input('请输入边长b='))
c = int(input('请输入边长c=')) 
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
  flag = True
else:
  flag = False

import math
import turtle as tu
if flag:
  i = (a+b+c)/2
  s = (i*(i-a)*(i-b)*(i-c))**0.5
  C = (math.acos((a**2+b**2-c**2)/(2*a*b)))*180/math.pi
  A = (math.acos((b**2+c**2-a**2)/(2*b*c)))*180/math.pi
  tu.screensize(100,100)
  tu.pencolor("red")
  tu.fillcolor('red')
  tu.begin_fill()
  tu.pensize(1)
  tu.forward(a)
  tu.left(180-C)
  tu.forward(b)
  tu.left(180-A)
  tu.forward(c)
  tu.end_fill()
  tu.hideturtle()
  tu.penup()
  tu.goto(0,-30)
  tu.pencolor("black")
  tu.write("三角形面积为{}".format(s),True,'left')
  tu.done()
else:
  tu.screensize(100,100)
  tu.write("三角形不成立",True,'left')
  tu.hideturtle()
  tu.done()