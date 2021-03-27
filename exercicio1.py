import numpy as np
import metodos
t0=0
tf=2
erros = []
listaN = [20,40,80,160,320,640]

#condicoes iniciais
x=np.array([1,1,1,-1]).transpose()
xLinha= metodos.calcXLinha(x)

#faz o loop para calculdo de x e do erro com diferentes numeros de passos
for i in range(len(listaN)):
    h=(tf-t0)/listaN[i]
    x, xLinha = metodos.RK4(0,x,xLinha,listaN[i],h) #aplica RK4
    erros.append(metodos.calculaErro(x,listaN[i],t0,tf)) #calcula erro e adiciona na lista de erros

#TODO: fazer a conta maluca do R
R=[]
for i in range(len(listaN)-1):
    R.append(np.max(erros[i])/np.max(erros[i+1]))
print("Array R:", end="")
print(R)


#TODO: plotter
