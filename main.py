from flask import Flask, render_template, url_for, request, redirect
import json_handler

app = Flask(__name__)


@app.route('/')
def home_page():
    """Displays The Homepage"""
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)