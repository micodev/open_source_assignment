# imported libraries
from textblob import TextBlob
from tkinter import *
# setup window
window = Tk()
window.geometry("350x370")
window.title("Translator Multi language")
# utilites
nth = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth"
}
frames = []
chk_values=[]
lang_chckbox = []
to_lang = ['english','Arabic','French','Portuguese']
to_suffix=['en','ar','fr','pt']
lbfs=[]

# events if happens
def checkit(event=""):
    for lbfi in lbfs:
        lbfi.grid_forget()
    for i in range(0,len(chk_values)):
        if(chk_values[i].get()):
            lbf=LabelFrame(window,text=to_lang[i]+" translation")
            tr =""
            try:
                tr = TextBlob(from_.get()).translate(from_lang='auto',to=to_suffix[i])
            except:
                tr = from_.get()
            label = Label(lbf,text=tr,bg="red")
            label.grid(column=0,row=0)
            lbf.grid(column=0,row=i+3,columnspan=4)
            lbfs.append(lbf)
        
# dynamic checkbox maker
for i in range(0,len(to_lang)):
    chk_values.append(BooleanVar())
    ch = Checkbutton(window,text =to_lang[i],variable=chk_values[len(chk_values)-1],command=checkit)
    ch.grid(column=i,row=2)
    lang_chckbox.append(ch)

# make trnalsation form

from_label = Label(window,text="Please insert your text :")
from_ = Entry(window,text="")
from_.bind("<KeyRelease>",checkit)

# setup globally grid     
from_label.grid(column=2,row=0)
from_.grid(column=2,row=1)          
window.mainloop()
