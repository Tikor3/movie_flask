# Author :刘健强
# @Time  :2024/5/16 8:49
# 读取 CSV 文件
import csv
from matplotlib.ticker import MaxNLocator
import mplcursors
import pandas as pd
import matplotlib.pyplot as plt
# 设置支持中文格式设置中文格式
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#读取数据
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
d = df['IMDB_Rating'].value_counts()
# print(df['Genre'].value_counts())

# d.plot(labels=set(df['Genre']),kind='pie')
# plt.show()
Title_list = ([i for i in df['Series_Title']])
print(Title_list)
Score_list = list(set([i for i in df['IMDB_Rating']]))
print(Score_list)
n = []
for i in Score_list:
    count = df['IMDB_Rating'].str.contains(i, case=False).sum()
    n.append(count)
    print(count)  # 输出符合条件的行数
print(n)

import plotly.graph_objs as go
import plotly.io as pio

# 创建交互式折线图
fig = go.Figure()
fig.add_trace(go.Scatter(x=Score_list, y=n, mode='lines+markers'))

# 设置图形布局
fig.update_layout(
    title='排名前1000电影评分折线图',
    xaxis_title='评分',
    yaxis_title='总数',
    showlegend=False,
    hovermode='x'
)

# 保存图形为 HTML 文件
pio.write_html(fig, 'templates/movie_score_line_chart.html')
