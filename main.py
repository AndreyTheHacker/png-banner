import png
import os
import sys
end = "\x1b[0m"
br = 0
oldstyle=""
term = os.popen("stty size","r").read().split(" ")
if len(sys.argv)==4:
    normarg = sys.argv[-3]
    br = int(sys.argv[-2])
    oldstyle = sys.argv[-1]
elif len(sys.argv)==3:
    normarg = sys.argv[-2]
    br = int(sys.argv[-1])
elif len(sys.argv)==2:
    normarg = sys.argv[-1]
else:
    normarg = sys.argv[-1]
    if(not normarg.endswith('.png')):
        print("Error: No .png file selected")
        print("Usage: pngbanner image [brightness] [oldstyle]")
        exit()
rd = png.Reader(normarg)
width, height, data, other = rd.read_flat()
isalpha = other['alpha']
print("%sx%s"%(width,height))
pw = 4
x, y = (0,0)
trig = False
while y<height:
    x=0
    while x<width:
        p=data[(x+(y*width))*4:((x+(y*width))+1)*4] if isalpha==True else data[(x+(y*width))*3:((x+(y*width))+1)*3]
        #print(p)
        r,g,b=(p[0],p[1],p[2]) if len(p)>=3 else (0,0,0)
        draw = "\x1b[38;2;%s;%s;%sm"%(r+br if r+br>0 else 0,g+br if g+br>0 else 0,b+br if b+br>0 else 0)
        x+=1
        print("%s\u2588%s"%(draw,end),end='') if len(oldstyle)<=0 else print("%s#%s"%(draw,end),end='')
        
    print("")
    y+=1
 