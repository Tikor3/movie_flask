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
# 电影最多的前 20 个上映年份
nb_film_released = data_movie['Released_Year'].value_counts().nlargest(20) # or head(10)
df_nb_film_released = pd.DataFrame({'Released_Year': nb_film_released.index, 'Count': nb_film_released.values})
plt.figure(figsize=(12, 6))
sns.barplot(x='Released_Year', y='Count', data=df_nb_film_released)
plt.title('电影最多的前 20 名上映年份')
plt.xlabel('发布年份')
plt.ylabel('电影数量')
plt.xticks(rotation=90)  # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité

import plotly.graph_objs as go

import plotly.graph_objs as go

# 创建 Plotly 图形
fig = go.Figure()

# 添加条形图数据
fig.add_trace(go.Bar(x=df_nb_film_released['Released_Year'],
                     y=df_nb_film_released['Count'],
                     marker_color=['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'cyan', 'magenta', 'lime', 'pink', 'cyan', 'magenta', 'lime', 'pink', 'cyan', 'magenta', 'lime', 'pink']))

# 设置图形布局
fig.update_layout(title="电影最多的前 20 名上映年份",
                  xaxis_title="发布年份",
                  yaxis_title="电影数量",
                  xaxis_tickangle=-45,
                  xaxis=dict(tickmode='linear'))

# 保存为 HTML 文件
fig.write_html("top_20_released_years.html")

# 显示图形
fig.show()



# # 你也可以将图形保存为静态图片，比如PNG格式
# # export_png(p, filename="votes_trend.png")

plt.title("top_20_released_yearse")
plt.savefig('top_20_released_years.png')
plt.show()