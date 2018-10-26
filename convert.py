import pyperclip
import re
def getStr(s):
    str1 = ''
    flag = False
    for c in s:
        if c.isupper():
            flag = True
        if flag and c.isupper():
            str1 += ('_'+c)
        if flag and c.islower():
            str1 += c
    return str1[1:]

content=pyperclip.paste()
out = ""

pattern=re.compile(r'\(.*\)')
pattern1 = re.compile(r'[a-zA-Z_\.]+') 
for line in content.split('\n'):
    if len(line) < 10:
        continue
    listA = pattern.search(line).group(0)[1:-1].split(',')
    out += (listA[0].strip()  + '.' + getStr(listA[1])+ ' := ')
    if str(listA[-1]).find('.') != -1:
        listB = listA[-1].split('.')
        out += (listB[0].strip()[2:] + '.' +getStr(listB[-1]))
    else:
        out += listA[-1].strip()
    out += ';\n';

pyperclip.copy(out)


        

    


        
