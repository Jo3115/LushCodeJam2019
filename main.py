from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)


@app.route('/')
def home_page():
    """Displays The Homepage"""
    return render_template('home.html',
                           weather_icon=weather.get_weather(),
                           news=news.short_list_news())
