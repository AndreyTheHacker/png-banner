import png
import os
import sys
from time import sleep
end = "\x1b[0m" # end draw command

term = os.popen("stty size","r").read().split(" ") # unused
if(not sys.argv[-1].endswith('.png')):
    print("Error: No .png file selected")
    exit()
rd = png.Reader(sys.argv[-1])
width, height, data, other = rd.read_flat()
print("%sx%s"%(width,height))
pw = 4
x, y = (0,0)
while y<height:
    x=0
    while x<width:
        p=data[(x+(y*width))*4:((x+(y*width))+1)*4]
        r,g,b=(p[0],p[1],p[2])
        draw = "\x1b[38;2;%s;%s;%sm"%(r,g,b)
        print("%s#%s"%(draw,end),end='')
        x+=1
    print("")
    y+=1

# It really works!