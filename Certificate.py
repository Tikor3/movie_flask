# Author :刘健强
# @Time  :2024/5/16 8:49
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
# certificate_list = list(set([i for i in df['Certificate']]))
# n = [df['Certificate'].str.contains(i, case=False).sum() for i in certificate_list]
certificate_list = list(set([i for i in df['Certificate']]))
certificate_list.remove('')
print(len(certificate_list))
print(certificate_list)
n = []
for i in certificate_list:
    count = df['Certificate'].str.contains(i, case=False).sum()
    n.append(count)
    print(count)  # 输出符合条件的行数

print(len(n))

# 使用 Plotly 创建饼图并保存为 HTML 文件
fig = go.Figure(data=[go.Pie(labels=certificate_list, values=n)])
fig.update_layout(title='排名前1000电影获得证书类型占比饼图')
pio.write_html(fig, 'templates/movie_certificate_pie.html')

# 使用 Bokeh 创建条形图并保存为 HTML 文件
source = ColumnDataSource(data=dict(x=certificate_list, y=n))
from bokeh.models import HoverTool

# 创建 Bokeh 图形
p = figure(x_range=certificate_list, plot_width=1200, plot_height=650,title='排名前1000电影获得证书类型占比条形图',
           toolbar_location=None, tools="")

# 添加条形图数据
bars = p.vbar(x='x', top='y', width=0.9, source=source, legend_field="x",
              line_color='white', fill_color=factor_cmap('x', palette=Category10[10], factors=certificate_list))

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
output_file("templates/movie_certificate_bar.html")
save(p)


# 绘制饼图
plt.pie(n, labels=certificate_list, autopct='%1.1f%%', pctdistance=0.9, labeldistance=1.25)
plt.title('排名前1000电影获得证书类型占比饼图')
plt.savefig('pie_movie_certificate.png')
plt.show()

# 绘制条形图
plt.rcParams['figure.figsize'] = (12, 8)
plt.bar(certificate_list, n, width=0.8)
for i, v in enumerate(n):
    plt.text(i, v + 0.5, str(v), ha='center')
plt.title('排名前1000电影获得证书类型占比条形图')
plt.xlabel('类别')
plt.ylabel('数量')
plt.xticks(rotation=30)
plt.savefig('bar_movie_certificate.png')
plt.show()
