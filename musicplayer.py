import pygame
from tkinter import *
from tkinter import filedialog
pygame.init()
class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")
        pygame.mixer.init()
        self.playlist = Listbox(self.root, bg="black", fg="white", selectbackground="green", selectmode=SINGLE)
        self.playlist.pack(fill=BOTH, expand=True)
        self.play_button = Button(self.root, text="Play", command=self.play)
        self.stop_button = Button(self.root, text="Stop", command=self.stop)
        self.pause_button = Button(self.root, text="Pause", command=self.pause)
        self.resume_button = Button(self.root, text="Resume", command=self.resume)
        self.add_button = Button(self.root, text="Add Song", command=self.add_song)
        self.play_button.pack()
        self.stop_button.pack()
        self.pause_button.pack()
        self.resume_button.pack()
        self.add_button.pack()
    def add_song(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            pygame.mixer.music.queue(file_path)
            self.playlist.insert(END, file_path)
    def play(self):
        selected_song = self.playlist.get(ACTIVE)
        if selected_song:
            pygame.mixer.music.load(selected_song)
            pygame.mixer.music.play()
    def stop(self):
        pygame.mixer.music.stop()
    def pause(self):
        pygame.mixer.music.pause()
    def resume(self):
        pygame.mixer.music.unpause()
root = Tk()
music_player = MusicPlayer(root)
root.mainloop()