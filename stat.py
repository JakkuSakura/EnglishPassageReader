#!/bin/python3

import re
def add(s, e):
    if e in s:
        s[e] += 1
    else:
        s[e] = 1
import show_words
if __name__ == "__main__":
    
    m = {}
    match = re.compile(r'[a-zA-Z]+')
    with open('passage.txt','r') as f:
        ls = match.findall(f.read())
    for e in ls:
        add(m, e.lower())
    l = sorted(m.items(), key=lambda x: x[1], reverse=True)
    mt = re.compile(r'<div class="hwd">.+?</div>')
    cnt_word = 0
    f = None
    for k, n in l:
        if f is None or cnt_word % 100 == 0:
            f = open('static/wordlist%02d.html' % (cnt_word // 100), 'w')
        # f.write('%s %d\n' % (k, n))
        lookup = show_words.get_exp(k)
        if lookup:
            al = mt.findall(lookup[0])
            lookup = lookup[0].replace(al[0], (al[0] + r'<div class="frq">出现次数:%d</div>') % (n))
            f.write(lookup)
        cnt_word += 1
    