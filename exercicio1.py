import numpy as np
import metodos
import matplotlib.pyplot as plt

t0=0
tf=2
erros = []
arraysX=[]
listaN = [20,40,80,160,320,640]

#condicoes iniciais
x=np.array([1,1,1,-1]).reshape(4,1)
xLinha= metodos.calcXLinha(x)

#faz o loop para calculdo de x e do erro com diferentes numeros de passos
for i in range(len(listaN)):
    h=(tf-t0)/listaN[i]
    x, xLinha = metodos.RK4(0,x,xLinha,listaN[i],h) #aplica RK4
    arraysX.append(x)
    erros.append(metodos.calculaErro(x,listaN[i],t0,tf)) #calcula erro e adiciona na lista de erros

#TODO: fazer a conta maluca do R
R=[]
for i in range(len(listaN)-1):
    R.append(np.max(erros[i])/np.max(erros[i+1]))
print("Array R:", end="")
print(R)


print("X finais: ")
for i in range(len(listaN)-1):
    print("n= {}: ".format(listaN[i]), end="")
    print(arraysX[i][:,-1])


#TODO: plotter
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for i in range(len(listaN)):
    eixoX=np.linspace(t0,tf,listaN[i])
    ax.plot(eixoX, erros[i], label="N= {}".format(listaN[i]))

plt.title("Erro do RK4 com diferente número de passos")
plt.legend(loc="upper right")
plt.show()