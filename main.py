# what a mess!
# don't even consider reading this code
# I had to rush to complete this .
# it doesn't even work , just a few video can work with .
# and thank you pytube for this bad library .
# sorry cs50x for this bad project :(


from pytube import YouTube
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os
import threading

def download(*argc):
    cleanlink = link.get()    
    threading.Thread(target=performe_download,args=argc).start()

def performe_download(*argc):
    cleanlink = link.get()
    yt = YouTube(cleanlink)
    path = filedialog.askdirectory(title='Select Path')

    if argc[0] == "144p" or argc[0] == "360p" or argc[0] == "720p":
        stream = (yt.streams.filter(file_extension='mp4',res=argc[0],progressive=True)).first()
        path = stream.download(path)
        result_label.config(text=f"Video path: {path}")
        show_button(path)

    elif argc[0] == "mp3":
        audio_stream = (yt.streams.filter(file_extension='mp4', only_audio=True)).first()
        audio_path = audio_stream.download(path)
        result_label.config(text=f"Audio path: {audio_path}")
        show_button(audio_path)

    elif argc[0] == "1080p":
        video_stream = (yt.streams.filter(file_extension='mp4', res=argc[0], adaptive=True, only_video=True)).first()
        audio_stream = (yt.streams.filter(file_extension='mp4', adaptive=True, only_audio=True)).first()
        video_path = video_stream.download(output_path=path,filename_prefix="video_")
        audio_path = audio_stream.download(output_path=path,filename_prefix="audio_")
        result_label.config(text=f"Video path: {video_path} Audio path: {audio_path}")
        show_button(video_path)
        show_message()
    else:
        result_label.config(text="An error occured")

def is_valid_youtube_url(url):
    try:
        lol = YouTube(url)
        return True
    except Exception as e:
        print(Exception)
        return False

def update_progress(x):
    root.after(100, update_progress)
    result_label.config(text=x)



def mp4_144():
    resolution = "144p"
    download(resolution)
def mp4_360():
    resolution = "360p"
    download(resolution)
def mp4_720():
    resolution = "720p"
    download(resolution)
def mp4_1080():
    resolution = "1080p"
    download(resolution)
def mp3():
    file = "mp3"
    download(file)

def show_download_buttons():
    cleanlink = link.get()
    
    if not cleanlink:
        result_label.config(text="Error: Please enter a valid YouTube link to proceed.")
        return "Please enter a valid YouTube link to proceed."
    if not is_valid_youtube_url(cleanlink):
        result_label.config(text="Error: The URL does not appear to be a valid YouTube link. Please check it and try again.")
        return "Invalid Youtube url"

    yt = YouTube(cleanlink)
    
    download_144.grid_forget()
    download_360.grid_forget()
    download_720.grid_forget()
    download_1080.grid_forget()
   
    if yt.streams.filter(file_extension='mp4',res="144p",progressive=True).first():
        download_144.grid(row=3,column=1)
        mp4_exists = True    
    if yt.streams.filter(file_extension='mp4',res="360p",progressive=True).first():
        download_360.grid(row=3,column=2)
        mp4_exists = True
    if yt.streams.filter(file_extension='mp4',res="720p",progressive=True).first():
        download_720.grid(row=3,column=3)
        mp4_exists = True
    if yt.streams.filter(file_extension='mp4',res="1080p").first():
        download_1080.grid(row=3,column=4)
        mp4_exists = True
    if mp4_exists == True:
        Label(mainframe,text="mp4: ").grid(row=3,column=0)
    if yt:
        Label(mainframe,text="mp3: ").grid(row=4,column=0)
        ttk.Button(mainframe,text="Download mp3",command=mp3).grid(row=4,column=1, columnspan=4)
def show_button(x):
    ttk.Button(mainframe,text="Open Folder",command=lambda: open_folder(x)).grid(row=5,column=2)
    ttk.Button(mainframe,text="Open File",command=lambda: open_file(x)).grid(row=5,column=3)
    
def open_folder(x):
    path = os.path.dirname(x)
    os.startfile(path)

def open_file(x):
    os.startfile(x)

def show_message():
    instructions_text = (
        "Instructions:\n"
        "1. You have downloaded separate video and audio files.\n"
        "2. To combine them into a single file, use a video editor or merging software.\n"
        "3. Alternatively, you can use ffmpeg for merging if available.\n"
        "4. Example ffmpeg command: \n"
        "   ffmpeg -i path/to/video.mp4 -i path/to/audio.mp4 -c:v copy -c:a aac output.mp4"
    )
    messagebox.showinfo("Instuctions", instructions_text)

def show_message2():
    instructions_text = (
        "Instructions:\n"
        "1. Enter a valid Youtube link (e.g., https://www.youtube.com/example).\n"
        "2. Choose the preferred resolution.\n"
        "3. Select the preferred path for the file to be downloaded to.\n"

        "\nNOTE: For 1080p resolution, the program will download separate video and audio files. You will need to combine them into a single file using a video editor or merging software.\n"
        "\nSupport:\n- For assistance or to report issues, please don't contact me."
    )
    messagebox.showinfo("Instuctions", instructions_text)
def show_credits():
    credits_text = (
        "Credits:\n"
        "- Developed by @medo_atif\n"
        "- Uses pytube library (https://pytube.io)\n"
        "- Special thanks to Harvard University for offering the CS50x course\n"
        "- A heartfelt thank you to David Malan for his exceptional teaching throughout the course."  

    )
    messagebox.showinfo("Credits", credits_text)


root = Tk()

root.title("Youtube Downloader")
root.geometry("645x220")
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(row=0, column=0, sticky=(W,E,N,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)




download_144 = ttk.Button(mainframe,text="Download 144p",command=mp4_144)
download_360 = ttk.Button(mainframe,text="Download 360p",command=mp4_360)
download_720 = ttk.Button(mainframe,text="Download 720p",command=mp4_720)
download_1080 = ttk.Button(mainframe,text="Download 1080p",command=mp4_1080)

link = StringVar()

link_entry = ttk.Entry(mainframe, width=100, textvariable=link)
link_entry.grid(row=0,column=1,pady=5,columnspan=4)


icon = PhotoImage(file="icons/download.png")
ttk.Button(mainframe, image=icon,command=show_download_buttons).grid(row=0,column=5,sticky="W")



result_label = Label(mainframe, text="")
result_label.grid(row=5, column=1, columnspan=4)

icon2 = PhotoImage(file="icons/help.png")
button = ttk.Button(mainframe, image=icon2, command=show_message2).grid(row=8,column=4,sticky="ES")
icon3 = PhotoImage(file="icons/credit.png")
button = ttk.Button(mainframe, image=icon3, command=show_credits).grid(row=8,column=5,sticky="ES")


root.mainloop()
