import numpy as np
import matplotlib.pyplot as plt

import metodos2
#constantes e condicoes iniciais, criando vetores
x0=1.5
y0=1.5

t0=0
tf=10

# n=5000
#
# t=np.linspace(t0,tf,n)
# x=np.zeros(n)
# y=np.zeros(n)
# x[0]=x0
# y[0]=y0
#
# xLinha=np.zeros(n)
# yLinha=np.zeros(n)
# xLinha[0]=metodos2.calcXlinha(x0,y0)
# yLinha[0]=metodos2.calcYlinha(x0,y0)
#
# #arrays para guardar resolucao de cada metodo e comparar
# arraysX=[]
# arraysY=[]
#
# x,y = metodos2.eulerExplicito(x,y,xLinha,yLinha,t)
# arraysX.append(x)
# arraysY.append(y)
#
# #plot Euler explicito
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.plot(t, x, label="População de Coelhos", color="blue")
# ax.plot(t, y, label="População de Raposas", color="red")
#
# plt.title("Clássico modelo presa-predador com Euler Explícito")
# plt.legend(loc="upper left")
# ax.set(xlabel='Tempo', ylabel='População')
# plt.show()
#
# fig2=plt.figure()
# ax = fig2.add_subplot(1, 1, 1)
# ax.plot(x, y, label="Retrato de fase", color="black")
#
# plt.title(" Retrato de Fase do Clássico modelo presa-predador com Euler Explícito")
# plt.legend(loc="upper right")
# # ax.set(xlabel='Tempo', ylabel='População')
# plt.show()



#euler implicito
n=5000

t=np.linspace(t0,tf,n)
x=np.zeros(n)
y=np.zeros(n)
x[0]=x0
y[0]=y0

xLinha=np.zeros(n)
yLinha=np.zeros(n)
xLinha[0]=metodos2.calcXlinha(x0,y0)
yLinha[0]=metodos2.calcYlinha(x0,y0)

x,y = metodos2.eulerImplicito(x,y,xLinha,yLinha,t)

#plot Euler implicito
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(t, x, label="População de Coelhos", color="blue")
ax.plot(t, y, label="População de Raposas", color="red")

plt.title("Clássico modelo presa-predador com Euler Implicito")
plt.legend(loc="upper left")
ax.set(xlabel='Tempo', ylabel='População')
plt.show()

fig2=plt.figure()
ax = fig2.add_subplot(1, 1, 1)
ax.plot(x, y, label="Retrato de fase", color="black")

plt.title(" Retrato de Fase do Clássico modelo presa-predador com Euler Implicito")
plt.legend(loc="upper right")
# ax.set(xlabel='Tempo', ylabel='População')
plt.show()





