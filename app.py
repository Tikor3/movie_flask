from flask import Flask, redirect, render_template, request, flash, url_for
import sqlite3
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ljq'


# 博客首页，查看博客列表
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pie_chart_of_movie_genres')
def pie_chart_of_movie_genres():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('pie_chart_of_movie_genres.html')


@app.route('/interactive_bar_chart_genre')
def interactive_bar_chart_genre():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('interactive_bar_chart_genre.html')

@app.route('/movie_score_line_chart')
def movie_score_line_chart():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('movie_score_line_chart.html')

@app.route('/movie_certificate_bar')
def movie_certificate_bar():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('movie_certificate_bar.html')\

@app.route('/movie_certificate_pie')
def movie_certificate_pie():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('movie_certificate_pie.html')

@app.route('/top_20_released_years')
def top_20_released_years():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('top_20_released_years.html')

@app.route('/top_20_movies')
def top_20_movies():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('top_20_movies.html')

@app.route('/top_10_runtime')
def top_10_runtime():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('top_10_runtime.html')

@app.route('/votes_by_year')
def votes_by_year():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('votes_by_year.html')

@app.route('/mean_gross_by_year')
def mean_gross_by_year():
    # 这里可以添加相关的逻辑，比如从数据库或文件中获取数据
    # 在渲染模板时传递数据到模板中
    return render_template('mean_gross_by_year.html')


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8090)
    app.run()
