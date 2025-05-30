from tkinter import *
import calendar
from tkinter import scrolledtext

def Calen():
    try:
        get_year = int(year_entry.get())

        # Create new window
        window = Toplevel()
        window.config(background="#efefef")
        window.title("Calendar")
        window.geometry("570x600")

        # Get calendar content
        window_content = calendar.calendar(get_year)

        # Use ScrolledText to display calendar
        year_cal = scrolledtext.ScrolledText(window, width=80, height=30, font=("Courier", 10))
        year_cal.insert(INSERT, window_content)
        year_cal.pack(padx=10, pady=10)
        year_cal.config(state='disabled')  # Make it read-only

    except ValueError:
        # Optional: add an error popup if input is invalid
        error_win = Toplevel()
        error_win.title("Error")
        Label(error_win, text="Please enter a valid year.", font=("Arial", 12), fg="red").pack(padx=20, pady=20)

if __name__ == '__main__':
    root = Tk()
    root.configure(background='#C4E1E6')
    root.title("Calendar")
    root.geometry("360x170")
    root.resizable(False, False)

    name = Label(root, text="Calendar", bg="#8DBCC7", font=("Arial", 20))
    name.grid(column=1, row=1, pady=(10, 5))

    year = Label(root, text="Enter the year", bg="#8DBCC7", font=("Arial", 14))
    year.grid(column=1, row=2)

    year_entry = Entry(root, bg="#FFFFFF", font=("Arial", 14))
    year_entry.grid(column=1, row=3)

    show_button = Button(root, text="Show Calendar", bg="#8DBCC7", font=("Arial", 12), command=Calen)
    show_button.grid(column=1, row=4, pady=10)

    root.mainloop()
