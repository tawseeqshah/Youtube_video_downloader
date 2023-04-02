from tkinter import *
from tkinter import font
from tkinter.ttk import Progressbar
import threading
from pytube import YouTube

def download_video(url, resolution, progress_bar):
    itag = choose_resolution(resolution)
    video = YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    progress_bar.stop()
    progress_bar['value'] = 0
    return stream.default_filename

def video_download(url, resolution, progress_bar):
    download_thread = threading.Thread(target=download_video, args=(url, resolution, progress_bar))
    download_thread.start()

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    elif resolution in ["medium", "720", "720p", "hd"]:
        itag = 22
    elif resolution in ["high", "1080", "1080p", "fullhd", "full_hd", "full hd"]:
        itag = 137
    elif resolution in ["very high", "2160", "2160p", "4K", "4k"]:
        itag = 313
    else:
        itag = 18
    return itag

window = Tk()
window.geometry("600x400")
window.config(bg="grey")
window.title("YouTube Video Downloader")

font_style = font.Font(family="Helvetica", size=16)

Label(window, text="YouTube Video Downloader", font=("Helvetica", 28, "bold"), bg="grey", fg="white").pack(padx=5, pady=20)
Label(window, text="Enter the YouTube video link:", font=font_style, bg="grey", fg="white").pack(padx=5, pady=10)

video_link = StringVar()

entry_link = Entry(window, width=50, font=font_style, textvariable=video_link)
entry_link.pack(padx=5, pady=10)

Label(window, text="Select the video resolution:", font=font_style, bg="grey", fg="white").pack(padx=5, pady=10)

resolution_options = ["360", "360p", "medium", "720", "720p", "hd", "high", "1080", "1080p", "fullhd", "full_hd", "full hd", "very high", "2160", "2160p", "4K", "4k"]

resolution_choice = StringVar()
resolution_choice.set(resolution_options[0])

option_menu = OptionMenu(window, resolution_choice, *resolution_options)
option_menu.config(font=font_style, bg="white", width=15)
option_menu.pack(padx=5, pady=10)

progress = DoubleVar()
progress.set(0)

progress_bar = Progressbar(window, orient=HORIZONTAL, length=300, mode='determinate', variable=progress)
progress_bar.pack(padx=5, pady=10)

def start_download():
    progress_bar.start(10)
    video_download(video_link.get(), resolution_choice.get(), progress_bar)

Button(window, text="Download", font=font_style, bg="blue", fg="white", command=start_download).pack(padx=5, pady=10)

window.mainloop()
