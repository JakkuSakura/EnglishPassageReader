#!/bin/python3
from show_words import *
from flask import *
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)


ignored_words = []
with open("ignored_words.txt", 'r') as f:
    for e in f:
        ignored_words.append(e.strip())
print('ignored', len(ignored_words), 'words')

@app.route('/')
def main_page():
    return render_template("passage.html")

@app.route('/concise-bing.css')
def get_css():
    return redirect(url_for('static', filename='concise-bing.css'))

@app.route('/word', methods=['GET'])
def lookup_dict():
    word = request.args.get('q')
    exp = get_exp(word)
    if exp:
        return exp[0]
    else:
        return "<h2 style='color: red;'>找不到单词:</h2>" + word

@app.route('/word-example-sentence', methods=['GET'])
def example_sentence():
    word = request.args.get('q')
    try:
        url = 'https://cn.bing.com/dict/search'
        r = requests.get(url, params={'q': word} )
        soup = BeautifulSoup(r.text, 'lxml')
        res = soup.find_all(class_='se_li')[:10]
        r = ''
        for e in res:
            r += str(e)
        return "<h3>例句</h3>" + r
    except Exception as e:
        print(e, file=sys.stderr)
        return ""
    
    
@app.route('/wordlist', methods=['POST'])
def wordlist():
    # print(request.form)
    psg = request.form['passage']
    li = get_wordlist(psg, ignored_words)
    ss = []
    for e in li:
        ss.append(e[1])
    return '<div>共有{}生词</div>'.format(len(ss))+''.join(ss)


@app.route('/ignore', methods=['POST'])
def ignore_word():
    word = request.form['w']
    ignored_words.append(word)
    with open("ignored_words.txt", "a") as f:
        f.write(word)
        f.write('\n')
    return ""


@app.route('/translate', methods=['POST'])
def translate():
    import baidu
    psg = request.form['passage']
    ts = baidu.Baidu('en', 'zh').translate(psg)
    return ts

if __name__ == '__main__':
    app.run(debug=True)
