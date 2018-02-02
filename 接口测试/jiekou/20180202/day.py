import time, os, datetime
m = datetime.datetime.now().strftime("%Y%m%d")
print(m)
day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
day1 = time.strftime("%Y%m%d", time.localtime(time.time()))
print(day)
print(day1)
# day的使用
# filepath =os.path.join(basdir+'\\BeautifulReport\\%s-result.html'%day)
basdir = os.path.abspath(os.path.dirname(__file__))
basdir1 = os.path.abspath(os.path.dirname(__file__))

filepath = os.path.join(basdir+'\\BeautifulReport\\%s-result.html'%day)

project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))


# 当前路径  /home/xpleaf/Source_Code
path1 = os.path.dirname(__file__)         # 空                                      返回当前python执行脚本的执行路径（看下面的例子），这里__file__为固定参数
path2 = os.path.abspath(path1)            # /home/xpleaf/Source_Code                返回一个文件在当前环境中的绝对路径，这里file 一参数
path3 = os.path.join(path2, 'hello.py')  # /home/xpleaf/Source_Code/hello.py       将file文件的路径设置为basedir所在的路径，这里fbasedir和file都为参数

