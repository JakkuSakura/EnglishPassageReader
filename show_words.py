#!/bin/python3
# coding: utf-8
import requests as rq
import sys
import re


from ReadMdx.mdict_query import IndexBuilder
builder = IndexBuilder('mdx/bing.mdx')

def get_exp(word):
    result_text = builder.mdx_lookup(word)
    return result_text


def split_words(passage):
    l = re.split(r'[^a-zA-Z]', passage)
    n = set()
    for e in l:
        if e:
            n.add(e.lower())
    new_l = list(n)
    new_l.sort()
    return new_l


def split_sentences(passage):
    l = re.split(r'\. |? ', passage)
    return l


def get_wordlist(sen, ignored):
    print(ignored)
    words = split_words(sen)
    pairs = []
    for e in words:
        if e in ignored:
            # print('ignored', e)
            continue
        exp = get_exp(e)
        if not exp:
            continue
        pairs.append((e, exp[0]))
    return pairs
