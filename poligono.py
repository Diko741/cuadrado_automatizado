import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle 
from PIL import Image

plt.imshow(Image.open('fondo.png'))

def DDA(x1, y1, x2, y2):
    x1r=x1; y1r=y1
    x2r=x2; y2r=y2
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    x3=x1
    y3=y1+dx
    if(dx>dy):
        steps=dx
    else:
        steps=dy
    xinc=float(dx/steps)    
    yinc=float(dy/steps)    
    xinc=round(xinc, 1)
    yinc=round(yinc, 1)

    dx1= abs(x3-x1)
    dy1= abs(y3-y1)
    if(dx1>dy1):
        steps=dx1
    else:
        steps=dy1
    xinc1=float(dx1/steps)
    yinc1=float(dy1/steps)
    xinc1=round(xinc1, 1)
    yinc1=round(yinc1, 1)

    for i in range (0, int (steps+1)) :
        plt.gca().add_patch(Rectangle((x1, y1), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.gca().add_patch(Rectangle((x3, y3), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.gca().add_patch(Rectangle((x1r, y1r), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.gca().add_patch(Rectangle((x2r, y2r), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.ylim(0, 25)
        x1=(x1+xinc); y1=(y1+yinc)
        x3=(x3+xinc); y3=(y3+yinc)
        x1r=(x1r+xinc1); y1r=(y1r+yinc1)
        x2r=(x2r+xinc1); y2r=(y2r+yinc1)
        print ("("+str(round(x1))+", "+str(round(y1))+")")
        print ("("+str(round(x3))+", "+str(round(y3))+")")
        print ("("+str(round(x1r))+", "+str(round(y1r))+")")
        print ("("+str(round(x2r))+", "+str(round(y2r))+")") 

    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.title('*** DDA ***')
    plt.show()

def Bresenham(x1, y1, x2, y2):
    x=x1; y=y1; xr=x1; yr=y1
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    p=2*dy-dx
    x3=x1; y3=y1+dx

    while (x<=x2) or (yr<=y3):
        plt.gca().add_patch(Rectangle((x, y), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.gca().add_patch(Rectangle((x3, y3), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.gca().add_patch(Rectangle((xr, yr), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.gca().add_patch(Rectangle((x2, y2), 1, 1, linewidth=1, edgecolor='m', facecolor='none'))
        plt.ylim(0, 25)
        x+=1; x3+=1
        yr+=1; y2+=1
        if (p<0):
            p=p+2*dy
        else:
            p=p+(2*dy)-(2*dx)
            y+=1; y3+=1
            xr+=1; x2+=1

        print ("("+str(round(x))+", "+str(round(y))+")")

    plt.xlabel('Eje x')
    plt.ylabel('Eje y')
    plt.title('*** Bresenhams ***')
    plt.show()

if __name__=="__main__":
    #solicitar los valores que son asignados a las variables de inicalización 
    tipo=int(input("\033[1;33m"+"Ingrese el valor del algoritmo a usar:\n1. Algoritmo DDA\n2. Algoritmo Bresenham\n"+'\033[0;m')) 
    x1=1
    y1 = 1
    x2 = int(input("\033[;36m"+"Ingrese la Longitud="+'\033[0;m'))     
    y2=y1

    if (tipo==1):
        DDA(x1, y1, ((x2+x1)-1), y2)
    elif (tipo==2):
        Bresenham(x1, y1, ((x2+x1)-1), y2)
