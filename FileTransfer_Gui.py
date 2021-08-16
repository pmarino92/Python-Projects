from tkinter import *
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog



#Defining CreateWidgets() function to
#create necessary tkinter widgets
def CreateWidgets():
    link_Label = Label(root, text="Select File: ", bg="#E8D579")
    link_Label.grid(row = 1, column = 0, pady = 5, padx = 5)

    root.sourceText = Entry(root, width = 50, textvariable = sourceLocation)
    root.sourceText.grid(row = 1, column = 1, pady = 5, padx = 5, columnspan = 2)

    source_browseButton = Button(root, text="Browse", command = SourceBrowse, width = 15)
    source_browseButton.grid(row = 1, column = 3, pady = 5, padx = 5)

    destinationLabel = Label(root, text="Select The Destination: ", bg="#E8D579")
    destinationLabel.grid(row = 2, column = 0, pady = 5, padx = 5)

    root.destinationText = Entry(root, width = 50, textvariable = destinationLocation)
    root.destinationText.grid(row = 2, column = 1, pady = 5, padx = 5, columnspan = 2)

    dest_browseButton = Button(root, text = "Browse", command = DestinationBrowse, width = 15)
    dest_browseButton.grid(row = 2, column = 3, pady = 5, padx = 5)

    copyfileButton = Button(root, text="Copy File", command = CopyFile, width = 15)
    copyfileButton.grid(row = 3, column = 1, pady = 5, padx = 5)

    moveButton = Button(root, text="Move File", command = MoveFile, width = 15)
    moveButton.grid(row = 3, column = 2, pady = 5, padx = 5)

def SourceBrowse(): #function allowing users to select files to copy for transfer
    root.files_list = list(filedialog.askopenfilenames(initialdir = "/Users/phili/OneDrive/Desktop/New Files/"))
    root.sourceText.insert('1', root.files_list)

def DestinationBrowse(): #function allowing users to select destination folder
    destinationdirectory = filedialog.askdirectory(initialdir = "/Users/phili/OneDrive/Desktop/Receiving Files/")
    root.destinationText.insert('1', destinationdirectory)

def CopyFile():
    #Retrieving the source file selected by user
    #storing it in a variable named 'files_list'
    files_list = root.files_list
    #Retrieving the destination location
    #Storing in destination_location
    destination_location = destinationLocation.get()

    for f in files_list:
        shutil.copy(f, destination_location)
    messagebox.showinfo("SUCCESSFUL")

def MoveFile():
    files_list = root.files_list
    destination_location = destinationLocation.get()

    #Looping through the files present in the list
    for f in files_list:
        #moving the file to the destination
        shutil.move(f, destination_location)
    messagebox.showinfo("SUCCESSFUL")

#Creating object of tk class
root = tk.Tk()

root.geometry('830x120')
root.title("File Transfer GUI")
root.config(background="black")

# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()
     
# Calling the CreateWidgets() function
CreateWidgets()
     
# Defining infinite loop
root.mainloop()
    
                           
