import tkinter
from tkinter.messagebox import showinfo

import windnd
from moviepy.editor import *


def mp4_to_mp3(mp4, mp3):
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close()
    # function call mp4_to_mp3("my_mp4_path.mp4", "audio.mp3")
    # os.remove(mp4)


def drag(files):
    msg = "\n".join((item.decode("gbk") for item in files))
    # showinfo(msg)
    print(msg)
    mp4_to_mp3(msg, msg[:-3] + "mp3")


if __name__ == "__main__":
    tk = tkinter.Tk()
    windnd.hook_dropfiles(tk, func=drag)
    tk.mainloop()
    mp4_to_mp3()
