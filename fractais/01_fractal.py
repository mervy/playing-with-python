# https://www.youtube.com/watch?v=WpE2Sg6Lq3U
# https://drive.google.com/file/d/1s40R0TSxmX2gpwaL3oD5pckHO2qToq9J/view
import matplotlib.pyplot as plt
import numpy as np
from random import randint
#Variaveis inicais
X,Y=1000,1000
Z=np.array([[0]*X for y in range(Y)])
Z[-1]=[1]*X
limite=Y-2
#deposicao
while limite!=0:
    x=randint(1,X-2)
    y=limite
    while (Z[y][x+1],Z[y][x-1],Z[y+1][x])==(0,0,0):
        y+=1
    Z[y][x]=Y-y
    if limite==y:
        limite=y-1
#grafico
Z = np.ma.masked_where(Z < 1, Z)

cmap = plt.cm.Accent
cmap.set_bad(color='black')
plt.matshow(Z,cmap=cmap)
plt.show()

