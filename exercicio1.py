import os

import numpy as np
import metodos
import matplotlib.pyplot as plt
import euler

if not os.path.exists('figs/ex1'):  # garantir que pasta existe para salvar imagens
    os.makedirs('figs/ex1')

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
for i in range(len(listaN)):
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
fig.savefig("figs/ex1/1-Euler")
plt.show()


# -----------------------------
# 2a parte
t0 = 1.1
tf = 3
n = 5000

t = np.linspace(t0, tf, n)
x = np.array([-8.79])
xLinha = np.array([euler.calcXLinha(t[0], x[0])])

h = (tf - t0) / n
x, xLinha = euler.euler(t, x, xLinha, 0, h)  # aplica RK4
xEstrela = euler.calcVetorXEstrela(t)
erro = (euler.calculaErro(x, xEstrela))  # calcula erro e adiciona na lista de erros

fig, axs = plt.subplots(3)

fig.suptitle("Comparação de resolução exata e utilizando método de Euler implícito, n={}".format(n))
axs[0].plot(t, xEstrela)
axs[0].set_title("Solução explícita x*(t)")
axs[1].plot(t, x)
axs[1].set_title("Solução numérica x(t)")
axs[2].plot(t, erro)
axs[2].set_title("Erro E(t)=x*(t)-x(t)")

for ax in axs.flat:
    ax.set(xlabel='Tempo', ylabel='x(t)')

fig.tight_layout()

# shift subplots down:
fig.subplots_adjust(top=0.85)
fig.savefig("figs/ex1/1-RK4")
plt.show()
