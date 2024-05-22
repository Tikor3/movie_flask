import csv
import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
from bokeh.plotting import figure, output_file, save
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Category10
import matplotlib.pyplot as plt

# 设置支持中文格式设置中文格式
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

# 读取数据
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

# 创建 DataFrame
df = pd.DataFrame(data, index=[i for i in range(len(data))], columns=columns)

# 统计各类别数量
c_list = list(set([i.strip() for i in ','.join([i for i in df['Genre']]).split(',')]))
n = [df['Genre'].str.contains(i, case=False).sum() for i in c_list]

# 使用 Plotly 创建饼图并保存为 HTML 文件
fig = go.Figure(data=[go.Pie(labels=c_list, values=n)])
fig.update_layout(title='排名前1000电影类型占比饼图')
pio.write_html(fig, 'templates/pie_chart_of_movie_genres.html')

# 使用 Bokeh 创建条形图并保存为 HTML 文件
source = ColumnDataSource(data=dict(x=c_list, y=n))
from bokeh.models import HoverTool

# 创建 Bokeh 图形
p = figure(x_range=c_list, plot_width=1300, plot_height=700, title='排名前1000电影类型占比条形图',
           toolbar_location=None, tools="")

# 添加条形图数据
bars = p.vbar(x='x', top='y', width=0.9, source=source, legend_field="x",
              line_color='white', fill_color=factor_cmap('x', palette=Category10[10], factors=c_list))

# 添加悬停工具
hover = HoverTool()
hover.tooltips = [("数量", "@y")]
p.add_tools(hover)

# 设置图形属性
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.yaxis.axis_label = "数量"
p.xaxis.major_label_orientation = 1.2

# 保存图形为 HTML 文件
output_file("templates/interactive_bar_chart_genre.html")
save(p)


# 绘制饼图
plt.pie(n, labels=c_list, autopct='%1.1f%%', pctdistance=0.9, labeldistance=1.25)
plt.title('排名前1000电影类型占比饼图')
plt.savefig('pie_chart_genre.png')
plt.show()

# 绘制条形图
plt.rcParams['figure.figsize'] = (10, 6)
plt.bar(c_list, n, width=0.8)
for i, v in enumerate(n):
    plt.text(i, v + 0.5, str(v), ha='center')
plt.title('排名前1000电影类型占比条形图')
plt.xlabel('类别')
plt.ylabel('值')
plt.xticks(rotation=30)
plt.savefig('bar_chart_genre.png')
plt.show()
