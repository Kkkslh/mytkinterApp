"""
This is my python app app
For unreadable text file creation and try to code running to python secrept:
_you can use .py file extension and the editor convert to reverse text.
_you can also run python script from this editor
I'm not good at OOP structure so my class seem a function not an object

"""
############################################################
#importing the require packages
from tkinter import*
from tkinter import scrolledtext
from tkinter import filedialog as fd
from tkinter import messagebox
import subprocess
import os
import re
##########################################################
#Creating an object to get a window
class my_app():
    def __init__(self):
        self.name=''
        self.appplace()
        self.line=''
#they are function 
    def appplace(self):
        self.app=Tk()
        self.app.title("Secure Text Editor")
        self.app.iconbitmap("D:/lesson/2020_test/python/app.ico")
        self.app.geometry("659x450+400+100")
        self.textt=scrolledtext.ScrolledText(self.app,fg="black",bg="white")
        self.textt.pack(anchor='nw',expand=1,fill="both",pady=35)
        self.comm=Label(text="You can use .ay extension for secure text file",font=("Courier",11))
        self.comm.place(x=5,y=10)
        #menu bar Creating
        self.menubar=Menu(self.app)
        self.filemenubar=Menu(self.menubar,tearoff=0)
        self.filemenubar.add_command(label="New",command=self.new)
        self.filemenubar.add_command(label="Open",command=self.fileopen)
        self.filemenubar.add_command(label="Save",command=self.filesave)
        self.filemenubar.add_command(label="Save as",command=self.filesaveas)
        self.filemenubar.add_command(label="Exit",command=self.exit)
        self.menubar.add_cascade(label="File",menu=self.filemenubar)

        self.editmenu=Menu(self.menubar,tearoff=0)
        self.editmenu.add_command(label="Undo",command=self.donothing)
        self.editmenu.add_command(label="Copy",command=self.donothing)
        self.editmenu.add_command(label="Paste",command=self.donothing)
        self.editmenu.add_command(label="Find",command=self.donothing)
        self.editmenu.add_command(label="Find and replace",command=self.donothing)
        self.menubar.add_cascade(label="Edit",menu=self.editmenu)

        self.Theme=Menu(self.menubar,tearoff=0)
        self.Theme.add_command(label="Light",command=lambda : self.theme("white","black","black"))
        self.Theme.add_command(label="Dark",command=lambda : self.theme("#201130","white","white"))
        self.menubar.add_cascade(label="Theme",menu=self.Theme)

        self.code=Menu(self.menubar,tearoff=0)
        self.code.add_command(label="Run",command=self.runT)
        self.code.add_command(label="Excute",command=self.excT)
        self.menubar.add_cascade(label="Code",menu=self.code)

        self.help=Menu(self.menubar,tearoff=0)
        self.help.add_command(label="About s_editor",command=self.donothing)
        self.menubar.add_cascade(label="Help",menu=self.help)
        self.app.config(menu=self.menubar)
    ####################################################
    #for switch dark and light theme
    def theme(self,bgcolor,fgcolor,cusorc):
        self.line=self.textt.get(1.0,END)
        self.textt.config(bg=bgcolor,fg=fgcolor,insertbackground=cusorc)
    #########################################################################################################
    def donothing(self):
        pass
    #clearing the text from the my text window
    def clearText(self):
        self.textt.delete("1.0",END)
    ##########################################
    #for opening file
    def open_secure(self,f_name):
        f=open(f_name,'r+')
        self.line=f.read()
        self.line=self.line[::-1] 
        self.clearText()
        self.textt.insert('1.0',self.line)
        f.close()
    
    def open_nfile(self,f_name):
        f=open(f_name,'r+')
        self.clearText()
        self.textt.insert(1.0,f.read())
        f.close()

    def fileopen(self):
        self.line=''
        self.line=self.textt.get(1.0,END +'-1c')
        if self.line=='':
            self.write()
        else:   
            test=messagebox.askyesno(title="warning",message="Do you want to save this file")
            if test==True:
                self.filesave()
                self.write()
            else:
                self.write()

    def write(self):
        self.name=fd.askopenfilename()
        self.ftitle=self.name.split("/")
        if self.name!='':
            if self.name[-2:]=='ay':
                self.open_secure(self.name)
                self.app.title(self.ftitle[-1])
            else:
                self.open_nfile(self.name)
                self.app.title(self.ftitle[-1])
        else:
            pass
        
    ##############################################
    #for saving file 
    def save_secure(self,f_name):
        f=open(f_name,'w+')
        self.line=self.textt.get(1.0,END)
        self.line=self.line[::-1]
        f.write(self.line)
        f.close()

    def save_normal(self,f_name):
        f=open(f_name,'w+')
        f.write(self.textt.get(1.0,END))
        f.close()    

    def filesaveas(self):
        self.name=fd.asksaveasfilename()
        self.ftitle=self.name.split("/")
        if self.name!='':
            if self.name[-2:]=='ay':
                self.save_secure(self.name)
                self.app.title(self.ftitle[-1])
            else:   
                self.save_normal(self.name)
                self.app.title(self.ftitle[-1])
        else:
            pass
    #################################
    def filesave(self):
        if self.name=='':
            self.filesaveas()
        elif self.name[-2:]=='ay':
            self.save_secure(self.name)
        else:
            self.save_normal(self.name)
    ######################################################
    #for running python script
    def runT(self):
        if self.name!='':
            self.run()
        else:
            test=messagebox.askyesno(title="warning",message="Do you want to save this file")
            if test==True:
                self.filesaveas()
                self.run()
    #to run python script calling cmd from the system
    #but this code will not work other operating system
    def run(self):
        if self.name[-3:]=='.py':
            os.system("python {}".format(self.name))
            #subprocess.run(["python",self.name],shell=True)
        elif self.name[-2:]=='.c'or self.name[-4:]=='.cpp':
            os.system("gcc {}".format(self.name))
        else:
            messagebox.showerror("Error","File name error")
    #######################################################
    #for excuting python script
    def excT(self):
        if self.name!='':
            self.exc()
        else:
            test=messagebox.askyesno(title="warning",message="Do you want to save this file")
            if test==True:
                self.filesaveas()
                self.run()
    #to excute python script calling cmd from the system
    #but this code wouldn't work other operating system
    def exc(self):
        if self.name[-3:]=='.py':
            self.name=re.sub(r"\/",r"\\",self.name)
            test=messagebox.askokcancel("icon","Do you want to add app icon")
            if test==True:
                icon=fd.askopenfilename()
                if icon[-3:]=='ico':
                    os.system("pyinstaller.exe --onefile --windowed --icon={} {}".format(icon,self.name))
                    #subprocess.run(["pyinstaller.exe","--onefile","--windowed","--icon=",icon,self.name],shell=True)
            else:
                os.system("pyinstaller.exe --onefile --windowed {}".format(self.name))
                #subprocess.run(["pyinstaller.exe","--onefile","--windowed",self.name],shell=True)
        elif self.name[-2:]=='.c'or self.name[-4:]=='.cpp':
            name=self.name.split(r"\/")
            name=name[-1]
            name=re.sub(r".c",".exe",name)
            os.system("gcc -o {} {}".format(name,self.name))
            #subprocess.run(["gcc","-o",name,self.name],shell=True)
        else:
            messagebox.showerror("Error","File name error")
    #######################################################
    #for exiting from the tkinter window
    def exit(self):
        if self.line=='':
            self.filesave()
            self.app.destroy()
        else:
            self.app.destroy()
    #########################################
    #for creating new window
    def new(self):
        new=my_app()
        new.app_runner()
    ####################################################
    #running my editor
    def app_runner(self):
        self.app.mainloop()
    ####################################################
aye_app=my_app()
aye_app.app_runner()

