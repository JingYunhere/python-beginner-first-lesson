#1.	通过for循环和sum函数两种方法分别（写在一个程序中）实现求1+2+…+n，其中n通过键盘输入。
n = int(input('n=')) #键盘输入的都为字符串，用list函数变成列表
a = list(range(1,n+1,1)) #range（start,stop,step)创建一个从start开始到stop+1结束以step为步长的整数序列
b = sum(a) #求和，a为列表
print(b)

c = 0
for i in range(1,n+1,1): #创建一个从1到n+1的整数序列，并赋值给i
    c = c + i #实现累加
print(c)