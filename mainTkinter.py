import subprocess
from tkinter import * 
from PIL import Image, ImageTk
import os
import random

W = 500
H = 500

with open('example.ppm', 'w') as fisk:
    fisk.write("P3\n")
    fisk.write(f"{W} {H}\n")
    fisk.write("255\n")

    for y in range(H):
        for x in range(W):
            fisk.write(f"{random.randint(1, 255)} {random.randint(1, 255)} {random.randint(1, 255)} ")
        fisk.write("\n")
        
subprocess.run("magick example.ppm output.png", capture_output=False)
os.remove("example.ppm")

root = Tk()
root.title("Randomly Generated Noise")
root.geometry = (f"{W}x{H}")

img = Image.open("output.png")
img = ImageTk.PhotoImage(img)
root.iconphoto(False, img)

label = Label(root, image=img)
label.pack()

root.mainloop()