from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)


@app.route('/')
def home_page():
    list = []
    file = open('product.csv', 'r')
    for i in file:
        row = []
        entry = i.split(',')
        if entry == ['', '\n']:
            pass
        else:
            row.append(entry[0])
            row.append(entry[1])
            list.append(row)
    return render_template('home.html', images=list)


@app.route('/animation')
def animation():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)