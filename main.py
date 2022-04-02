from pygame import mixer
from tkinter import *
import os
from PIL import Image, ImageTk


root = Tk()
root.title("Fazz Music")
root.geometry("300x400+600+150")
root.resizable(width=False, height=False)
root.iconbitmap("img/FazzMusic.ico")
backgroundColor = Label(bg="#0ECC4D", width=300, height=400)
backgroundColor.place(x=0, y=0)


def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    mixer.music.play()

def stopsong():
    mixer.music.stop()

def pausesong():
    mixer.music.pause()


def resumesong():
    mixer.music.unpause()

mixer.init()


playlist=Listbox(root,selectmode=SINGLE, bg="#2E2A2C", fg="white", font="arial 15", width=23)
playlist.place(x=22, y=30)


songs=os.listdir(r'./playlist')


for s in songs:
    playlist.insert(END,s)


buttons = Label(bg="#202523", width=35, height=4)
buttons.place(x=25, y=300)

resim1 = ImageTk.PhotoImage(Image.open("img/play.png"))

Button1 = Button(image=resim1, width=50, height=50, bg="#202523", command=playsong)
Button1.place(x=90, y=305)

resim2 = ImageTk.PhotoImage(Image.open("img/stop.png"))

Button2 = Button(image=resim2, width=50, height=50, bg="#202523", command=stopsong)
Button2.place(x=160, y=305)

Button3 = Button(text="Pause", bg="#444044", fg="#0ECC4D", command=pausesong)
Button3.place(x=40, y=320)

Button4 = Button(text="Resume", bg="#444044", fg="#0ECC4D", command=resumesong)
Button4.place(x=220, y=320)

songs=os.chdir(r'./playlist')

root.mainloop()