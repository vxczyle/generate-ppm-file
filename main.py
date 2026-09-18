import subprocess
import os
import random
import time
import argparse
import sys


parser = argparse.ArgumentParser(description= "1 = True, 0 = False. THE DEFAULT WIDTH HEIGHT IS UH UHHH 500X500 JSYK OKAY BUHBYE")
parser.add_argument("-p", help="Choose whether to open the app in Photos.exe", type=int, metavar="{0,1}")
parser.add_argument("-d", help="Deletes the PPM file", type=int, metavar="{0,1}")
# For this part to actually work you need a image viewer that's set to view PPM files by default :)
parser.add_argument("-s", help="Opens the PPM file", type=int, metavar="{0,1}")
parser.add_argument("-w", "--width", help="Sets the width of the image", type=int, metavar="number")
parser.add_argument("-t", "--height", help="Sets the height of the image", type=int, metavar="number")
args = parser.parse_args(["-h"] if len(sys.argv) == 1 else None)

delppm = args.d
photos = args.p
startppm = args.s

W = args.width
H = args.height
print("the t instead of -h in height stands for tall btw HHAHAHHAAHAAHA ahem")

with open('example.ppm', 'w') as fisk:
    fisk.write("P3\n")
    fisk.write(f"{W} {H}\n")
    fisk.write("255\n")

    for y in range(H):
        for x in range(W):
            fisk.write(f"{random.randint(1, 255)} {random.randint(1, 255)} {random.randint(1, 255)} ")
        fisk.write("\n")
        
subprocess.run("magick example.ppm output.png", capture_output=False)
time.sleep(0.2)
if photos == 1 and delppm == 1:
    os.remove("example.ppm")
elif photos == 1 and delppm == None:
    os.startfile("output.png")
elif photos == None and startppm ==1 and delppm == None:
    os.startfile("example.ppm")
elif photos == None and delppm == 1:
    os.remove("example.ppm")
    print("..why?? nothing is going to open!")
elif photos == 1 and startppm == 1 and delppm == 1:
    print("no.")
    time.sleep(5)
elif delppm == 1 and startppm == None and photos == None:
    print("genuinely what are you doing? like bro WHY or i mean the output.png still exists but WHY")
    time.sleep(5)

