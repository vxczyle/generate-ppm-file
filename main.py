import subprocess
import os
import random
import time
import argparse
import sys

W = 500
H = 500


parser = argparse.ArgumentParser(description= "1 = True, 0 = False.")
parser.add_argument("-p", help="Choose whether to open the app in Photos.exe", type=int, metavar="{0,1}")
parser.add_argument("-d", help="Deletes the PPM file", type=int, metavar="{0,1}")
parser.add_argument("-s", help="Starts the PPM file", type=int, metavar="{0,1}")
args = parser.parse_args(["-h"] if len(sys.argv) == 1 else None)

delppm = args.d
photos = args.p
startppm = args.s

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
    print("no")

