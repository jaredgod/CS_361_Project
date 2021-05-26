import json
import random
import requests
from base64 import b64decode

port = 51788

cname = []
cweight = []

with open('cname.txt', 'r') as f:
    cname = json.load(f)
with open('cweight.txt', 'r') as f:
    cweight = json.load(f)

sumweight = 0
for w in cweight:
    sumweight += w

def addcategory(names):
    global sumweight, cweight, cname
    for name in names:
        if name == '':
            pass
        elif name in cname:
            index = cname.index(name)
            cweight[index] += 1
            sumweight += 1
        else:
            cname.append(name)
            cweight.append(1)
            sumweight += 1
    with open('cname.txt', 'w') as f:
        f.truncate()
        f.seek(0)
        json.dump(cname, f)
    
    with open('cweight.txt', 'w') as f:
        f.truncate()
        f.seek(0)
        json.dump(cweight, f)

def getrandcategory():
    count = random.randint(0, sumweight - 1)
    index = 0
    count -= cweight[index]
    while(count >= 0):
        count -= cweight[index]
        index += 1
    return cname[index]

def randFromList(list):
    ind = random.randint(0, len(list) - 1)
    return list[ind]

def getrandarticle():
    category = getrandcategory()
    nextLink = f'https://en.wikipedia.org/wiki/Special:RandomInCategory/{category}'
    link = ''
    done = False
    title, cat, sum, cont = '', '', '', ''
    while not done:
        error, title, cat, sum, cont = getArticle(nextLink)
        if error:
            return True, '', '', '', '', ''
        link = nextLink
        nextLink = f'https://en.wikipedia.org/wiki/Special:RandomInCategory/{randFromList(cat)}'
        test = title.split(':')
        done = test[0] != 'Category'
    
    temp = title.replace(' ', '_')
    link = f'https://en.wikipedia.org/wiki/{temp}'
    return error, link, title, cat, sum, cont

def getArticle(link): 
    try:
        categoryRes = requests.get(f'http://127.0.0.1:{port}/get/{link}')
        if categoryRes.status_code != 200:
            return True, '', '', '', ''
    except:
        return True, '', '', '', ''
    cat = categoryRes.text
    cat = cat.replace('/wiki/Category:', '')
    cat = cat.split('\n')
    cat.remove('')

    try:
        contentRes = requests.post("https://wikiscraperproject.herokuapp.com/", data = {"url": link})
        if contentRes.status_code != 200:
            return True, '', '', '', ''
    except:
        return True, '', '', '', ''

    content = contentRes.text.split('\n\"')
    title=content[0].replace('\n', ' ')
    sum = content[1]

    cont = ''
    for c in content[1:]:
        cont += c
        cont += '\n'

    return False, title, cat, sum, cont
