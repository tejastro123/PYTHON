from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob

root = Tk()
root.title("Google Translate")
root.geometry("1080x400")

#icon
image_icon = PhotoImage(file="D:\PROJECTS\PYTHON\GUI\googletrans.png")
root.iconphoto(False,image_icon)

#arrow
arrow_image = PhotoImage(file="D:\PROJECTS\PYTHON\GUI\arrow.png")
image_label = Label(root, image=arrow_image,width=150)
image_label.place(x=460,y=50)



language = googletrans.LANGUAGES
languageV = list(language.values())
lang1= language.keys()

combo1=ttk.Combobox(root,values=languageV,font="Roboto 15",state="r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right",fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)




combo2=ttk.Combobox(root,values=languageV,font="Roboto 15",state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1=Frame(root,bg="black",bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2=Text(f,font="Roboto 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

root.configure(bg="white")
root.mainloop()