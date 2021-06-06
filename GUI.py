import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk



class mainPage:
    def __init__(self, root):

        def background():
            self.root = root
            self.frame = tk.Frame(root, width=1600, height=900, background='white')
            self.frame.pack()
        
        def title():
            self.title = tk.Label(self.frame, font=('Raleway', 24), text='Loading Title...',
                                background='white', anchor=SW, wraplength=1100, justify=LEFT)
            self.title.place( x=10, y=10, height=80, relwidth=.75)
            self.underline = tk.Canvas(self.frame, height=5, background='black')
            self.underline.place( x=10, y=90, height=5, relwidth=.75)
        
        def image():
            self.image = tk.Label(self.frame)
            self.image.place(relx=0.75, x=20, rely=.2, y=30, relwidth=.25, width=-30, height=370)

        def content():
            self.category = tk.Label(self.frame, font=('Raleway', 14), text='Loading Categories...', 
                                background='white', anchor=NW, wraplength=1100, justify=LEFT)
            self.category.place(x=10, y=95, height=25, relwidth=.75)
            self.content = tk.Label(self.frame, font=('Raleway', 14), text='Loading Content...', 
                                background='white', anchor=NW, wraplength=1100, justify=LEFT)
            self.content.place(x=10, y=120, relheight=.9, height=-145, relwidth=.75)
        
        def next():
            self.nextButton = tk.Button(self.frame, font=('Raleway', 14), text='Next',
                border=0, background='lightblue')
            self.nextButton.place(relx=.8, x=-10, rely=.9, y=-10, relwidth=.2, relheight=.1)
        
        def learnMore():
            self.learnButton = tk.Button(self.frame, font=('Raleway', 14), text='Learn More',
                border=0, background='lightblue')
            self.learnButton.place(relx=.2, x=20, rely=.9, y=-10, relwidth=.6, width=-40, relheight=.1)
        
        def previous():
            self.prevButton = tk.Button(self.frame, font=('Raleway', 14), text='Previous',
                border=0, background='lightblue')
            self.prevButton.place(relx=0.0, x=10, rely=.9, y=-10, relwidth=.2, relheight=.1)
        
        def help():
            self.helpButton = tk.Button(self.frame, font=('Raleway', 14), text='Help',
                border=0, background='lightblue')
            self.helpButton.place(relx=0.75, x=20, y=10, relwidth=.25, width=-30, relheight=.1)

        def history():
            self.historyButton = tk.Button(self.frame, font=('Raleway', 14), text='History',
                border=0, background='lightblue')
            self.historyButton.place(relx=0.75, x=20, rely=.1, y=20, relwidth=.25, width=-30, relheight=.1)
        
        background()
        title()
        image()
        content()
        next()
        learnMore()
        previous()
        help()
        history()


    

    def setTitle(self, text):
        self.title.config(text=text)
    
    def setCategory(self, text):
        self.category.config(text=text)
        
    def setContent(self, text):
        self.content.config(text=text)
    
    def setButton(self, next, prev, showlearn, showhelp, showHistory):
        self.nextButton.config(command=next)
        self.learnButton.config(command=showlearn)
        self.prevButton.config(command=prev)
        self.helpButton.config(command=showhelp)
        self.historyButton.config(command=showHistory)

    def setImage(self, src):
        self.img = Image.open(f'{src}')
        self.img = self.img.resize((370, 370), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.image.configure(image=self.img)

    def hide(self):
        self.frame.pack_forget()
            
    def show(self):
        self.frame.pack()


class learnPage:
    def __init__(self, root):
        #background
        self.root = root
        self.frame = tk.Frame(root, width=1600, height=900, background='white')
        self.frame.pack()
        
        #title
        self.title = tk.Label(self.frame, font=('Raleway', 24), text='Loading Title...',background='white', anchor=SW, wraplength=1100, justify=LEFT)
        self.title.place( x=10, y=10, height=80, relwidth=.75)
        self.underline = tk.Canvas(self.frame, height=5, background='black')
        self.underline.place( x=10, y=90, height=5, relwidth=.75)
        
        #content
        self.category = tk.Label(self.frame, font=('Raleway', 14), text='Loading Categories...', background='white', anchor=NW, wraplength=1100, justify=LEFT)
        self.category.place(x=10, y=95, height=25, relwidth=1.0, width=-20)
        self.content = tk.Text(self.frame, font=('Raleway', 14), background='white', wrap=WORD)
        self.sb = tk.Scrollbar(orient="vertical", command=self.content.yview)
        self.content.configure(yscrollcommand=self.sb.set)
        self.sb.pack(side="right", fill="y")
        self.content.place(x=10, y=120, relheight=.9, height=-145, relwidth=1.0, width=-20)
        self.content.configure(state="disabled")

        #back
        self.backButton = tk.Button(self.frame, font=('Raleway', 14), text='Back',
            border=0, background='lightblue')
        self.backButton.place(relx=0.75, x=20, y=10, relwidth=.25, width=-30, relheight=.1)

    def setTitle(self, text):
        self.title.config(text=text)
        
    def setContent(self, text):
        self.content.configure(state="normal")
        self.content.delete(1.0, END)
        self.content.insert(1.0, text)
        self.content.configure(state="disabled")
    
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
        self.frame = tk.Frame(root, width=1600, height=900, background='white')
        self.frame.pack()
        
        #title
        self.title = tk.Label(self.frame, font=('Raleway', 24), text='Loading Title...',background='white', anchor=SW, wraplength=1100, justify=LEFT)
        self.title.place( x=10, y=10, height=80, relwidth=.75)
        self.underline = tk.Canvas(self.frame, height=5, background='black')
        self.underline.place( x=10, y=90, height=5, relwidth=.75)
        
        #content
        self.category = tk.Label(self.frame, font=('Raleway', 14), text='Loading Categories...', background='white', anchor=NW, wraplength=1100, justify=LEFT)
        self.category.place(x=10, y=95, height=25, relwidth=1.0, width=-20)
        self.content = tk.Label(self.frame, font=('Raleway', 14), text='Loading Content...', background='white', anchor=NW, wraplength=1100, justify=LEFT)
        self.content.place(x=10, y=120, relheight=.9, height=-145, relwidth=1.0, width=-20)
        
        #next
        self.nextButton = tk.Button(self.frame, font=('Raleway', 14), text='Next',
            border=0, background='lightblue')
        self.nextButton.place(relx=.8, x=-10, rely=.9, y=-10, relwidth=.2, relheight=.1)
        self.nextHelp = tk.Label(self.frame, font=('Raleway', 11), background='lightgrey', anchor=NW, wraplength=460, justify=LEFT)
        self.nextHelp.configure(text='Click here to learn about something else! You can always revisit previously viewed articles.')
        self.nextHelp.place(relx=.7, x=-10, rely=.75, y=-20, relheight=.15, height=0, relwidth=.3, width=0)
        
        #learn more
        self.learnButton = tk.Button(self.frame, font=('Raleway', 14), text='Learn More',
            border=0, background='lightblue')
        self.learnButton.place(relx=.2, x=20, rely=.9, y=-10, relwidth=.6, width=-40, relheight=.1)
        self.learnHelp = tk.Label(self.frame, font=('Raleway', 11), background='lightgrey', anchor=NW, wraplength=460, justify=LEFT)
        self.learnHelp.configure(text='Click here to view more information about this topic. Press back to return to the main screen.')
        self.learnHelp.place(relx=.3, x=20, rely=.75, y=-20, relheight=.15, height=0, relwidth=.4, width=-40)
        
        #previous
        self.prevButton = tk.Button(self.frame, font=('Raleway', 14), text='Previous',
            border=0, background='lightblue')
        self.prevButton.place(relx=0.0, x=10, rely=.9, y=-10, relwidth=.2, relheight=.1)
        self.prevHelp = tk.Label(self.frame, font=('Raleway', 11), background='lightgrey', anchor=NW, wraplength=460, justify=LEFT)
        self.prevHelp.configure(text='Click here to revisit recently visited articles.')
        self.prevHelp.place(x=10, rely=.75, y=-20, relheight=.15, height=0, relwidth=.3, width=0)
        
        #back
        self.backButton = tk.Button(self.frame, font=('Raleway', 14), text='Back',
            border=0, background='lightblue')
        self.backButton.place(relx=0.75, x=20, y=10, relwidth=.25, width=-30, relheight=.1)
        
        #history
        self.historyButton = tk.Button(self.frame, font=('Raleway', 14), text='History',
            border=0, background='lightblue')
        self.historyButton.place(relx=0.75, x=20, rely=.1, y=20, relwidth=.25, width=-30, relheight=.1)
        self.histHelp = tk.Label(self.frame, font=('Raleway', 11), background='lightgrey', anchor=NW, wraplength=460, justify=LEFT)
        self.histHelp.configure(text='Click this to view a list of all the articles you have learned more about. Click on one of the articles to reread that article')
        self.histHelp.place(relx=.65, x=0, rely=.2, y=30, relheight=.2, height=0, relwidth=.35, width=-10)

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
        self.frame = tk.Frame(root, width=1600, height=900, background='white')
        self.frame.pack()
        
        #title
        self.title = tk.Label(self.frame, font=('Raleway', 24), text='History', background='white', anchor=SW, wraplength=1100, justify=LEFT)
        self.title.place( x=10, y=10, height=80, relwidth=.75)
        self.underline = tk.Canvas(self.frame, height=5, background='black')
        self.underline.place( x=10, y=90, height=5, relwidth=.75)

        #history
        self.historyList = []
        self.historyCount = 0
        self.history = tk.Text(self.frame, wrap="none", background='white', borderwidth=0)
        self.sb = tk.Scrollbar(orient="vertical", command=self.history.yview)
        self.history.configure(yscrollcommand=self.sb.set)
        self.sb.pack(side="right", fill="y")
        self.history.place(x=10, y=130, relheight=1.0, height=-140, relwidth=1.0, width=-20)
        self.history.configure(state="disabled")

        #back
        self.backButton = tk.Button(self.frame, font=('Raleway', 14), text='Back',
            border=0, background='lightblue')
        self.backButton.place(relx=0.75, x=20, y=10, relwidth=.25, width=-30, relheight=.1)


    def deleteHistory(self, index):
        self.historyList.pop(index)
        self.history.configure(state="normal")
        self.history.delete(0.0, END)
        self.history.configure(state="disabled")
        for i in range(len(self.historyList)):
            self.updateHistory(self.historyList[i][0], self.historyList[i][1], self.historyList[i][2], self.historyList[i][3], i)

    def addHistory(self, title, link, open, delete):
        self.history.configure(state="normal")
        i = len(self.historyList)
        a = tk.Button(self.frame, font=('Raleway', 16), text='Delete', background='red', borderwidth=0)
        a.config(command=lambda: delete(i))
        b = tk.Button(self.frame, font=('Raleway', 16), text=title, background='white', borderwidth=0)
        b.config(command=lambda: open(link))
        self.history.insert(0.0, "\n")
        self.history.window_create(0.0, window=a)
        self.history.window_create(0.0, window=b)
        self.history.configure(state="disabled")
        self.historyList.append([title, link, open, delete])

    def updateHistory(self, title, link, open, delete, index):
        self.history.configure(state="normal")
        delButton = tk.Button(self.frame, font=('Raleway', 16), text='Delete', background='red', borderwidth=0)
        delButton.config(command=lambda: delete(index))
        linkButton = tk.Button(self.frame, font=('Raleway', 16), text=title, background='white', borderwidth=0)
        linkButton.config(command=lambda: open(link))
        self.history.insert(0.0, "\n")
        self.history.window_create(0.0, window=delButton)
        self.history.window_create(0.0, window=linkButton)
        self.history.configure(state="disabled")

    def setButton(self, showmain):
        self.backButton.config(command=showmain)

    def hide(self):
        self.frame.pack_forget()
            
    def show(self):
        self.frame.pack()

