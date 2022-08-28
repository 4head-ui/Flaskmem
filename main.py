from flask import Flask,render_template,request
from data import *
app = Flask(__name__)

@app.route('/')
def entry_page():
    return render_template('base.html')



@app.route('/gamereturn',methods=['POST'])
def game():
    word = request.form['word']
    the_result = stonepaperknifes(word)
    return render_template('game.html',word=word,the_result=the_result)

@app.route('/game')
def gamereturn():
    return render_template('game_engine.html')

@app.route('/readme')
def readme():
    return render_template('readme.html')

if __name__ == '__main__':
    app.run(debug=False)