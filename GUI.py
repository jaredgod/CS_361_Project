import tkinter as tk
from tkinter import *
import chooser

class mainPage:
    def __init__(self, root):

        #background
        self.root = root
        self.frame = tk.Frame(window, width=800, height=450, background='white')
        self.frame.pack()
        
        #title
        self.title = tk.Label(self.frame, font=('Raleway', 24), text='Loading Title...',background='white', anchor=SW, wraplength=770, justify=LEFT)
        self.title.place( x=10, y=10, height=80, relwidth=.75)
        self.underline = tk.Canvas(self.frame, height=5, background='black')
        self.underline.place( x=10, y=90, height=5, relwidth=.75)
        
        #content
        self.category = tk.Label(self.frame, font=('Raleway', 14), text='Loading Categories...', background='white', anchor=NW, wraplength=770, justify=LEFT)
        self.category.place(x=10, y=95, height=25, relwidth=1.0, width=-20)
        self.content = tk.Label(self.frame, font=('Raleway', 14), text='Loading Content...', background='white', anchor=NW, wraplength=770, justify=LEFT)
        self.content.place(x=10, y=120, relheight=.9, height=-145, relwidth=1.0, width=-20)
        
        #next
        self.nextButton = tk.Button(self.frame, font=('Raleway', 14), text='Next',
            border=0, background='lightblue')
        self.nextButton.place(relx=.8, x=-10, rely=.9, y=-10, relwidth=.2, relheight=.1)
        
        #learn more
        self.learnButton = tk.Button(self.frame, font=('Raleway', 14), text='Learn More',
            border=0, background='lightblue')
        self.learnButton.place(relx=.2, x=20, rely=.9, y=-10, relwidth=.6, width=-40, relheight=.1)
        
        #previous
        self.prevButton = tk.Button(self.frame, font=('Raleway', 14), text='Previous',
            border=0, background='lightblue')
        self.prevButton.place(relx=0.0, x=10, rely=.9, y=-10, relwidth=.2, relheight=.1)
        
        #help
        self.helpButton = tk.Button(self.frame, font=('Raleway', 14), text='Help',
            border=0, background='lightblue')
        self.helpButton.place(relx=0.75, x=20, y=10, relwidth=.25, width=-30, relheight=.1)

        #history
        self.historyButton = tk.Button(self.frame, font=('Raleway', 14), text='History',
            border=0, background='lightblue')
        self.historyButton.place(relx=0.75, x=20, rely=.1, y=20, relwidth=.25, width=-30, relheight=.1)


    def setTitle(self, text):
        self.title.config(text=text)
    
    def setCategory(self, text):
        self.category.config(text=text)
        
    def setContent(self, text):
        self.content.config(text=text)
    
    def setButton(self, next, prev, showlearn, showhelp):
        self.nextButton.config(command=next)
        self.learnButton.config(command=showlearn)
        self.prevButton.config(command=prev)
        self.helpButton.config(command=showhelp)

    def hide(self):
        self.frame.pack_forget()
            
    def show(self):
        self.frame.pack()
        

class learnPage:
    def __init__(self, root):
        #background
        self.root = root
        self.frame = tk.Frame(window, width=800, height=450, background='white')
        self.frame.pack()
        
        #title
        self.title = tk.Label(self.frame, font=('Raleway', 24), text='Loading Title...',background='white', anchor=SW, wraplength=770, justify=LEFT)
        self.title.place( x=10, y=10, height=80, relwidth=.75)
        self.underline = tk.Canvas(self.frame, height=5, background='black')
        self.underline.place( x=10, y=90, height=5, relwidth=.75)
        
        #content
        self.category = tk.Label(self.frame, font=('Raleway', 14), text='Loading Categories...', background='white', anchor=NW, wraplength=770, justify=LEFT)
        self.category.place(x=10, y=95, height=25, relwidth=1.0, width=-20)
        self.content = tk.Label(self.frame, font=('Raleway', 14), text='Loading Content...', background='white', anchor=NW, wraplength=770, justify=LEFT)
        self.content.place(x=10, y=120, relheight=.9, height=-145, relwidth=1.0, width=-20)

        #back
        self.backButton = tk.Button(self.frame, font=('Raleway', 14), text='Back',
            border=0, background='lightblue')
        self.backButton.place(relx=0.75, x=20, y=10, relwidth=.25, width=-30, relheight=.1)

    def setTitle(self, text):
        self.title.config(text=text)
        
    def setContent(self, text):
        self.content.config(text=text)
    
    def setCategory(self, text):
        self.category.config(text=text)

    def setButton(self, showmain):
        self.backButton.config(command=showmain)

    def hide(self):
        self.frame.pack_forget()
            
    def show(self):
        self.frame.pack()

