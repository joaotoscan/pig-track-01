import matplotlib.pyplot as plt
import numpy as np

def diferenca(mx,mpx): #diferenca de um frame em comparacao com o anterior
    for l in range(0,len(mx)):
        if l == 0:
            mpx.append(0)
            continue
        if mx[l] < mx[l-1]:
            mpx.append(int(mx[l-1]) - int(mx[l]))
        elif mx[l] > mx[l-1]:
            mpx.append(int(mx[l]) - int(mx[l-1]))
        else:
            mpx.append(0)
    return mpx

def ajeito(lista):
    while len(lista)%6 > 0:
        lista.append(0)
    return(lista)

def somar(lista,frame):
    lista2 = []
    for l in range(0,len(lista),6):
        i = l
        total = 0

        print(l)
        try:
            while i<l+6:
                total = total + lista[i]
                i=i+1
        except:
            break

        lista2.append(total)

    return(lista2)
#arquivo txt
px = [] #lista das coordenadas x e y
py = []
arquivo = open('posicao_porco.txt','r')
for line in arquivo:
    line = line.strip()
    Xo,Yo=line.split(',')
    px.append(Xo)
    py.append(Yo)

arquivo.close
#transformar px em m
mx = [] #lista das coordenadas x e y em metros
my = []
taxa = 1 #1px = ?cm
for l in px:
    mx.append(l*taxa)
for l in py:
    my.append(l*taxa)

#ver m por minuto
mpx = [] #lista da movimentacao x e y a cada segundo
mpy = []
frame = 6 #frames por segundo
mpx = diferenca(mx,mpx)
mpy = diferenca(my,mpy)
mpx = ajeito(mpx)
mpy = ajeito(mpy)
mpx = (somar(mpx,frame))
mpy = (somar(mpy,frame))
mt = []
mtc =[]
for l in range(1,len(mpx)):
    mt.append( (mpx[l-1]**2 + mpy[l-1]**2)**0.5)
    mtc.append(l)
    l = l + 1

#grafico
y = mt
x = mtc

plt.plot(x,y)
plt.title('Movimentacao do pig')
plt.xlabel('Segundos')
plt.ylabel('Centimetros')
plt.grid(True)
plt.savefig("test.png")
plt.show()
