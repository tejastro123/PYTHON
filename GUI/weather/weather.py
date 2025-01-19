from tkinter import *
import tkinter as tk
from geopy.geocoders import nominatim
from tkinter import ttk,messagebox
from timezonefinder import timezonefinder
from datetime import datetime
import pytz
import requests

root = Tk()
root.title("Weather App")
root.geometry("900x500")
root.resizable(False,False)

def getweather():
    try:
        city=textfield.get()

        geolocator= nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj = timezonefinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=timezonefinder.now(home)
        current_time = local_time.strftime("%I: %M &p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

    #WEATHER
        api = " https://api.openweathermap.org/data/2.5/weather?q"+city+"&appid=a6895b9e9143b6ee504c4188adf25a19"

        json_data = requests.get(api).json 
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        pressure = json_data['main']['pressure']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        d.config(text=(description))
        h.config(text=(humidity))
        w.config(text=(wind))
        p.config(text=(pressure))
    
    except Exception as e:
        messagebox.showerror("Weather App","Invalid")



#search box
search_image=PhotoImage(file="GUI/weather/search.png")
myimage=Label(image=search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon=PhotoImage(file="GUI/weather/search_icon.png")
myimage_icon=Button(image=search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
myimage_icon.place(x=400,y=34)

#logo
logo_image=PhotoImage(file="GUI/weather/logo.png")
logo=Label(image=logo_image)
logo.place(x=150,y=100)

#bottom box
Frame_image=PhotoImage(file="GUI/weather/box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.place(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef")
w.place(x=120,y=430)
h=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef")
h.place(x=280,y=430)
d=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef")
d.place(x=450,y=430)
p=Label(text="...",font=("arial",20,"bold"),fg="#1ab5ef")
p.place(x=670,y=430)

    