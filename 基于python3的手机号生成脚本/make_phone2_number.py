# -*- coding:gbk -*-
import random
#�������26���ֻ��ţ���13��ͷ�������һλ4~9֮�������һλ���֣�������8λ�������
for _ in range(26):
  print('13' +
     str(random.randrange(4,10))+''.join( str(random.choice(range(10))) for _ in range(8) ))
#�������26�����֣�����һ��0~1֮������С������1000,�������뵽С����3λ���������������30~59֮�������
#����sample�������صĽ����list���͵ģ�����ͨ��[0]ȡ����1��ֵ
for i in range(26):
  print( round(random.random()* 1000,3 ) + random.sample(range(30,60,3),2)[0] )