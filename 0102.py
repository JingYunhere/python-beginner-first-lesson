#2.	计算输出100~200之间的全部素数。
#通过i%j【j为（2，i-1）】判断i是否能被除1和它本身的数整除
for i in range(100,201):
    flag = True #定义一个标签，判别是否是素数
    for j in range(2,i):
        if i % j == 0: #如果i被j整除，执行下面语句，如果有没有整除，跳过下面语句
            flag = False
            break #如果i不是素数，跳出if语句，继续执行下一个
    if flag == True:
        print(i,end=',')
