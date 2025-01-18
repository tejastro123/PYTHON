import code
from tkinter import *
from tkinter import messagebox
import base64
import os
from turtle import reset

def decrypt():
    password = code.get()

    if password == "1234":
       screen2 = Toplevel(screen2)
       screen2.title("decryption")
       screen2.geometry("400x200")
       screen2.configure(bg="#00bd56")

       message = text2.get(1.0,END)
       decode_message = message.encode("ascii")
       base64_bytes=base64.b64decode(decode_message)
       decrypt = base64_bytes.decode("ascii")

       Label(screen2, text="DECRYPT", fg="white", font="arial", bg="#ed3833").place(x=10,y=0)
       text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
       text2.place(x=10,y=40,width=380,height=150)

       text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("encryption", "Please enter the password")
    elif password != "1234":
        messagebox.showerror("encryption", "Invalid password")

def encrypt():
    password = code.get()

    if password == "1234":
       screen1 = Toplevel(screen1)
       screen1.title("encryption")
       screen1.geometry("400x200")
       screen1.configure(bg="#ed3833")

       message = text2.get(1)
       encode_message = message.encode("ascii")
       base64_bytes=base64.b64encode(encode_message)
       encrypt = base64_bytes.decode("ascii")

       Label(screen1, text="ENCRYPT", fg="white", font="Arial", bg="#ed3833").place(x=10,y=0)
       text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
       text2.place(x=10,y=40,width=380,height=150)

       text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("encryption", "Please enter the password")
    elif password != "1234":
        messagebox.showerror("encryption", "Invalid password")





def main_screen():
    screen = Tk()
    screen.geometry("400x400")

    #icon
    image_icon = PhotoImage(file="keys.png")
    screen.iconphoto(False, image_icon)
    
    #title
    screen.title("E-D APP")
    
    #labels
    Label(text="Enter text for encryption and decryption", fg="black",font=("calbri",15).place(X=10, Y=10))
    
    #entry box
    text1 = Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter Secret key  for encryption and decryption", fg="black",font=("calbri",15).place(X=10, Y=170))

    code=StringVar()
    Entry(textvariable=code,width=20,bd=0,font=("arial",25),show="*").place(X=10, Y=200)

    Button(text="ENCRYPT",height="2",width=23,bg="#ed3833",fg="white",bd=0,command=encrypt).place(X=10, Y=150)
    Button(text="DECRYPT",height="2",width=23,bg="#00bd56",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,bg="#1089ff",fg="white",bd=0,command=reset).place(x=10,y=300)


    
    screen.mainloop()