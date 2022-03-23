import subprocess
import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def SaveConfig():
    if(ServLoc.get() != "" and ServFile.get() != "" and RamSize.get() != ""):
        path = ServLoc.get()
        jar = ServFile.get()
        jar = jar[len(path)+1:len(jar)]

        file = open("res\\temp\\000000.md","w")
        file.write(ServLoc.get())
        file.close()

        file = open("res\\temp\\000001.md","w")
        file.write(ServFile.get())
        file.close()

        if(BackLoc.get() != ""):
            file = open("res\\temp\\000002.md","w")
            file.write(BackLoc.get())
            file.close()
        elif(os.path.isfile("res\\temp\\000002.md")):
            os.remove("res\\temp\\000002.md")

        file = open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Server.bat","w")
        file.write("cd " + path + "\njava -Xms" + RamSize.get() + "G -Xmx" + RamSize.get() + "G -jar " + jar)
        file.close()

        if(os.path.isfile("res\\temp\\000002.md")):
            file = open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Server.bat","a")
            file.write("\ncd..\n7z a Server.7z Server\nMOVE Server.7z " + BackLoc.get())
            file.close()
        
        if(PowerActions.get() == 1):
            file = open("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Server.bat","a")
            file.write("\nshutdown /s /t0")
            file.close()

        messagebox.showinfo("Deploy", "        Done!        ")
        exit()
    else:
        messagebox.showinfo("Error", "Fill in the fields above.")

def RemoveProgram():
    os.remove("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Server.bat")
    messagebox.showinfo("Remove", "        Done!        ")
    exit()

def ServerFolder():
    ServLoc.set(filedialog.askdirectory(title="Select Folder"))

def BackupFolder():
    BackLoc.set(filedialog.askdirectory(title="Select Folder"))

def ServerFile():
    if(ServLoc.get() != ""):
        ServFile.set(filedialog.askopenfilename(filetypes=[("Java files", "*.jar")]))
    else:
        messagebox.showinfo("Error", "Select your Server Folder")

def About():
    root2 = Tk()
    root2.title("Help")
    root2.resizable(False,False)
    root2.iconbitmap("res\img\zap.ico")
    root2.config(bg="#F8F8F8")

    Label(root2, text="Instructions", bg="#F8F8F8").grid(row=0,column=1)
    Label(root2, text="1)", bg="#F8F8F8").grid(row=1,column=0)
    Label(root2, text="Rename your server folder \"Server\".", bg="#F8F8F8").grid(row=1,column=1,sticky="w")
    Label(root2, text="2)", bg="#F8F8F8").grid(row=2,column=0)
    Label(root2, text="Fill in the fields in the application.", bg="#F8F8F8").grid(row=2,column=1,sticky="w")
    Label(root2, text="3)", bg="#F8F8F8").grid(row=3,column=0)
    Label(root2, text="Press the \"deploy\" button.", bg="#F8F8F8").grid(row=3,column=1,sticky="w")
    Label(root2, text="4)", bg="#F8F8F8").grid(row=4,column=0,sticky="n")
    Label(root2, text="To remove the program restart the   \napp and press the \"Remove\" button.", bg="#F8F8F8").grid(row=4,column=1,sticky="w")
    Label(root2, text="About", bg="#F8F8F8").grid(row=5,column=1,padx=20)
    Label(root2, text="Coded by NightDarkness 2022", bg="#F8F8F8").grid(row=6,column=1)
    root2.mainloop()

root = Tk()
root.title("Server AutoSave")
root.resizable(False,False)
root.iconbitmap("res\img\zap.ico")
root.config(bg="#F8F8F8")

ServLoc = StringVar()
BackLoc = StringVar()
ServFile = StringVar()
RamSize = StringVar()
PowerActions = IntVar()

if(os.path.isfile("res\\temp\\000000.md")):
    file = open("res\\temp\\000000.md","r")
    ServLoc.set(file.read())
    file.close() 

if(os.path.isfile("res\\temp\\000001.md")):
    file = open("res\\temp\\000001.md","r")
    ServFile.set(file.read())
    file.close() 

if(os.path.isfile("res\\temp\\000002.md")):
    file = open("res\\temp\\000002.md","r")
    BackLoc.set(file.read())
    file.close() 

if(os.path.isfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp\Server.bat")):
    Remove = Button(root, text="Remove",command=RemoveProgram)
    Remove.config(cursor="hand2")
    Remove.pack(padx=100,pady=100)
else:
    Label(root, text="Server Path", bg="#F8F8F8").grid(row=0,column=0)
    Entry(root, textvariable=ServLoc).grid(row=0,column=1,pady=10)

    Search1 = Button(root, text="...",command=ServerFolder)
    Search1.config(cursor="hand2")
    Search1.grid(row=0,column=2,padx=10)

    Label(root, text="Server Executable", bg="#F8F8F8").grid(row=1,column=0)
    Entry(root, textvariable=ServFile).grid(row=1,column=1,pady=10)

    Search2 = Button(root, text="...",command=ServerFile)
    Search2.config(cursor="hand2")
    Search2.grid(row=1,column=2,padx=10)

    Label(root, text="Server Backup Destiny (Optional)", bg="#F8F8F8").grid(row=2,column=0)
    Entry(root, textvariable=BackLoc).grid(row=2,column=1,pady=10)

    Search3 = Button(root, text="...",command=BackupFolder)
    Search3.config(cursor="hand2")
    Search3.grid(row=2,column=2,padx=10)

    Label(root, text="Amount of dedicated RAM", bg="#F8F8F8").grid(row=3,column=0)
    Label(root, text="Minimum 2GB", bg="#F8F8F8").grid(row=3,column=1)
    ram = Entry(root, textvariable=RamSize, width=2)
    RamSize.set("4")
    ram.config(justify="right")
    ram.grid(row=3,column=1,sticky="e")
    Label(root, text="GB", bg="#F8F8F8").grid(row=3,column=2,sticky="w")

    Label(root, text="Power actions", bg="#F8F8F8").grid(row=4,column=0)
    Label(root, text="Shutdown on close", bg="#F8F8F8").grid(row=4,column=1,sticky="w")
    ShutdownOnClose = Checkbutton(root, variable=PowerActions)
    ShutdownOnClose.grid(row=4,column=2,sticky="W")

    Help = Button(root, text="Help",command=About)
    Help.config(cursor="hand2")
    Help.grid(row=5,column=2,padx=10)

    Deploy = Button(root, text="Deploy",command=SaveConfig)
    Deploy.config(cursor="hand2")
    Deploy.grid(row=5,column=1,padx=10)

root.mainloop()

