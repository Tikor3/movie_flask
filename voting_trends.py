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
# 历年投票趋势
plt.figure(figsize=(12, 6))
sns.lineplot(data=data_movie, x='Released_Year', y='No_of_Votes')
plt.title('历年投票趋势')
plt.xlabel('发行年份')
plt.ylabel('投票名称')

from bokeh.plotting import figure, output_file, save
import pandas as pd

# 假设你的数据已经准备好了，放在名为votes_by_year的DataFrame中
# votes_by_year = data_movie.groupby('Released_Year')['No_of_Votes'].sum().reset_index()

# 创建一个Bokeh图形
p = figure(plot_width=1200, plot_height=650,title='历年投票趋势', x_axis_label='发行年份', y_axis_label='得票总数')
p.line(votes_by_year['Released_Year'], votes_by_year['No_of_Votes'], line_width=2)

# 将图形保存为HTML文件
output_file("templates/votes_by_year.html")
save(p)

# 你也可以将图形保存为静态图片，比如PNG格式
# export_png(p, filename="votes_trend.png")
plt.savefig('votes_trend.png')
plt.show()