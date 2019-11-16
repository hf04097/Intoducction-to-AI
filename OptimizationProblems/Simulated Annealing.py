import random
import math
#import matplotlib.pyplot as plt 

    
def stimulatedAnhealing(func,rangef,find):
    c = (random.uniform(rangef[0],rangef[1])),random.uniform(rangef[2],rangef[3])
    Tmax = 100
    Tmin = 1
    Talpha = 0.99
    step = 0.1
    n = [0]
    output = []
    
    while (Tmax > Tmin):    #till it reaches min temp
        Tmax = Tmax * Talpha
        neighbourList =[(c[0]+step,c[1]),(c[0],c[1]+step),(c[0],c[1]-step),(c[0]-step,c[1])]    #list of neighbours
        neighbour = neighbourList[random.randint(0,len(neighbourList)-1)]   #choosing a neighbour
    
        while not( (rangef[0] <= neighbour[0] <= rangef[1]) and (rangef[2] <= neighbour[1] <= rangef[3])):
            neighbour = neighbourList[random.randint(0,len(neighbourList)-1)]
            
        deltaF = func(neighbour[0],neighbour[1])  - func(c[0],c[1])
        if (find ==0):
            if (deltaF > 0):
                c = neighbour
            elif ((math.exp( deltaF / Tmax))*100 > random.randint(0,100)):    #checking probaility for max
                    c = neighbour
        elif (find ==1):
            if (deltaF < 0):
                c = neighbour
            elif ((math.exp( -deltaF / Tmax))*100 > random.randint(0,100)):    #checking probaility for min
                c = neighbour
    return c

def f(x,y):
    return x**2+y**2
print(stimulatedAnhealing(f,(-5,5,-5,5),0)) #find 0 for max
##plt.plot(x1, y1, label = "x**2+y**2 max") 
print(stimulatedAnhealing(f,(-5,5,-5,5),1)) #find 1 for min
##plt.plot(x1, y1, label = "x**2+y**2 min") 


def f(x,y):
    return 100* (x**2-y**2)+(1-x)**2
print(stimulatedAnhealing(f,(-2,2,-1,3),0)) #find 0 for max
print(stimulatedAnhealing(f,(-2,2,-1,3),1)) #find 1 for min


def f(x,y):
    return ((x**2 + y**2)/4000)- math.cos(x)*math.cos(y/math.sqrt(2))+1
print(stimulatedAnhealing(f,(-1,1,-1,1),0)) #find 0 for max
print(stimulatedAnhealing(f,(-1,1,-1,1),1)) #find 1 for min



