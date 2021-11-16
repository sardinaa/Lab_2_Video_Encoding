from tkinter import *
from clip_cutter import cut_fragment
from yuv_histogram import histogram
from resize_clip import change_resolution
from audio_to_mono import mono_codec
from tkinter.ttk import Combobox
from tkinter import messagebox
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
import os

global filename


class MyWindow(tk.Tk):

    def __init__(self, win):
        self.selected = str(0)
        self.selected_audio = str(0)
        self.filename = tk.StringVar()
        self.lbl1 = Label(win, text='Start cutting [s]')
        self.lbl2 = Label(win, text='End cutting [s]')
        self.lbl3 = Label(win, text='Choose Resolution')
        self.lbl4 = Label(win, text='Name exported file')
        self.lbl5 = Label(win, text='Name audio file')
        self.lbl6 = Label(win, text='Audio codec')
        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()
        self.btn1 = Button(win, text='Cut')
        self.btn2 = Button(win, text='Histogram')
        self.btn3 = Button(win, text='Export')
        self.btn4 = Button(win, text='Convert to mono')
        self.lbl1.place(x=15, y=50)
        self.t1.place(x=120, y=50)
        self.lbl2.place(x=15, y=75)
        self.t2.place(x=120, y=75)
        self.lbl4.place(x=15, y=210)
        self.t3.place(x=150, y=210)
        self.lbl5.place(x=15, y=280)
        self.t4.place(x=150, y=280)
        self.lbl6.place(x=15, y=310)
        self.b1 = Button(win, text='Cut', command=self.cut)
        self.b2 = Button(win, text='Histogram', command=self.hist)
        self.b3 = Button(win, text='Export', command=self.resolution)
        self.b4 = Button(win, text='Convert to mono', command=self.audio_codec)
        # self.b2.bind('<Button-1>', self.sub)
        self.b1.place(x=115, y=105)
        self.b2.place(x=115, y=140)
        self.b3.place(x=150, y=240)
        self.b4.place(x=150, y=340)
        self.lbl3.place(x=15, y=180)

        data = ["720p", "480p", "360x240p", "160x120p"]
        cb = Combobox(window, values=data)
        cb.pack()
        cb.bind('<<ComboboxSelected>>', self.on_select)
        cb.place(x=150, y=180)

        codec = [".mp3", ".wav", ".flac", ".aac"]
        cb_a = Combobox(window, values=codec)
        cb_a.pack()
        cb_a.bind('<<ComboboxSelected>>', self.on_select_audio)
        cb_a.place(x=150, y=310)

        self.open_button = Button(win, text='Open a File',
                                  command=self.select_file)
        self.open_button.pack(expand=True)
        self.open_button.place(x=115, y=10)

    def cut(self):
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num2 - num1

        if result > 0:
            cut_fragment(self.filename, int(self.t1.get()),
                         int(self.t2.get()))
        else:
            messagebox.showinfo(message="Please, choose a correct time.",
                                title="Error time selection")

    def resolution(self):
        if len(self.t3.get()) == 0 or self.selected == 0:
            messagebox.showinfo(
                message="Please, define a name and a resolution.",
                title="Selection error")
        else:
            if self.selected == "720p":
                change_resolution(self.t3.get(), 1280, 720)
            elif self.selected == "480":
                change_resolution(self.t3.get(), 854, 480)
            elif self.selected == "360x240p":
                change_resolution(self.t3.get(), 360, 240)
            else:
                change_resolution(self.t3.get(), 160, 120)

    def audio_codec(self):
        if len(self.t4.get()) == 0 or self.selected_audio == 0:
            messagebox.showinfo(message="Please, define a name and a codec.",
                                title="Selection error")
        else:
            if self.selected_audio == ".mp3":
                mono_codec(self.t4.get(), self.selected_audio)
            elif self.selected_audio == ".wav":
                mono_codec(self.t4.get(), self.selected_audio)
            elif self.selected_audio == ".flac":
                mono_codec(self.t4.get(), self.selected_audio)
            else:
                mono_codec(self.t4.get(), self.selected_audio)

    def hist(self):
        histogram("test.mp4")

    def on_select(self, event):
        self.selected = event.widget.get()

    def on_select_audio(self, event):
        self.selected_audio = event.widget.get()

    def select_file(self):
        filetypes = (
            ('MP4 files', '*.mp4'),
            ('All files', '*.*')
        )

        self.filename.set(fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes))
        self.filename = os.path.basename(self.filename.get())
        print(self.filename)


window = Tk()
mywin = MyWindow(window)
window.title('FFMPeg Editor')
window.geometry("400x420+10+10")
window.mainloop()
