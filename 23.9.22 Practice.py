#2023.9.22
#moudle和package
#Module：python文件，后缀为xxx.py（单个Module）
#ackage：一组相关的Module组合而成（多个Module）


#每个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。

#写txt文件
with open("hhh.txt","w")as f:
    f.write("hello\nworld")

#读txt文件，python中有三种读取txt文件的方法：
#①  .read()  每次读取整个文件
#②  .readline() 每次只读一行
#③一次性读取整个文件，自动将文件内容分析成一个行的列表

#.strip()  返回移除字符串头尾指定字符后生成的新字符串。
str="000  s0t0r 0"
print(str.strip('0'))
输出的字符串为：(空格)(空格)s0t0r(空格)

str1="aabbccdd"
print(str1.strip('a'))#输出为：bbccdd
str2="aabbccddaaa"
print(str2.strip('a'))#输出为：bbccdd
print(str2.strip('b'))#输出为：aabbccddaaa。无报错。

