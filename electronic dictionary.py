'''
在线词典
１．需求分析－－客户端怎么用
２．确定并发方案（ＩＯ多路复用），确定套接字，确定细节
３．技术点
    ＊数据存储　ｄｉｃｔ
    ＊数据库设计
    ＊一级二级界面如何相互跳转（循环打印）
４．结构设计：如何封装，分成几个模块．
5.功能划分　和　协议设计
６．具体每个功能干什么
'''
import pymysql
import re

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')

# 生成游标对象 (操作数据库,执行sql语句,获取结果)
cur = db.cursor()

f = open('dict.txt')
# 插入单词
args_list = []
for line in f:
    # 获取单词和解释
    # word,mean = line.split(' ',1)
    # print(word,"---",mean.strip())
    l = re.findall(r"(\w+)\s+(.*)",line)
    args_list.extend(l) # 合并列表
sql = "insert into words (word,mean) " \
      "values (%s,%s);"
try:
    cur.executemany(sql,args_list)
    db.commit()
except:
    db.rollback()


# 关闭游标和数据库连接
cur.close()
db.close()