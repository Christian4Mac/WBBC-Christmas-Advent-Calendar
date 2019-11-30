import datetime
from flask import Flask, request, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/instructions")
def instructions():
    return render_template('instructions.html')

@app.route("/go_to_day")
def go_to_day():
    day = int(request.args.get('day'))
    dt = datetime.datetime.today()
    if day <= dt.day or dt.month < 4:
        return redirect(f'http://www.westbradenton.org/family-advent/posts/december-{day}')
    else:
        return render_template('too_early.html')

# Run flask
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
