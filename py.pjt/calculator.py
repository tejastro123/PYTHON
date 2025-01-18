import tkinter as tk 
import tkinter.ttk as ttk

win = tk.Tk()
win.title("CALCULATOR")

expr = ''
text = tk.StringVar()
def press(num):
    global expr
    expr += str(num)
    text.set(expr)

def clr():
    global expr
    expr = ''
    text.set(expr)

def equal():
    global expr
    ttl = str(eval(expr))
    text.set(ttl)

entry = ttk.Entry(win,justify='right',textvariable=text)
entry.grid(row=0,columnspan=4,sticky='nsew')

button7 = ttk.Button(win,text='7',command=lambda:press(7))
button7.grid(row=1,column=0)

button8 = ttk.Button(win,text='8',command=lambda:press(8))
button8.grid(row=1,column=1)

button9 = ttk.Button(win,text='9',command=lambda:press(9))
button9.grid(row=1,column=2)

button_d = ttk.Button(win,text='/',command=lambda:press('/'))
button_d.grid(row=1,column=3)

button4 = ttk.Button(win,text='4',command=lambda:press(4))
button4.grid(row=2,column=0)

button5 = ttk.Button(win,text='5',command=lambda:press(5))
button5.grid(row=2,column=1)

button6 = ttk.Button(win,text='6',command=lambda:press(6))
button6.grid(row=2,column=2)

button_m = ttk.Button(win,text='*',command=lambda:press('*'))
button_m.grid(row=2,column=3)

button1 = ttk.Button(win,text='1',command=lambda:press(1))
button1.grid(row=3,column=0)

button2 = ttk.Button(win,text='2',command=lambda:press(2))
button2.grid(row=3,column=1)

button3 = ttk.Button(win,text='3',command=lambda:press(3))
button3.grid(row=3,column=2)

button_s = ttk.Button(win,text='-',command=lambda:press('-'))
button_s.grid(row=3,column=3)

button0 = ttk.Button(win,text='0',command=lambda:press(0))
button0.grid(row=4,column=0)

button_ = ttk.Button(win,text='.',command=lambda:press('.'))
button_.grid(row=4,column=1)

button_c = ttk.Button(win,text='c',command=clr)
button_c.grid(row=4,column=2)

button_a = ttk.Button(win,text='+',command=lambda:press('+'))
button_a.grid(row=4,column=3)

button_e = ttk.Button(win,text='=',command=equal)
button_e.grid(row=5,columnspan=4,sticky='nsew')



win.mainloop()

