import random,sys

import pygame
from pygame.locals import *
import math, random

pygame.init()

screensize=(600,400)
screen = pygame.display.set_mode(screensize)
pygame.display.set_caption('Eeeny Meeny')

bg=(0,0,0)
fg=(0,200,80)
fontobject = pygame.font.Font(None,34)
smallfontobject = pygame.font.Font(None,14)

end=False

clock=pygame.time.Clock()

colours=[(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255)]


def distance(a,b):
    if len(a)!=len(b):
        raise Exception("Items must have same numebr of components")
    value=0
    for i in range(len(a)):
        value+=(a[i]-b[i])**2
    return value**0.5


def assign(means,data):
    classes=[]

    for i in range(len(means)):
        classes.append([])

    for i in data:
        nearest=0
        for j in range(len(means)):
            if distance(i,means[j]) < distance(i,means[nearest]):
                nearest=j
        classes[nearest].append(i)
    return classes

    
def getMeans(classes):
    means=[]
    for i in range(len(classes)):
        tempx,tempy=0,0
        if len(classes[i])>0:
            for j in classes[i]:
                tempx+=j[0]
                tempy+=j[1]
            means.append((tempx/len(classes[i]),tempy/len(classes[i])))
        else:
            means.append((0,0))
    return means




#Number of means is defined by how many we give at the start
data=[]
for i in range(100):
    newItem=(random.randint(0,screensize[0]),random.randint(0,screensize[1]))
    data.append(newItem)

#Arbitrary starting points
means=[(0,0),(50,50),(100,100), (200,200),(300,300)]
    
while not end:
    


    for event in pygame.event.get(): 
        if event.type == QUIT:
            end=True
        elif event.type == KEYDOWN:
            if event.key == K_q:
                end=True




    clock.tick(2)
    screen.fill(bg)


    #Calculate new class membership
    classes=assign(means,data)
        
    #Draw the means
    for i in range(len(classes)):
        pygame.draw.rect(screen,colours[i],pygame.Rect(means[i][0]-10,means[i][1]-10,20,20),0)

    #Draw the points    
    for i in range(len(classes)):           
        marker=smallfontobject.render("%d"%i,1, colours[i])
        for j in classes[i]:
            screen.blit(marker,j)


                
    #Update the means
    means=getMeans(classes)

        

    screen.blit(fontobject.render("Press Q to quit", 1, fg),(0,0))
    pygame.display.flip()
