import os

import numpy as np
import matplotlib.pyplot as plt
import metodos2

if not os.path.exists('figs/ex2'):  # garantir que pasta existe para salvar imagens
    os.makedirs('figs/ex2')
#constantes e condicoes iniciais, criando vetores
x0=1.5
y0=1.5

t0=0
tf=10

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


x,y = metodos2.eulerExplicito(x,y,xLinha,yLinha,t)

#plot Euler explicito
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(t, x, label="População de Coelhos", color="blue")
ax.plot(t, y, label="População de Raposas", color="red")

plt.title("Clássico modelo presa-predador com Euler Explícito, n={}".format(n))
plt.legend(loc="upper left")
ax.set(xlabel='Tempo', ylabel='População')
fig.savefig("figs/ex2/1tempo, n={}".format(n))
plt.show()

fig2=plt.figure()
ax = fig2.add_subplot(1, 1, 1)
ax.plot(x, y, label="Retrato de fase", color="black")

plt.title(" Retrato de Fase do Clássico modelo presa-predador com Euler Explícito, n={}".format(n))
plt.legend(loc="upper right")
# ax.set(xlabel='Tempo', ylabel='População')
fig2.savefig("figs/ex2/1fase, n={}".format(n))
plt.show()



# euler implicito
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

plt.title("Clássico modelo presa-predador com Euler Implicito, n={}".format(n))
plt.legend(loc="upper left")
ax.set(xlabel='Tempo', ylabel='População')
fig.savefig("figs/ex2/2tempo, n={}".format(n))
plt.show()

fig2=plt.figure()
ax = fig2.add_subplot(1, 1, 1)
ax.plot(x, y, label="Retrato de fase", color="black")

plt.title(" Retrato de Fase do Clássico modelo presa-predador com Euler Implicito, n={}".format(n))
plt.legend(loc="upper right")
# ax.set(xlabel='Tempo', ylabel='População')
fig2.savefig("figs/ex2/2fase, n={}".format(n))
plt.show()




#parte 3

arrayN=[250,500,1000,2000,4000]
for n in arrayN:
    t=np.linspace(t0,tf,n)
    x=np.zeros(n)
    y=np.zeros(n)
    x[0]=x0
    y[0]=y0

    xLinha=np.zeros(n)
    yLinha=np.zeros(n)
    xLinha[0]=metodos2.calcXlinha(x0,y0)
    yLinha[0]=metodos2.calcYlinha(x0,y0)

    xE,yE = metodos2.eulerExplicito(x,y,xLinha,yLinha,t)
    xI,yI = metodos2.eulerImplicito(x,y,xLinha,yLinha,t)

    eX=xI-xE
    eY=yI-yE

    #plot do erro
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(t, eX, label="População de Coelhos", color="blue")
    ax.plot(t, eY, label="População de Raposas", color="red")

    plt.title("Clássico modelo presa-predador comparação de métodos de Euler n={}".format(n))
    plt.legend(loc="upper left")
    ax.set(xlabel='Tempo', ylabel='População')
    fig.savefig("figs/ex2/3tempo, n={}".format(n))
    plt.show()


#parte 4
#RK4
n=500

t=np.linspace(t0,tf,n)
x=np.zeros(n)
y=np.zeros(n)
x[0]=x0
y[0]=y0

xLinha=np.zeros(n)
yLinha=np.zeros(n)
xLinha[0]=metodos2.calcXlinha(x0,y0)
yLinha[0]=metodos2.calcYlinha(x0,y0)

x,y = metodos2.RK4(x,y,xLinha,yLinha,t)

#plot RK4
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(t, x, label="População de Coelhos", color="blue")
ax.plot(t, y, label="População de Raposas", color="red")

plt.title("Clássico modelo presa-predador com RK4")
plt.legend(loc="upper left")
ax.set(xlabel='Tempo', ylabel='População')
fig.savefig("figs/ex2/4tempo, n={}".format(n))
plt.show()

fig2=plt.figure()
ax = fig2.add_subplot(1, 1, 1)
ax.plot(x, y, label="Retrato de fase", color="black")

plt.title(" Retrato de Fase do Clássico modelo presa-predador com RK4, n={}".format(n))
plt.legend(loc="upper right")
# ax.set(xlabel='Tempo', ylabel='População')
fig2.savefig("figs/ex2/4fase, n={}".format(n))
plt.show()