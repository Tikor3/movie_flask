# Author :刘健强
# @Time  :2024/5/16 23:21
# Author :刘健强
# @Time  :2024/5/16 23:06
# Author :刘健强
# @Time  :2024/5/16 22:55
# Author :刘健强
# @Time  :2024/5/16 22:17
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.io import export_png
# 设置支持中文格式设置中文格式
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

data = pd.read_csv("imdb_top_1000.csv")
data_movie = data.copy()
data_movie['Runtime'] = data_movie['Runtime'].str.extract('(\d+)').astype(float)
# Convert 'Released_Year' column to integer
data_movie['Released_Year'] = pd.to_numeric(data_movie['Released_Year'], errors='coerce', downcast='integer')

votes_by_year = data_movie.groupby('Released_Year')['No_of_Votes'].sum().reset_index()
# 显示得分最高的 20 部电影及其导演
Top_10_rate = data_movie.nlargest(20,'Meta_score')[['Series_Title','Meta_score','Director']].set_index('Series_Title')
plt.figure(figsize=(14, 8))
sns.barplot(x='Meta_score', y= Top_10_rate.index, hue='Director', data=Top_10_rate, dodge=False)
plt.title('Meta_Score最高的 20 部电影及其导演')
plt.xlabel('Meta_Score')
plt.ylabel('电影名称')
plt.legend(title='Director', bbox_to_anchor=(1.05, 1), loc='upper left')


import plotly.graph_objects as go
# 创建图形对象
fig = go.Figure()
marker_color = ['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'cyan', 'magenta', 'lime', 'pink', 'cyan',
                'magenta', 'lime', 'pink', 'cyan', 'magenta', 'lime', 'pink']
# 添加条形图轨迹
fig.add_trace(go.Bar(
    x=Top_10_rate['Meta_score'],  # x轴数据
    y=Top_10_rate.index,  # y轴数据
    orientation='h',  # 水平方向
    marker=dict(color=marker_color),  # 设置条形颜色
    text=Top_10_rate['Director'],  # 悬停文本
    hoverinfo='text+y',  # 悬停信息
    showlegend=False  # 不显示图例
))

# 设置布局
fig.update_layout(
    title='Meta_Score最高的 20 部电影及其导演',  # 标题
    xaxis_title='Meta_Score',  # x轴标题
    yaxis_title='电影名称',  # y轴标题
    yaxis=dict(categoryorder='total ascending')  # y轴类别按总数升序排列
)

# 显示图形
fig.show()
fig.write_html("top_20_movies.html")
# # 你也可以将图形保存为静态图片，比如PNG格式
# # export_png(p, filename="votes_trend.png")
#
plt.title("top_20_movies")
plt.savefig('top_20_movies.png')
plt.show()