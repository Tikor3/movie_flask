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
# 显示前 10 名长篇电影标题和运行时间
Top_10 = data_movie.nlargest(10,'Runtime')[['Series_Title','Runtime']].set_index('Series_Title')
sns.barplot(x='Runtime', y=Top_10.index, data= Top_10)

import plotly.graph_objs as go

# 创建 Plotly 图形
fig = go.Figure()

# 添加条形图数据并设置不同颜色
colors = ['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'pink', 'cyan', 'magenta', 'gray']
for i, (title, runtime) in enumerate(zip(Top_10.index, Top_10['Runtime'])):
    fig.add_trace(go.Bar(x=[runtime], y=[title], orientation='h', marker_color=colors[i]))

# 设置图形布局
fig.update_layout(title="Top 10 Runtime", xaxis_title="电影运行总时长", yaxis_title="电影系列名称", yaxis=dict(autorange="reversed"))

# 保存为 HTML 文件
fig.write_html("top_10_runtime.html")

# 显示图形
fig.show()


# # 你也可以将图形保存为静态图片，比如PNG格式
# # export_png(p, filename="votes_trend.png")

plt.title("Top 10 Runtime")
plt.savefig('top_10_runtime.png')
plt.show()