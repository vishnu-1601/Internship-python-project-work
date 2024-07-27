from tkinter import *
from tkinter import filedialog
from PIL import ImageTk
import os
import time
from pygame import mixer
from mutagen.mp3 import MP3

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("620x514")
        self.root.configure(background='black')

        mixer.init()

        # Background image
        self.bg_image = ImageTk.PhotoImage(file='3m.jpg')
        bg_label = Label(self.root, image=self.bg_image,bg='black')
        bg_label.place(x=0, y=28)

        # Labels
        self.file_label = Label(self.root, text='No file selected', bg='black', fg='PeachPuff2', font=('Helvetica', 12))
        self.file_label.place(x=20,y=18)

        self.status_label = Label(self.root, text='Welcome to Music Player', bg='gray50', fg='black', font=('Helvetica', 12))
        self.status_label.pack(pady=0, side=BOTTOM, fill=X)

        # Initialize paused and filename
        self.paused = False
        self.filename = None

        # Choose Music button
        choose_button = Button(self.root, text="Choose Music", command=self.choose_music)
        choose_button.place(x=525,y=12)

        # Play button
        self.play_image = ImageTk.PhotoImage(file='p3.png')
        play_button = Button(self.root, image=self.play_image,bg='black',bd=0 ,command=self.play_music)
        play_button.place(x=268,y=447)

        # Pause button
        self.pause_image = ImageTk.PhotoImage(file='paus.jpg')
        pause_button = Button(self.root, image=self.pause_image,bg='black',bd=0 ,command=self.pause_music)
        pause_button.place(x=315,y=446)

        # Stop button
        self.stop_image = ImageTk.PhotoImage(file='s1.png')
        stop_button = Button(self.root, image=self.stop_image,bg='black',bd=0 ,command=self.stop_music)
        stop_button.place(x=215,y=446)

        # Volume control
        self.vol_image = ImageTk.PhotoImage(file='soun.png')
        volume_button = Button(self.root, image=self.vol_image,bg='black',bd=0 ,command=self.mute_unmute)
        volume_button.place(x=473,y=455)

        self.scale = Scale(self.root, from_=0, to=100, orient=HORIZONTAL, command=self.set_volume)
        self.scale.set(80)
        mixer.music.set_volume(0.7)
        self.scale.place(x=505,y=446)

    def choose_music(self):
        self.filename = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3")])
        if self.filename:
            self.file_label['text'] = os.path.basename(self.filename) + ' is playing....'
            self.play_music()
        else:
            self.file_label['text'] = 'No file selected'

    def play_music(self):
        try:
            if not self.filename:
                self.status_label.config(text="No file selected")
                return

            if self.paused:
                mixer.music.unpause()
                self.status_label.config(text="Music Resumed")
                self.paused = False
            else:
                mixer.music.load(self.filename)
                mixer.music.play()
                self.status_label.config(text="Music Playing")
                self.song_length = MP3(self.filename).info.length
                self.update_duration()
        except Exception as e:
            self.status_label.config(text=f"Error: {e}")

    def pause_music(self):
        self.paused = True
        mixer.music.pause()
        self.status_label.config(text="Music Paused")

    def stop_music(self):
        mixer.music.stop()
        self.status_label.config(text="Music Stopped")

    def set_volume(self, val):
        volume = int(val) / 100
        mixer.music.set_volume(volume)

    def mute_unmute(self):
        current_volume = mixer.music.get_volume()
        if current_volume > 0:
            self.previous_volume = current_volume
            mixer.music.set_volume(0)
            self.scale.set(0)
            self.status_label.config(text="Music Muted")
        else:
            mixer.music.set_volume(self.previous_volume)
            self.scale.set(self.previous_volume * 100)
            self.status_label.config(text="Music Unmuted")

    def update_duration(self):
        if mixer.music.get_busy():
            current_time = mixer.music.get_pos() / 1000
            remaining_time = self.song_length - current_time
            formatted_time = time.strftime('%M:%S', time.gmtime(remaining_time))
            self.status_label.config(text=f"Time Remaining: {formatted_time}")
            self.root.after(1000, self.update_duration)
        else:
            self.status_label.config(text="Music Stopped")

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()