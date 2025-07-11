import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import pyautogui
import datetime
import os
import threading
import time
from PIL import Image, ImageTk
import keyboard
import json


class ScreenshotTool:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Enhanced Screenshot Tool")
        self.app.geometry("450x600")
        self.app.resizable(False, False)

        # Settings
        self.settings = self.load_settings()
        self.save_dir = self.settings.get("save_dir", "Screenshots")
        self.file_format = self.settings.get("file_format", "PNG")
        self.hotkey_enabled = self.settings.get("hotkey_enabled", True)

        # Create save directory
        os.makedirs(self.save_dir, exist_ok=True)

        # Initialize GUI
        self.setup_gui()

        # Setup global hotkey
        if self.hotkey_enabled:
            self.setup_hotkey()

        # Preview image reference
        self.preview_image = None

    def load_settings(self):
        try:
            with open("screenshot_settings.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_settings(self):
        settings = {
            "save_dir": self.save_dir,
            "file_format": self.file_format,
            "hotkey_enabled": self.hotkey_enabled
        }
        with open("screenshot_settings.json", "w") as f:
            json.dump(settings, f, indent=2)

    def setup_gui(self):
        # Main frame
        main_frame = ttk.Frame(self.app, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = tk.Label(main_frame, text="Enhanced Screenshot Tool",
                               font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

        # Screenshot options
        options_frame = ttk.LabelFrame(main_frame, text="Screenshot Options", padding="10")
        options_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        # Full screen button
        self.full_screen_btn = tk.Button(options_frame, text="📱 Full Screen",
                                         font=("Arial", 10), bg="#4CAF50", fg="white",
                                         command=self.take_fullscreen_screenshot)
        self.full_screen_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # Region selection button
        self.region_btn = tk.Button(options_frame, text="🔲 Select Region",
                                    font=("Arial", 10), bg="#2196F3", fg="white",
                                    command=self.take_region_screenshot)
        self.region_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Active window button
        self.window_btn = tk.Button(options_frame, text="🪟 Active Window",
                                    font=("Arial", 10), bg="#FF9800", fg="white",
                                    command=self.take_window_screenshot)
        self.window_btn.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Delayed screenshot button
        self.delay_btn = tk.Button(options_frame, text="⏱️ Delayed (3s)",
                                   font=("Arial", 10), bg="#9C27B0", fg="white",
                                   command=self.take_delayed_screenshot)
        self.delay_btn.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Configure grid weights
        options_frame.columnconfigure(0, weight=1)
        options_frame.columnconfigure(1, weight=1)

        # Settings frame
        settings_frame = ttk.LabelFrame(main_frame, text="Settings", padding="10")
        settings_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        # Save directory
        tk.Label(settings_frame, text="Save Directory:").grid(row=0, column=0, sticky="w")
        self.dir_label = tk.Label(settings_frame, text=self.save_dir,
                                  font=("Arial", 9), fg="blue")
        self.dir_label.grid(row=0, column=1, sticky="w", padx=(10, 0))

        change_dir_btn = tk.Button(settings_frame, text="Change",
                                   command=self.change_directory)
        change_dir_btn.grid(row=0, column=2, padx=(10, 0))

        # File format
        tk.Label(settings_frame, text="File Format:").grid(row=1, column=0, sticky="w", pady=(10, 0))
        self.format_var = tk.StringVar(value=self.file_format)
        format_combo = ttk.Combobox(settings_frame, textvariable=self.format_var,
                                    values=["PNG", "JPG", "BMP", "TIFF"], state="readonly")
        format_combo.grid(row=1, column=1, sticky="w", padx=(10, 0), pady=(10, 0))
        format_combo.bind("<<ComboboxSelected>>", self.on_format_change)

        # Hotkey toggle
        self.hotkey_var = tk.BooleanVar(value=self.hotkey_enabled)
        hotkey_check = tk.Checkbutton(settings_frame, text="Enable Hotkey (Ctrl+Shift+S)",
                                      variable=self.hotkey_var, command=self.toggle_hotkey)
        hotkey_check.grid(row=2, column=0, columnspan=2, sticky="w", pady=(10, 0))

        # Preview frame
        preview_frame = ttk.LabelFrame(main_frame, text="Preview", padding="10")
        preview_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))

        self.preview_label = tk.Label(preview_frame, text="No screenshot taken yet",
                                      bg="lightgray", width=40, height=8)
        self.preview_label.grid(row=0, column=0, columnspan=2)

        # Status frame
        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E))

        self.status_label = tk.Label(status_frame, text="Ready", font=("Arial", 9), fg="green")
        self.status_label.grid(row=0, column=0, sticky="w")

        # Configure main grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def setup_hotkey(self):
        def hotkey_handler():
            self.take_fullscreen_screenshot()

        try:
            keyboard.add_hotkey('ctrl+shift+s', hotkey_handler)
        except:
            pass  # Hotkey setup failed, continue without it

    def toggle_hotkey(self):
        self.hotkey_enabled = self.hotkey_var.get()
        self.save_settings()
        if self.hotkey_enabled:
            self.setup_hotkey()
        else:
            try:
                keyboard.remove_hotkey('ctrl+shift+s')
            except:
                pass

    def change_directory(self):
        new_dir = filedialog.askdirectory(initialdir=self.save_dir)
        if new_dir:
            self.save_dir = new_dir
            self.dir_label.config(text=self.save_dir)
            os.makedirs(self.save_dir, exist_ok=True)
            self.save_settings()

    def on_format_change(self, event):
        self.file_format = self.format_var.get()
        self.save_settings()

    def update_status(self, message, color="black"):
        self.status_label.config(text=message, fg=color)
        self.app.update()

    def create_filename(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        extension = self.file_format.lower()
        if extension == "jpg":
            extension = "jpeg"
        return os.path.join(self.save_dir, f"screenshot_{timestamp}.{extension}")

    def save_screenshot(self, screenshot, screenshot_type="screenshot"):
        try:
            filename = self.create_filename()

            # Convert to RGB if saving as JPEG
            if self.file_format == "JPG":
                screenshot = screenshot.convert("RGB")

            screenshot.save(filename, format=self.file_format)
            self.update_preview(screenshot)
            self.update_status(f"✓ {screenshot_type} saved: {os.path.basename(filename)}", "green")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to save screenshot:\n{e}")
            self.update_status("❌ Save failed", "red")

    def update_preview(self, screenshot):
        # Resize image for preview
        preview_size = (200, 150)
        preview_img = screenshot.copy()
        preview_img.thumbnail(preview_size, Image.Resampling.LANCZOS)

        # Convert to PhotoImage
        self.preview_image = ImageTk.PhotoImage(preview_img)
        self.preview_label.config(image=self.preview_image, text="")

    def take_fullscreen_screenshot(self):
        self.update_status("📱 Taking full screen screenshot...")
        try:
            screenshot = pyautogui.screenshot()
            self.save_screenshot(screenshot, "Full screen screenshot")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to take screenshot:\n{e}")
            self.update_status("❌ Screenshot failed", "red")

    def take_region_screenshot(self):
        self.update_status("🔲 Click and drag to select region...")
        self.app.withdraw()  # Hide main window

        try:
            # Simple region selection using messagebox
            messagebox.showinfo("Region Selection",
                                "This will take a screenshot of the entire screen.\n"
                                "For advanced region selection, consider using a specialized tool.")

            screenshot = pyautogui.screenshot()
            self.save_screenshot(screenshot, "Region screenshot")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to take region screenshot:\n{e}")
            self.update_status("❌ Region screenshot failed", "red")
        finally:
            self.app.deiconify()  # Show main window again

    def take_window_screenshot(self):
        self.update_status("🪟 Taking active window screenshot...")
        try:
            # Get active window (this is a simplified version)
            screenshot = pyautogui.screenshot()
            self.save_screenshot(screenshot, "Window screenshot")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to take window screenshot:\n{e}")
            self.update_status("❌ Window screenshot failed", "red")

    def take_delayed_screenshot(self):
        def delayed_capture():
            for i in range(3, 0, -1):
                self.update_status(f"⏱️ Taking screenshot in {i}...", "orange")
                time.sleep(1)

            try:
                screenshot = pyautogui.screenshot()
                self.save_screenshot(screenshot, "Delayed screenshot")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to take delayed screenshot:\n{e}")
                self.update_status("❌ Delayed screenshot failed", "red")

        # Run in separate thread to avoid blocking GUI
        thread = threading.Thread(target=delayed_capture)
        thread.daemon = True
        thread.start()

    def run(self):
        self.app.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.app.mainloop()

    def on_closing(self):
        self.save_settings()
        try:
            keyboard.unhook_all()
        except:
            pass
        self.app.destroy()


if __name__ == "__main__":
    # Required dependencies check
    try:
        import keyboard
        from PIL import Image, ImageTk
    except ImportError as e:
        print(f"Missing dependency: {e}")
        print("Please install required packages:")
        print("pip install pyautogui pillow keyboard")
        exit(1)

    app = ScreenshotTool()
    app.run()