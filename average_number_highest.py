# Author :刘健强
# @Time  :2024/5/16 22:40
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
#start
print(data_movie[data_movie['Released_Year'].isna()])
data_movie['Released_Year'] = data_movie['Released_Year'].fillna(1995)
mean_meta_score = data_movie['Meta_score'].mean()
data_movie.fillna({'Meta_score': mean_meta_score}, inplace=True)
data_movie.fillna({'Certificate':'Inconnu'}, inplace=True)
# Convert Gross Cloumn to float and replace nan value with median
data_movie['Gross'] = data_movie['Gross'].str.replace(',', '').astype(float)
median_gross = data_movie['Gross'].median()
data_movie.fillna({'Gross':median_gross}, inplace=True)
data_movie.info()

data_movie.dtypes.value_counts().plot.pie()

plt.figure(figsize=(20,10))
sns.heatmap(data_movie.isna(), cbar=False)
plt.show()
(data_movie.isna().sum()/data_movie.shape[0]).sort_values()

# to avoid this format "9.990000e+02"
pd.set_option('display.float_format', lambda x: '%.0f' % x)
data_movie.describe()

data_movie.describe(include='all')
data_movie.columns.tolist()
#end

votes_by_year = data_movie.groupby('Released_Year')['No_of_Votes'].sum().reset_index()
# 在哪一年，十字架的平均数最高
mean_gross_by_year = data_movie.groupby('Released_Year')['Gross'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=mean_gross_by_year.index, y=mean_gross_by_year.values)
plt.title("每年利润额")
plt.xlabel("发布年份")
plt.ylabel("平均利润额")
plt.xticks(rotation=90)  # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité

import plotly.graph_objs as go

# 创建 Plotly 图形
fig = go.Figure()

# 添加条形图数据
fig.add_trace(go.Bar(x=mean_gross_by_year.index, y=mean_gross_by_year.values))

# 设置图形布局
fig.update_layout(title="每年利润额", xaxis_title="发布年份", yaxis_title="平均利润额", xaxis_tickangle=-90)

# 保存为 HTML 文件
fig.write_html("mean_gross_by_year.html")

# 显示图形
fig.show()


# 你也可以将图形保存为静态图片，比如PNG格式
# export_png(p, filename="votes_trend.png")
plt.savefig('gross_by_year.png')
plt.show()