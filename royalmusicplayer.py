from tkinter import *
from tkinter import filedialog as fd
import pygame
from pygame import mixer
musicList = {}
musicPlayer = Tk()
mixer.init()
musicPlayer.title('Music Player')
musicPlayer.geometry('700x600')

songV = StringVar()
curr = StringVar()

def open():
    num = 1
    
    filetypes = (
        ('mp3 files', '*.mp3'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilenames(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
    
    for son in filename:
        c = son.split('/')
        Lb1.insert(END,c[-1])
        musicList[c[-1]] = son
        num += 1
    

def play():
    for i in Lb1.curselection():
        currentsong=Lb1.get(i)
    songV.set(currentsong)
    mixer.music.load(musicList[currentsong])
    curr.set('Playing...')
    mixer.music.play()


def pause():
    curr.set("Paused")
    mixer.music.pause()

def stop():
    curr.set("Stopped")
    mixer.music.stop()

def resume():
    curr.set("Resuming")
    mixer.music.unpause()

name = Label(musicPlayer, text='Royal Music Player',font= 20)
name.pack()

currentPlay = Label(musicPlayer,textvariable=curr)
currentPlay.pack()

playing = Label(musicPlayer,textvariable= songV)
playing.pack()

frame1 = Frame(musicPlayer)
frame1.pack()

Lb1 = Listbox(frame1, height= 20, width= 50,selectmode=SINGLE)
Lb1.pack(side=LEFT)

Lb2 = Listbox(frame1, height= 20, width= 50,selectmode=SINGLE)
Lb2.pack(side=LEFT)

openbtn = Button(musicPlayer, text= 'Open',command=open,width= 40)
openbtn.pack()

playbtn = Button(musicPlayer, text= 'Play',command=play,width= 40)
playbtn.pack()

pausebtn = Button(musicPlayer, text= 'Pause',command=pause,width= 40)
pausebtn.pack()

stopbtn = Button(musicPlayer, text= 'Stop',command=stop,width= 40)
stopbtn.pack()

resumebtn = Button(musicPlayer, text= 'Resume',command=resume,width= 40)
resumebtn.pack()

exitbtn = Button(musicPlayer, text= 'Exit',command=exit,width= 40)
exitbtn.pack()

mainloop()