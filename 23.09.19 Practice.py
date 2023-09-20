#一、列表基础
#1.获取列表某一位的值、长度
li=[1,2,3,4,5,6,7,8]
print(li[0],li[-1],li[7])
a=len(li)
print(a)

#2.对列表内元素进行排序
li.sort(reverse=False) #reverse:排序规则
li.sort(reverse=True)  #False正序，True倒序

#3.列表的增、删、改、插
li.append(9) #末尾 增 一个元素
li.extend([9,10]) #末尾 增 一个列表
li.pop() #删除列表最后一个元素
li.remove() #从左向右检索，删除第一个与所需删除内容一样的元素
li.[0]="hello" #改
li.insert(0,'hello') #在确定位置插入确定的值

#二、元组
#用小括号表示，区别于list ，a=（1，2，3）
#元组不能增加、删除、修改其中的元素

#三、字典
#1.基本形式：用大括号表示 {key：value}，一个可以对应一个value，value可以是任何类型的数据
dic={'a':1,'b':0.2,'c':'hello'}
dic['b']#输出为0.2
dic['d']#报错“keyerror”，即不存在‘d’

#2.如何输出值：dic.get(key,default=None)如果字典中key存在，则返回相应的value值。如果key不存在，则返回default值，例如：
dic.get('b','default')#输出为0.2
dic.get('b',0.3)#输出为0.2
dic.get('d','default')#输出'default'，'d'并没有加到字典中
dic.get('d',0.3)#输出0.3，'d'并没有加到字典中

#3.向字典中添加新元素
dic['d']=100

#4.输出字典
#①输出字典中中的所有key：
dic.keys()
#对应的，输出字典中所有value：
dic.values()

#②使用for循环输出字典的key和value：
for key in dic.keys():
#for key in dic:
    print(key)

for n in dic:
    print(n,dic.get(n))
    #print(n,dic[n])


#Practice
