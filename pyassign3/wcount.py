#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Wang Yizhou"
__pkuid__  = "1700011804"
__email__  = "1700011804@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    r={}
    l=''
    lines=lines.lower()
    for i in lines:
        if i.isalpha() or i==' ' or i=="'" or i=='-':
            l+=i
        else:
            l+=' '
    l=l.split()
    print(l)
    for i in l:
        r[i]=r.get(i,0)+1
    c=list(r.items())
    v=list(r.values())
    v.sort(reverse=True)
    v=v[:topn]
    for i in v:
        for (j,k) in c:
            if k==i:
                print(j,' '*(12-len(j)),k)
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
