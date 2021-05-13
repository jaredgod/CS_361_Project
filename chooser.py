import json
import random

nf = open('cname.txt', 'r')
wf = open('cweight.txt', 'r')

cname = json.load(nf)
cweight = json.load(wf)
sumweight = 0
for w in cweight:
    sumweight += w

def addcategory(name):
    if name in cname:
        index = cname.find(name)
        cweight[index] += 1
        sumweight += 1
    else:
        cname.append(name)
        cweight.append(1)

def getrandcategory():
    count = random.randint(0, sumweight - 1)
    index = 0
    count -= cweight[index]
    while(count >= 0):
        count -= cweight[index]
        index += 1
    return cname[index]


def save():
    with open('cname.txt', 'w') as filehandle:
        json.dump(cname, filehandle)
    with open('cweight.txt', 'w') as filehandle:
        json.dump(cweight, filehandle)

def getrandarticle():
    link = random.randint(0, 100)
    return link, 'Hello World' + str(link), ['category 1', 'category 2', 'category 3', 'category 4'], 'A "Hello, World!" program', 'A "Hello, World!" program generally is a computer program that outputs or displays the message "Hello, World!".'

def getArticle(number): #TODO: replace this with url
    return 'Hello World' + str(number), ['category 1', 'category 2', 'category 3', 'category 4'], 'A "Hello, World!" program', 'A "Hello, World!" program generally is a computer program that outputs or displays the message "Hello, World!".'
