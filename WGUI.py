from tkinter import *
import webbrowser

# Creating webbrowser function to open new tab when user clicks ok
def wbbrowser():
    f = open('index.html','w')
    text = source.get()
    message = "<html><head></head><body><p>%s</p></body</html>" % text
    f.write(message)
    f.close()
    webbrowser.open_new_tab('index.html')

# Gui Instance
wbGui = Tk()
source = StringVar()


wbGui.geometry('450x450+500+300')
wbGui.title('Web Browser')

wblabel = Label(wbGui,text='Type Your Text Below').pack()

wbbutton = Button(wbGui,text="Open Browser",command = wbbrowser).pack()

wbEntry = Entry(wbGui,textvariable=source).pack()
