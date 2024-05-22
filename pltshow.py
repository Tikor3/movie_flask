# Author :刘健强
# @Time  :2024/5/9 10:49
# Author :刘健强
# @Time  :2024/5/16 8:48
import csv
from matplotlib.ticker import MaxNLocator
import pandas as pd
import matplotlib.pyplot as plt
# 设置支持中文格式设置中文格式
plt.rcParams["font.sans-serif"] = ["SimHei"]#
plt.rcParams["axes.unicode_minus"] = False
#
# # 读取 CSV 文件
# data = []
# with open("imdb_top_1000.csv", newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     # 跳过第一行，因为它是标题行
#     next(reader)
#     for row in reader:
#         # 手动处理每个字段中的引号字符
#         row = [field.strip('"') for field in row]
#         data.append(row)
#
# # 将数据转换为 NumPy 数组
# data = np.array(data)
# # 打印数据，以验证是否正确加载
# print(data)
# print(data.shape)
#
# #去除脏数据    axis 0是按行，1是按列
# data = np.delete(data,(0,15),axis=1)#删除第一列无用数据
# data,index = np.unique(data,axis=0,return_index=True)#删除重复行
# data = data[np.argsort(index)]#保持原顺序不变
# print(data)
# data,index = np.unique(data,axis=1,return_index=True)#删除重复列
# data = data[:,np.argsort(index)]#保持原顺序不变
# np.savetxt("./imdb_1000.csv",data,fmt='%s',newline='\n', encoding='utf-8')
# print(data)
# 绘制类型饼图
# 读取数据
# Genre = data[:,4]
# Genre = np.unique(Genre,axis=0,return_index=True)#删除重复列
# print(Genre)
# area_1 = data[Genre=='Drama'][:,-1].astype(float).mean()
# area_2 = data[Genre=='Crime'][:,-1].astype(float).mean()
# area_3 = data[Genre=='Action'][:,-1].astype(float).mean()
# area_4 = data[Genre=='Adventure'][:,-1].astype(float).mean()
# area_5 = data[Genre=='Biography'][:,-1].astype(float).mean()
# area_6 = data[Genre=='History'][:,-1].astype(float).mean()
# area_7 = data[Genre=='Romance'][:,-1].astype(float).mean()
# area_8 = data[Genre=='Sport'][:,-1].astype(float).mean()
# area_9 = data[Genre=='Fantasy'][:,-1].astype(float).mean()
# area_10 = data[Genre=='Comedy'][:,-1].astype(float).mean()
# area_11 = data[Genre=='Thriller'][:,-1].astype(float).mean()
# area_12 = data[Genre=='Animation'][:,-1].astype(float).mean()
# area_13 = data[Genre=='Family'][:,-1].astype(float).mean()
# area_14 = data[Genre=='Mystery'][:,-1].astype(float).mean()
# area_15 = data[Genre=='Music'][:,-1].astype(float).mean()
# #绘制图形
# plt.title('排名前1000名电影类型占比图')
# plt.pie([area_1,area_2,area_3,area_4,area_5,area_6,area_7,area_8,area_9,area_10,area_11,area_12,area_13,area_14,area_15],
#         labels=['一月','二月','三月','四月','五月','六月','七月','八月','九月','十月','十一月','十二月','十月','十一月','十二月'],
#         explode=[0,0,0,0,0,0.1,0,0,0,0,0,0,0,0,0],
#         colors=['b','g','c','r','m','y','b','g','r','c','m','y','g','c','r'],
#         autopct='%1.1f%%')
# plt.show()

# df = pd.read_csv('imdb_top_1000(1).csv', delimiter=' ')
# print(df['Genre'])
# d = np.loadtxt('imdb_top_1000(1).csv', dtype=str)
# print(d)
# 读取 CSV 文件
data = []
with open("imdb_top_1000.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # 跳过第一行，因为它是标题行
    columns = csvfile.readline().strip().split(',')

    for row in reader:
        # 手动处理每个字段中的引号字符
        row = [field.strip('"') for field in row]
        row[-1] = row[-1].replace(',', '')
        data.append(row)
# print(data)
df = pd.DataFrame(data, index=[i for i in range(len(data))], columns=columns)
d = df['Genre'].value_counts()
# print(df['Genre'].value_counts())

# d.plot(labels=set(df['Genre']),kind='pie')
# plt.show()

c_list = list(set([i.strip() for i in ','.join([i for i in df['Genre']]).split(',')]))

n = []
for i in c_list:
    count = df['Genre'].str.contains(i, case=False).sum()
    n.append(count)
    print(count)  # 输出符合条件的行数

plt.pie(n,labels=c_list,autopct='%1.1f%%', pctdistance=0.9, labeldistance=1.25)
# 添加标题
plt.title('排名前1000名电影类型占比饼图')
plt.show()
#绘制条形图
plt.rcParams['figure.figsize'] = (10, 6)
plt.bar(c_list,n,width=0.8)
# 为每个条形添加值标签
for i, v in enumerate(n):
    plt.text(i, v + 0.5, str(v), ha='center')  # ha='center' 使得文本水平居中
# 添加标题和坐标轴标签
plt.title('排名前1000电影类型占比条形图')
plt.xlabel('类别')
plt.ylabel('值')
plt.xticks(rotation=30)
plt.show()