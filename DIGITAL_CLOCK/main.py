import tkinter as tk
from time import strftime

# main window
root = tk.Tk()
root.title("TIMENOW")
root.geometry("500x200")
root.resizable(False, False)

# create a canvas for background
canvas = tk.Canvas(root,width=500,height=200)
canvas.pack(fill=tk.BOTH,expand=True)


# draw vertical gradient on canvas
def draw_gradient(canvas, color1, color2, steps=100):
    r1, g1, b1 = root.winfo_rgb(color1)
    r2, g2, b2 = root.winfo_rgb(color2)

    r_ratio = (r2 - r1) / steps
    g_ratio = (g2 - g1) / steps
    b_ratio = (b2 - b1) / steps

    for i in range(steps):
        nr = int(r1 + (r_ratio * i)) // 256
        ng = int(g1 + (g_ratio * i)) // 256
        nb = int(b1 + (b_ratio * i)) // 256
        color = f'#{nr:02x}{ng:02x}{nb:02x}'
        canvas.create_rectangle(0, i * 2, 500, (i +1) * 2, outline=color, fill=color)

draw_gradient(canvas, '#d4d4d4','#b3b3b3') # dark blue to navy gradient

# add text to canvas
time_text =canvas.create_text(250,100,fill='#2b2b2b',font=('DS-Digital',50,'bold'),text='')

# update the clock
def time():
    string = strftime("%H:%M:%S %p\n%D")
    canvas.itemconfig(time_text, text=string)
    root.after(1000,time)


time()
root.mainloop()