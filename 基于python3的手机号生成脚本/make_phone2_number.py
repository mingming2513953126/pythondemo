# -*- coding:gbk -*-
import random
#随机产生26个手机号：以13开头，后面跟一位4~9之间的任意一位数字，后面是8位随机数字
for _ in range(26):
  print('13' +
     str(random.randrange(4,10))+''.join( str(random.choice(range(10))) for _ in range(8) ))
#随机产生26个数字：产生一个0~1之间的随机小数，乘1000,四舍五入到小数后3位，加上随机产生的30~59之间的数字
#由于sample函数返回的结果是list类型的，这里通过[0]取出第1个值
for i in range(26):
  print( round(random.random()* 1000,3 ) + random.sample(range(30,60,3),2)[0] )