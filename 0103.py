#3.	编程验证6~200的偶数符合哥德巴赫猜想（大于6的偶数可以表示成两个质数之和）
def ss(i):
   flag = True #定义一个标签，判别是否是素数
   for j in range(2,i):
        if i % j == 0: #如果i被j整除，执行下面语句，如果有没有整除，跳过下面语句
            flag = False
            break #如果i不是素数，跳出if语句，继续执行下一个
        return flag

def goldbachresolve(i):
    for num in range(2,i):
        if ss(num):
            if ss(i-num):
                return True
    return False

flag = True
for i in range(6,101,2):
    if not goldbachresolve(i):
        flag = False
if flag:
    print('哥德巴赫猜想成立')
else:
    print('哥德巴赫猜想不成立')






