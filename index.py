from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')

@app.route('/download_v3')

def download_v3():
    return render_template('downloadv3.html')

@app.route('/download_vpro')

def download_vpro():
    return render_template('downloadvpro.html')


@app.route('/info_v3')

def info_v3():
    return render_template('info_v3.html')


@app.route('/info_vpro')

def info_vpro():
    return render_template('info_vpro.html')



@app.route('/data')

def data():
    return render_template('data.html')


if __name__ == '__main__':
    app.run()