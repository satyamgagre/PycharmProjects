import os
import threading
from tkinter import *
from tkinter import ttk, messagebox
from pytube import YouTube
import moviepy
# from  moviepy.editor import *

# --- Functions ---

# Fetch available video resolutions and enable download buttons
def fetch_screen():
    url = url_var.get()
    if not url.strip():
        messagebox.showerror("Error", "Please enter a Youtube URL.")
        return
    try:
        # Create Youtube object
        yt = YouTube(url)

        # Get all progressive strams (video + audio) in MP4 format
        strams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()

        # Get only audio streams (for audio download)
        audio_streams = yt.streams.get_audio_only()

        # Extract available resolutions for dropdown menu
        resolutions = [stream.resolution for stream in streams]
        res_combo['values'] = resolutions

        #Select the first resolution by default
        if resolutions:
            res_combo.current(0)

        #Enable download buttons
        download_btn.config(state=NORMAL)
        audio_btn.config(state=NORMAL)

        # Update status
        status_var.set("Ready to download.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch video info: {e}")

# Download the selected video resolution
def download_video():
    def task():
        try:
            status_var.set("Downloading video...")
            yt = YouTube(url_var.get())

            # Get selected resolution stream
            stream = yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution(res_var.get())

            # Download to 'downloads' folder
            stream.download(output_path="downloads")
            status_var.set("Video downloaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Video download failed: {e}")
            status_var.set("Download failed.")

    # `Run download in separate thread to avoid GUI freezing
    threading.Thread(target=task).start()

# Download audio as MP3
def download_audio():
    def task():
        try:
            status_var.set("Downloading audio...")
            yt = YouTube(url_var.get())

            # Get the first available audio stram
            audio_stram = yt.streams.filter(only_audio=True).first()

            # Download as .MP4 audio
            out_file = audio_stram.download(output_path="downloads")

            # convert .MP4 to .MP3 using moviepy
            mp3_file = out_file.replace(".mp4", ".mp3")
            clip = AudioFileClip(out_file)
            clip.write_audiofile(mp3_file)
            clip.close()

            # Remove the temporary .mp4 audio file
            os.remove(out_file)
            status_var.set("Audio downloaded as MP3!")
        except Exception as e:
            messagebox.showerror("Error", f"Audio download failed: {e}")
            status_var.get("Download failed.")

    #Run audio download in separate thread
    threading.Thread(target=task).start()

#GUI setup

# Create main application window
app = Tk()
app.title("Youtube Video Downloader")
app.geometry("500x300")
app.resizable(False, False)

# Youtube URL input
url_var = StringVar()
label = ttk.Label(app, text="Enter YouTube URL:").pack(pady=(10, 0))
Entry(app, textvariable=url_var, width=60).pack(pady=5)

# Button to fetch video info (resolutions)
Button(app, text="Fetch Video Info", command=fetch_streams).pack()

# Dropdown to select video resolution
res_var = StringVar()
Label(app, text="Select Resolution:").pack(pady=(10, 0))
res_combo = ttk.Combobox(app, textvariable=res_var, state="readonly", width=20)
res_combo.pack()

# Button to download video
download_btn = Button(app, text="Download Video", state=DISABLED, command=download_video)
download_btn.pack(pady=(10, 5))

# Button to download audio as MP3
audio_btn = Button(app, text="Download Audio (MP3)", state=DISABLED, command=download_audio)
audio_btn.pack()

# Status label to display messages
status_var = StringVar()
status_label = Label(app, textvariable=status_var, fg="blue")
status_label.pack(pady=10)

# Inform user about download location
Label(app, text="Downloads will be saved in the 'downloads' folder.").pack(side=BOTTOM, pady=10)

# Start the GUI event loop
app.mainloop()