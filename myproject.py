from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=57380c692669fa1143df0589592f46e6").json()

    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15))+" degree")
    p_label1.config(text =str(int(data["main"]["pressure"]))+" mbar")
    wind_label1.config(text =str(int(data["wind"]["speed"]))+" km/h")
    
 
win = Tk()
win.title("Weather App(Internet Required)")
win.config(bg="Teal")
win.geometry("500x550")

name_label = Label(win,text ="VITA Weather App",font=("Verdana",20,"bold"))
name_label.place(x = 50,y = 50,height = 50,width =400 )

city_name = StringVar()

list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com = ttk.Combobox(win, values=list_name, font=("Verdana", 12),textvariable = city_name)
com.place(x = 100,y = 120 ,height = 40,width =300)

w_label =Label(win,text="Weather Climate",font=("Verdana",13))
w_label.place(x=25,y=250,height=40,width=200)
w_label1 =Label(win,text="",font=("Verdana",13))
w_label1.place(x=250,y=250,height=40,width=200)

wb_label = Label(win,text="Weather Discription",font=("Verdana",13))
wb_label.place(x=25,y=300,height=40,width = 200)
wb_label1 = Label(win,text="",font=("Verdana",13))
wb_label1.place(x=250,y=300,height=40,width = 200)

temp_label = Label(win,text="Temperature",font=("Verdana",13))
temp_label.place(x = 25,y = 350 , height = 40,width = 200)
temp_label1 = Label(win,text="",font=("Verdana",13))
temp_label1.place(x = 250,y = 350 , height = 40,width = 200)

p_label = Label(win,text="Pressure",font=("Verdana",13))
p_label.place(x = 25,y = 400 , height = 40,width = 200)
p_label1 = Label(win,text="",font=("Verdana",13))
p_label1.place(x = 250,y = 400 , height = 40,width = 200)

wind_label = Label(win,text="Wind Speed",font=("Verdana",13))
wind_label.place(x = 25,y = 450 , height = 40,width = 200)
wind_label1 = Label(win,text="",font=("Verdana",13))
wind_label1.place(x = 250,y = 450 , height = 40,width = 200)

done_button = Button(win,text = "Done",font=("Verdana",15),command = data_get)
done_button.place(x=200,y=180,height=40,width=100)

win.mainloop()

