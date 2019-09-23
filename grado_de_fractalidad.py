# Este programa realiza el conteo de palabras por caja de longitud s para el calculo del 
# grado de fractalidad. (Texto sin acentos)
from math import *
import string
import random
import operator

def cargar_datos(filename):

    f=open("capitulo_1.txt", "r")
    #texto='la vida es como una caja de chocolates nunca se sabe lo que te tocara'
    #texto='te quiero porque me quieres quieres que te quiera mas te quiero mas que me quieres que mas quieres que te quiera'
    texto=f.read()
    #Pasar a minusculas
    texto=texto.lower()
    #Eliminar puntuacion
    texto=texto.translate(str.maketrans('', '', string.punctuation))
    #Separar en palabras el texto
    palabras=texto.split()
    #Definir el numero total de palabras
    N=len(palabras)
    return palabras

#Es necesario crear una lista de las palabras que contiene el texto, sin que se repitan.
def fractalidad(palabras):
    voc=[]                                             #la variable voc contendra cada palabra que aparecen en el texto
    for p in palabras:
        if(p not in voc):
            voc.append(p)

    #Es necesario crear una lista que contenga las mismas palabras del texto original pero en orden aleatorio
    palabras_sh=palabras[:]
    random.shuffle(palabras_sh)
    #print('**************************************************')
    #print('Lista de palabras en el texto')
    #print(palabras)
    #print('**************************************************')
    gf={}

    for p in voc:                                 #Recorre el vocabulario, palabra por palabra
        dfw=0.0
        dfwm=0.0
        M=palabras.count(p)
        for s in range(1,N+1):                          #Define el tamanio de la caja
            noc=0                                       #Frecuencia de la palabra actual
            nocsh=0
    # Ahora hay que determinar la condicion de paro para el for que recorre las cajas
            r=N%s
            if(r==0):
                paro=N-s+1
            else:
                paro=N-s+1+r
            if(paro < s):
                paro=paro+2*s
            if(s == floor(N/2)):
                paro=3*s
            for i in range(0,paro,s):                   #Recorre el texto caja por caja de tamanio s
                if(p in palabras[i:i+s]):               #Determina si la palabra actual esta en cada caja de tamanio s
                    noc=noc+1
                if(p in palabras_sh[i:i+s]):               #Determina si la palabra actual esta en cada caja de tamanio s
                    nocsh=nocsh+1
            nsh=round(M/(1+round(M-1)/(N-1)*(s-1)))
            if(noc != 0 and nsh !=0):
                dfwm=dfwm+log(nsh/noc)
            if(noc != 0 and nocsh !=0):
                dfw=dfw+log(nocsh/noc)
        #print('frec(',p,')=',M)
        gf[p]=dfwm

    #print(gf)
    sorted_x = sorted(gf.items(), key=operator.itemgetter(1))
    for it in sorted_x:
        print(it)

    #for it in gf:
        #print(it,gf[it])
    return sorted_x
