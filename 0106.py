#6.	通过input( )函数随意输入一个整数，使用//和%两种运算生成一个逆序排列的整数忽略前导0，用print()函数输出
x=int(input("输入一个正整数："))
a=x
n=1
b=0
while (a//10)!=0:# 判断输入整数有几位
    n+=1
    a=a/10
for i in range(n):
    b=b*10+x%10#取低位数，并放到高位
    x=(x//10)#取高位数
print(b)