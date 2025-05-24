# step-1 import required libraries
import tkinter as tk
from PIL import Image,ImageTk
import random

# step-2 create root window
root = tk.Tk()
root.geometry("500x360")
root.title("ROLL THE DICE")
root.resizable(width=False, height=False)

# step-3 List of dice image path
dice = ["images/dice_1.png", "images/dice_2.png", "images/dice_3.png",
        "images/dice_4.png", "images/dice_5.png", "images/dice_6.png"]

# steo-4 load inital images
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((100, 100), Image.Resampling.LANCZOS))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((100, 100), Image.Resampling.LANCZOS))



# step-5 creates labels and place them
label1 = tk.Label(root, image=image1)
label1.image = image1
label1.place(x=50, y=100)

label2 = tk.Label(root, image=image2)
label2.image = image2
label2.place(x=300,y=100)

# step-6 function to update dice images
def roll_dice():
    new_image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((100, 100), Image.Resampling.LANCZOS))
    new_image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)).resize((100, 100), Image.Resampling.LANCZOS))

    label1.configure(image=new_image1)
    label1.image = new_image1

    label2.configure(image=new_image2)
    label2.image = new_image2

# step-7 button to roll the dice
button = tk.Button(root, text="ROLL THE DICE", command=roll_dice,fg="orange", bg="black")
button.pack(pady=20)

root.mainloop()