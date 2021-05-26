import GUI
import chooser
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.config(background='white')
window.geometry('1600x900')
window.resizable(False, False)

main = GUI.mainPage(window)
main.hide()
learn = GUI.learnPage(window)
learn.hide()
help = GUI.helpPage(window)
history = GUI.historyPage(window)
history.hide()

link = ''
title = ''
cat = []
sum = ''
cont = ''

tempIndex = -1
tempHistory = [] 

historyFile = 'history.csv'
hist=''


#motion
def hideall():
    main.hide()
    learn.hide()
    help.hide()
    history.hide()

def showMain():
    hideall()
    main.show()

def showLearn():
    saveArticle()
    hideall()
    learn.show()

def showHelp():
    hideall()
    help.show()

def showHelp():
    hideall()
    help.show()

def showHistory():
    hideall()
    history.show()


#scraper
def getNewArticle():
    global link, title, cat, sum, cont
    update('Loading Content...', '', '', '')
    error, link, title, cat, sum, cont = chooser.getrandarticle()
    if error:
        update('Error', "The application couldn't connect to wikipedia.", "Please make sure that you are connected to the internet and try restarting the program.", "Please make sure that you are connected to the internet and try restarting the program.")
        return
    addLink(link)
    concatCategory=''
    for c in cat:
        concatCategory += c + ' - '
    update(title, concatCategory, sum, cont)

def getArticle(l):
    global link, title, cat, sum, cont
    update('Loading Content...', '', '', '')
    error, title, cat, sum, cont = chooser.getArticle(l)
    if error:
        update('Error', "The application couldn't connect to wikipedia.", "Please make sure that you are connected to the internet and try restarting the program.", "Please make sure that you are connected to the internet and try restarting the program.")
        return
    addLink(l)
    concatCategory=''
    for c in cat:
        concatCategory += c + ' - '
    update(title, concatCategory, sum, cont)

def addLink(link):
    global tempIndex
    if len(tempHistory) > 19:
        tempHistory.pop(0)
    tempHistory.append(link)
    tempIndex=len(tempHistory)-1

def update(title, cat, sum, cont):
    main.setTitle(title)
    learn.setTitle(title)
    help.setTitle(title)

    main.setCategory(cat)
    learn.setCategory(cat)
    help.setCategory(cat)

    main.setContent(sum)
    learn.setContent(cont)
    help.setContent(sum)

def next():
    global tempIndex
    global tempHistory
    if tempIndex == len(tempHistory) - 1:
        getNewArticle()
    else:
        tempIndex += 1
        error, title, cat, sum, cont = chooser.getArticle(tempHistory[tempIndex])
        if error:
            update('Error', "The application couldn't connect to wikipedia.", "Please make sure that you are connected to the internet and try restarting the program.", "Please make sure that you are connected to the internet and try restarting the program.")
            return
        concatCategory=''
        for c in cat:
            concatCategory += c + ' - '
        update(title, concatCategory, sum, cont)

def prev():
    global tempIndex
    global tempHistory
    if tempIndex > 0:
        tempIndex -= 1
        error, title, cat, sum, cont = chooser.getArticle(tempHistory[tempIndex])
        if error:
            update('Error', "The application couldn't connect to wikipedia.", "Please make sure that you are connected to the internet and try restarting the program.", "Please make sure that you are connected to the internet and try restarting the program.")
            return
        concatCategory=''
        for c in cat:
            concatCategory += c + ' - '
        update(title, concatCategory, sum, cont)


#history
def deleteHistory(index):
    
    history.deleteHistory(index)
    with open(historyFile, 'r+') as f:
        temp=f.readlines()
        temp.pop(index)
        f.seek(0)
        f.truncate()
        for h in temp:
            f.write(h)

def loadHistory(link):
    getArticle(link)
    showMain()

def saveArticle():
    global title, link, cat, hist
    history.addHistory(title, link, loadHistory, deleteHistory)
    with open(historyFile, 'a') as f:
        f.write(f'{title},{link}\n')
    chooser.addcategory(cat)

def savedArticle(info):
    history.addHistory(info[0], info[1], loadHistory, deleteHistory)


main.setButton(next, prev, showLearn, showHelp, showHistory)
learn.setButton(showMain)
help.setButton(showMain)
history.setButton(showMain)

next()

with open(historyFile, 'r') as f:
    hist=f.readlines()
    if hist != ['']:
        for h in hist:
            temp = h.split(',')
            savedArticle(temp)


window.mainloop()