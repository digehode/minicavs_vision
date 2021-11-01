#!/bin/env python
import sys,math
from PIL import Image, ImageFilter

acc_size=150
scale=20.0

edge_threshold=100
acc_threshold=30




acc={}
cs=[]

def drawline(mc,im):
    for x in range(im.size[0]):
        y=mc[0]*x+mc[1]*scale
        if y>0 and y<im.size[1]:
            im.putpixel((x,y),255)

def add_to_acc(x,y):
    for m in range(-acc_size,acc_size):        
        c=((-x)*m+y)/scale
        #cs.append(c)
        #print m,c
        if not math.fabs(c)>acc_size:
            
            if acc.has_key((m,c)):
                acc[(m,c)]+=1
            else:
                acc[(m,c)]=1

def threshold(val,thresh):
    if val<thresh:
        return 0
    else:
        return 255

if len(sys.argv)!=2:
    print("Usage: "+sys.argv[0]+" image")
    sys.exit()

image_file=sys.argv[1]

image=Image.open(image_file).convert("L")

image.show()

image=image.filter(ImageFilter.BLUR)


im2=image.point(lambda v: threshold(v,edge_threshold))
im2.show()
im2=im2.filter(ImageFilter.FIND_EDGES)
im2.show()


data=im2.getdata()
pos=0
for y in range(im2.size[1]):
    #print y,"/",im2.size[1]
    for x in range(im2.size[0]):
        if data[pos]>128:
            add_to_acc(x,y)
        pos+=1
#print pos,len(data)
            
acc_image=Image.new("L",(acc_size*2,acc_size*2))
keys=acc.keys()
keys.sort()
for k in keys:
    x=k[0]
    y=k[1]
    x+=acc_size
    y+=acc_size
    #print x,y
    try:
        acc_image.putpixel((x,y),acc[k]*100)
    except:
        pass #print "busted",x,y
print()
acc_image.show()

out_im=Image.new("L",image.size)

thresh=acc_threshold

for k in keys:
    if acc[k]>thresh:
        drawline(k,out_im)
out_im.show()
