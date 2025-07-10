import tkinter as tk
from tkinter import  messagebox, filedialog, ttk
import  pyautogui
import datetime
import os
import threading
import time
from PIL import Image, ImageTk
import keyword
import  json

class ScreenshotTool:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Screenshot Tool")
        self.app.geometry("450x600")
        self.app.resizable(False, False)

        #settings
        self.settings = self.load_settings()
        self.save_dir = self.settings["save_dir", "Screenshots"]
        self.file_format = self.settings["file_format", "PNG"]
        self.hotkey_enabled = self.settings["hotkey_enabled", True]

        #creare save directory
        os.makedirs(self.save_dir, exist_ok=True)

        # Initialize GUI
        self.setup_gui()

        # setup global hotkey
        if self.hotkey_enabled:
            self.setup_hotkey()

        # Preview image reference
        self.preview_image = None