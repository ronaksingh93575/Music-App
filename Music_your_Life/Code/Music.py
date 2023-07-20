from tkinter import *
import tkinter as tk #used to develop GUI
from tkinter import filedialog
from tkinter.filedialog import askdirectory #it permit to select dir
from pygame import mixer #used to create video games
import os #it permits to interact with the operating system
from PIL import Image, ImageTk
# You can call functions or use variables from the turtle_animation_module here
# For example, if you have a function called `start_animation` in turtle_animation_module,
# you can call it like this:



music_player = tk.Tk() 
music_player.title("Music your Life") 
music_player.geometry("900x670+290+85")
music_player.configure(bg ="#0f1a2b")
music_player.resizable(False,False)

mixer.init()

def open_folder():
    path= filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs=os.listdir(path)
        # print(songs)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END,song)

def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text = music_name[0:64])

#icons
image_icon=ImageTk.PhotoImage(file = "r.png")
music_player.iconphoto(False,image_icon)

Top = ImageTk.PhotoImage(file = "top.png")
Label(music_player,image=Top,bg = "#0f1a2b").pack()

#button
play_button=ImageTk.PhotoImage(file="play2.png")
Button(music_player, image=play_button,bg= "#0f1a2b",bd =0 , command=play_song ).place(x=92,y=350)

stop_button=ImageTk.PhotoImage(file="stop.png")
Button(music_player, image=stop_button,bg= "#0f1a2b",bd =0 , command=mixer.music.stop).place(x=92,y=480)

# pause_button=ImageTk.PhotoImage(file="pause.png")
# Button(music_player, image=pause_button,bg= "#0f1a2b",bd =0 , command=mixer.music.pause).place(x=155,y=500)

# reusme_button=ImageTk.PhotoImage(file="resume.png")
# Button(music_player, image=reusme_button,bg= "#0f1a2b",bd =0 , command=mixer.music.unpause).place(x=250,y=500)

#lable
music=Label(music_player,text="", font=("arial",15),fg="white",bg="#0f1a2b")
music.place(x=80,y=290)

#logo
Logo = ImageTk.PhotoImage(file="music.png")
Label(music_player, image=Logo, bg ="#0f1a2b").place(x=400 ,y=130)

#music
Menu = ImageTk.PhotoImage(file="menu.png")
Label(music_player,image=Menu,bg="#0f1a2b").pack(padx=10,pady=50,side=RIGHT)

music_frame =Frame(music_player,bd=2,relief=RIDGE)
music_frame.place(x=330 ,y=400 ,width=560 ,height=250)

Button(music_player,text= "Open Folder" ,width=15,height=2, font=("arial",10,"bold"),fg="white",bg="#21b3de", command=open_folder).place(x=330, y=350)
scroll = Scrollbar(music_frame)
playlist=Listbox(music_frame,width=100,font=("arial",10),bg="#333333", fg="grey", selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT,fill=BOTH)

music_player.mainloop()
