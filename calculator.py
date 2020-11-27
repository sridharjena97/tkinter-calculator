'''
Author: Sridhar JENA
Company: Sridhwork
Created on: 21-November-2020
Purpose: General Calculator Program
'''
from tkinter import *
import time
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x580")
        self.minsize(400,580)
    def statusbar(self):
        '''
        To show status at buttom of GUI
        '''
        self.status=StringVar()
        self.status.set("Ready")
        self.sbar=Label(self,textvariable=self.status,relief=SUNKEN,anchor="w")
        self.sbar.pack(side=BOTTOM,fill=X)
    def update_status(self,state="Ready"):
        '''
        To update status of GUI
        '''
        self.status.set(state)
        self.sbar.update()
    def create_button(self,master=None,btntxt="Button",bg="sky blue",relief=RAISED,bd=6,funcname=None,side=None,padx=3,pady=3,anchor=None,ipadx=10,ipady=None,**kwargs):
        '''
        To Create a button
        '''
        kargs={}
        for key,value in kwargs.items():
            kargs.__setitem__(key,value)
        btn=Button(master,text=btntxt,command=funcname,bg=bg,relief=relief,bd=bd,**kargs)
        btn.pack(side=side,padx=padx,pady=pady,anchor=anchor,ipadx=ipadx,ipady=ipady)
        btn.bind("<Button-1>", click)
        
    
# Fonts
dfont="Consolas 40 bold"
font1="Lucida 22 bold"
font2="Lucida 15 bold"
# methods
# Responding to Enter events when typing manually.
def enter(event):
    global dtext
    if dtext.get().isdigit():
        value= int(dtext.get())
    else:
        try:
            value=eval(dtext.get())
        except:
            value=""
            dtext.set("Error")
            display.update()
            time.sleep(2)
    dtext.set(value)
    display.update()
# Responding to mouse clicks on gui
def click(event):
    global dtext
    text= event.widget.cget("text")
    if text=="=":
        if dtext.get().isdigit():
            value= int(dtext.get())
        else:
            try:
                value=eval(dtext.get())
            except:
                value=""
                dtext.set("Error")
                display.update()
                time.sleep(2)
        dtext.set(value)
        display.update()
    elif text=="C":
        dtext.set("")
        display.update()
    elif text=="<-":
        str=dtext.get()
        str=str[:-1]
        dtext.set(str)
        display.update()
    else:
        dtext.set(dtext.get()+text)
        display.update()

if __name__ == "__main__":
    window=GUI()
    # window.statusbar()
    # window title
    window.title("Calculator")
    # Setting dark background
    window.configure(bg="gray16")
    # Setting icon of the app
    window.wm_iconbitmap("icon.ico")
    # creating a varibale
    dtext=StringVar()
    dtext.set("")
    # Display of calculator
    display= Entry(window,textvar=dtext,bd=10,relief=RIDGE,justify=RIGHT,font=dfont,bg="gray80")
    display.pack(anchor="w",pady=5,padx=5,fill=X,ipady=5)
    # Binding event to display
    display.bind("<Return>", enter)
    # creating buttons
    # section-1
    frame1= Frame(window,bg="grey11")
    frame1.pack(anchor="w",padx=5,pady=5,fill=X)
    window.create_button(master=frame1,btntxt="C",font=font1,side=LEFT,ipadx=17,bg="yellow")
    window.create_button(master=frame1,btntxt="(",font=font1,side=LEFT,ipadx=3,bg="DodgerBlue2")
    window.create_button(master=frame1,btntxt=")",font=font1,side=LEFT,ipadx=3,bg="DodgerBlue2")
    
    frame2=Frame(frame1,bg="gray11")
    frame2.pack(side=RIGHT,anchor="ne")
    window.create_button(master=frame2,btntxt="<-",font=font1,ipadx=35,bg="red")
    # section-2
    frame3=Frame(window,bg="grey11")
    frame3.pack(anchor="w",padx=5,pady=5,fill=X)
    window.create_button(master=frame3,btntxt="9",font=font1,side=LEFT)
    window.create_button(master=frame3,btntxt="8",font=font1,side=LEFT)
    window.create_button(master=frame3,btntxt="7",font=font1,side=LEFT)

    frame4=Frame(frame3,bg="gray11")
    frame4.pack(side=RIGHT,anchor="ne",ipady=9)
    window.create_button(master=frame4,btntxt="*",font=font1,side=LEFT,ipadx=18,bg="DodgerBlue2")
    window.create_button(master=frame4,btntxt="/",font=font1,side=LEFT,ipadx=18,bg="DodgerBlue2")
    # section-3
    frame5=Frame(window,bg="grey11")
    frame5.pack(anchor="w",padx=5,pady=5,fill=X)
    window.create_button(master=frame5,btntxt="6",font=font1,side=LEFT)
    window.create_button(master=frame5,btntxt="5",font=font1,side=LEFT)
    window.create_button(master=frame5,btntxt="4",font=font1,side=LEFT)

    frame6=Frame(frame5,bg="gray11")
    frame6.pack(side=RIGHT,anchor="ne",ipady=9)
    window.create_button(master=frame6,btntxt="**",font=font1,side=LEFT,ipadx=12,bg="DodgerBlue2")
    window.create_button(master=frame6,btntxt="%",font=font1,side=LEFT,ipadx=10,bg="DodgerBlue2")
    # Section-4
    frame7=Frame(window,bg="grey11")
    frame7.pack(anchor="w",padx=5,pady=5,fill=X)
    window.create_button(master=frame7,btntxt="3",font=font1,side=LEFT)
    window.create_button(master=frame7,btntxt="2",font=font1,side=LEFT)
    window.create_button(master=frame7,btntxt="1",font=font1,side=LEFT)

    frame8=Frame(frame7,bg="gray11")
    frame8.pack(side=RIGHT,anchor="ne")
    window.create_button(master=frame8,btntxt="-",font=font1,side=LEFT,ipadx=15,bg="salmon1",ipady=9)
    window.create_button(master=frame8,btntxt="+",font=font1,side=LEFT,ipadx=17,bg="tomato2",ipady=9)
    # Section-5
    frame9=Frame(window,bg="grey11")
    frame9.pack(anchor="w",padx=5,pady=5,fill=X)
    window.create_button(master=frame9,btntxt=".",font=font1,side=LEFT,ipadx=14)
    window.create_button(master=frame9,btntxt="0",font=font1,side=LEFT)
    window.create_button(master=frame9,btntxt="00",font=font2,side=LEFT,ipady=9,padx=5)

    frame10=Frame(frame9,bg="gray11")
    frame10.pack(side=RIGHT,anchor="ne")
    window.create_button(master=frame10,btntxt="=",font=font1,side=LEFT,ipadx=55,bg="green")

    window.mainloop()