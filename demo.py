# Author :刘健强
# @Time  :2024/5/16 8:50
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("imdb_top_1000.csv")
print(data.head(10))
# Check Last 10 Rows
data.tail(10)
data.shape
# Get Information about data¶
data.info()
# Convert Runtime column to Float
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
d = data_movie[data_movie['Runtime']>=180]['Series_Title']
print(d)

votes_by_year = data_movie.groupby('Released_Year')['No_of_Votes'].sum().reset_index()
# 历年投票趋势
# plt.figure(figsize=(12, 6))
# sns.lineplot(data=votes_by_year, x='Released_Year', y='No_of_Votes')
# plt.title('Tendance des Votes au fil des Années')
# plt.xlabel('Année de Sortie')
# plt.ylabel('Somme des Votes')
# plt.show()

# plt.figure(figsize=(12, 6))
# sns.lineplot(data=data_movie, x='Released_Year', y='No_of_Votes')
# plt.title('Tendance des Votes au fil des Années')
# plt.xlabel('Année de Sortie')
# plt.ylabel('Nombre de Votes')
#
# 在哪一年，十字架的平均数最高
# mean_gross_by_year = data_movie.groupby('Released_Year')['Gross'].mean().sort_values(ascending=False)
# plt.figure(figsize=(12, 6))
# sns.barplot(x=mean_gross_by_year.index, y=mean_gross_by_year.values)
# plt.title("Gross per year")
# plt.xlabel("Released Year")
# plt.ylabel("Mean Gross")
# plt.xticks(rotation=90)  # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité

# 显示前 10 名长篇电影标题和运行时间
# Top_10 = data_movie.nlargest(10,'Runtime')[['Series_Title','Runtime']].set_index('Series_Title')
# sns.barplot(x='Runtime', y=Top_10.index, data= Top_10)
# #
#
# # 电影最多的前 20 个上映年份
# nb_film_released = data_movie['Released_Year'].value_counts().nlargest(20) # or head(10)
# df_nb_film_released = pd.DataFrame({'Released_Year': nb_film_released.index, 'Count': nb_film_released.values})
# plt.figure(figsize=(12, 6))
# sns.barplot(x='Released_Year', y='Count', data=df_nb_film_released)
# plt.title('Top 20 Released Years with the Most Films')
# plt.xlabel('Released Year')
# plt.ylabel('Number of Films')
# plt.xticks(rotation=90)  # Rotation des étiquettes de l'axe des x pour une meilleure lisibilité
# plt.show()

# 显示得分最高的 20 部电影及其导演
Top_10_rate = data_movie.nlargest(20,'Meta_score')[['Series_Title','Meta_score','Director']].set_index('Series_Title')
plt.figure(figsize=(14, 8))
sns.barplot(x='Meta_score', y= Top_10_rate.index, hue='Director', data=Top_10_rate, dodge=False)
plt.title('Top 20 Movies with the Highest Meta_Score and their Directors')
plt.xlabel('Meta_Score')
plt.ylabel('Movie Title')
plt.legend(title='Director', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# # 显示前 20 名总票房最高的电影标题
# Top_20_grosss = data_movie.nlargest(20,'Gross')[['Series_Title','Gross']].set_index('Series_Title')
# sns.barplot(x='Gross', y= Top_20_grosss.index, data=Top_20_grosss)
# plt.title('Top 20 Movies with the Highest Gross')
# plt.xlabel('Gross')
# plt.ylabel('Movie Title')
#
# # 评级会影响总值吗 ==> 是的
# sns.scatterplot(x="Meta_score", y='Gross', data=data_movie)
plt.show()

