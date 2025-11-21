import tkinter as tk
from tkinter import*
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
root=Tk()
root.title("Text to speech")
root.geometry("900x450")
root.resizable(False,False)
root.configure(bg="#305065")


def speaknow():
    engine = pyttsx3.init()  
    
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    if gender == "male":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)

    if speed == "fast":
        engine.setProperty("rate", 250)
    elif speed == "normal":
        engine.setProperty("rate", 150)
    else:
        engine.setProperty("rate", 60)

    engine.say(text)
    engine.runAndWait()
    engine.stop()


def download():
    engine = pyttsx3.init() 
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty("voices")

    if gender == "male":
        engine.setProperty("voice", voices[0].id)
    else:
        engine.setProperty("voice", voices[1].id)

    if speed == "fast":
        engine.setProperty("rate", 250)
    elif speed == "normal":
        engine.setProperty("rate", 150)
    else:
        engine.setProperty("rate", 60)

    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        engine.save_to_file(text, "text.mp3")
        engine.runAndWait()
        engine.stop()
    

#icon
image_icon=PhotoImage(file="C:/Users/Dell/Downloads/speaker logo.png")
root.iconphoto(False,image_icon)

#top frame
Top_frame=Frame(root,bg="white",width=900,height=100)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="C:/Users/Dell/Downloads/speaker logo.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)
Label(Top_frame,text="TEXT TO SPEECH",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)

text_area=Text(root,font="robote 20",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)

gender_combobox=Combobox(root,values=["male","female"],font="arial 14",state="r",width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set("male")


speed_combobox=Combobox(root,values=["fast","normal","slow"],font="arial 14",state="r",width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set("normal")

imageicon=PhotoImage(file="C:/Users/Dell/Downloads/speak.png")
btn=Button(root,text="speak",compound=LEFT,image=imageicon,width=130,font="arial 14 bold",command=speaknow)
btn.place(x=550,y=280)


imageicon2=PhotoImage(file="C:/Users/Dell/Downloads/download.png")
save=Button(root,text="save",compound=LEFT,image=imageicon2,width=130,bg="#39c790",font="arial 14 bold",command=download)
save.place(x=730,y=280)


root.mainloop()