class historyPage:
    def __init__(self, root):
        #background
        self.root = root
        self.frame = tk.Frame(window, width=800, height=450, background='white')
        self.frame.pack()
        
        #title
        self.title = tk.Label(self.frame, font=('Raleway', 24), text='History',background='white', anchor=SW, wraplength=770, justify=LEFT)
        self.title.place( x=10, y=10, height=80, relwidth=.75)
        self.underline = tk.Canvas(self.frame, height=5, background='black')
        self.underline.place( x=10, y=90, height=5, relwidth=.75)
        
        #content
        self.category = tk.Label(self.frame, font=('Raleway', 14), text='Loading Categories...', background='white', anchor=NW, wraplength=770, justify=LEFT)
        self.category.place(x=10, y=95, height=25, relwidth=1.0, width=-20)
        self.content = tk.Label(self.frame, font=('Raleway', 14), text='Loading Content...', background='white', anchor=NW, wraplength=770, justify=LEFT)
        self.content.place(x=10, y=120, relheight=.9, height=-145, relwidth=1.0, width=-20)

        #back
        self.backButton = tk.Button(self.frame, font=('Raleway', 14), text='Back',
            border=0, background='lightblue')
        self.backButton.place(relx=0.75, x=20, y=10, relwidth=.25, width=-30, relheight=.1)

    def setTitle(self, text):
        self.title.config(text=text)
        
    def setContent(self, text):
        self.content.config(text=text)
    
    def setCategory(self, text):
        self.category.config(text=text)

    def setButton(self, showmain):
        self.backButton.config(command=showmain)

    def hide(self):
        self.frame.pack_forget()
            
    def show(self):
        self.frame.pack()
    

class helpPage:
    def __init__(self, root):

        #background
        self.root = root
        self.frame = tk.Frame(window, width=800, height=450, background='white')
        self.frame.pack()
        
        #title
        self.title = tk.Label(self.frame, font=('Raleway', 24), text='Loading Title...',background='white', anchor=SW, wraplength=770, justify=LEFT)
        self.title.place( x=10, y=10, height=80, relwidth=.75)
        self.underline = tk.Canvas(self.frame, height=5, background='black')
        self.underline.place( x=10, y=90, height=5, relwidth=.75)
        
        #content
        self.category = tk.Label(self.frame, font=('Raleway', 14), text='Loading Categories...', background='white', anchor=NW, wraplength=770, justify=LEFT)
        self.category.place(x=10, y=95, height=25, relwidth=1.0, width=-20)
        self.content = tk.Label(self.frame, font=('Raleway', 14), text='Loading Content...', background='white', anchor=NW, wraplength=770, justify=LEFT)
        self.content.place(x=10, y=120, relheight=.9, height=-145, relwidth=1.0, width=-20)
        
        #next
        self.nextButton = tk.Button(self.frame, font=('Raleway', 14), text='Next',
            border=0, background='lightblue')
        self.nextButton.place(relx=.8, x=-10, rely=.9, y=-10, relwidth=.2, relheight=.1)
        
        #learn more
        self.learnButton = tk.Button(self.frame, font=('Raleway', 14), text='Learn More',
            border=0, background='lightblue')
        self.learnButton.place(relx=.2, x=20, rely=.9, y=-10, relwidth=.6, width=-40, relheight=.1)
        
        #previous
        self.prevButton = tk.Button(self.frame, font=('Raleway', 14), text='Previous',
            border=0, background='lightblue')
        self.prevButton.place(relx=0.0, x=10, rely=.9, y=-10, relwidth=.2, relheight=.1)
        
        #back
        self.backButton = tk.Button(self.frame, font=('Raleway', 14), text='Back',
            border=0, background='lightblue')
        self.backButton.place(relx=0.75, x=20, y=10, relwidth=.25, width=-30, relheight=.1)

    def setTitle(self, text):
        self.title.config(text=text)
        
    def setContent(self, text):
        self.content.config(text=text)
    
    def setCategory(self, text):
        self.category.config(text=text)

    def setButton(self, showmain):
        self.backButton.config(command=showmain)

    def hide(self):
        self.frame.pack_forget()
            
    def show(self):
        self.frame.pack()


window = Tk()
window.config(background='white')
window.geometry('800x450')
window.resizable(False, False)

main = mainPage(window)
learn = learnPage(window)
learn.hide()
help = helpPage(window)
help.hide()

tempIndex = -1
tempHistory = [] 

def showMain():
    main.show()
    learn.hide()
    help.hide()

def showLearn():
    main.hide()
    learn.show()
    help.hide()

def showHelp():
    main.hide()
    learn.hide()
    help.show()

def getNewArticle():
    update('Loading Content...', '', '', '')
    link, title, cat, sum, cont = chooser.getrandarticle()
    addLink(link)
    concatCategory=''
    for c in cat:
        concatCategory += c + ' - '
    #update(title, concatCategory, sum, cont)

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
        title, cat, sum, cont = chooser.getArticle(tempHistory[tempIndex])
        concatCategory=''
        for c in cat:
            concatCategory += c + ' - '
        update(title, concatCategory, sum, cont)

def prev():
    global tempIndex
    global tempHistory
    if tempIndex > 0:
        tempIndex -= 1
        title, cat, sum, cont = chooser.getArticle(tempHistory[tempIndex])
        concatCategory=''
        for c in cat:
            concatCategory += c + ' - '
        update(title, concatCategory, sum, cont)

main.setButton(next, prev, showLearn, showHelp)
learn.setButton(showMain)
help.setButton(showMain)

next()


window.mainloop()

