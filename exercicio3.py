import numpy as np
import matplotlib.pyplot as plt
import metodos3

# constantes e condicoes iniciais, criando vetores

x0=500
y0=500
z0=10

t0=0
arrayTf=[100, 100, 500, 500, 2000, 2000]
# arrayTf=[400]

n=6000
arraysAlfa=[0.001, 0.002, 0.0033, 0.0036, 0.005, 0.0055]
# arraysAlfa=[0.005]

for i in range(len(arraysAlfa)):
    t=np.linspace(t0, arrayTf[i], n)
    x=np.zeros(n)
    y=np.zeros(n)
    z=np.zeros(n)
    x[0]=x0
    y[0]=y0
    z[0]=z0

    xLinha=np.zeros(n)
    yLinha=np.zeros(n)
    zLinha=np.zeros(n)
    xLinha[0]=metodos3.calcXlinha(x0, y0, z0)
    yLinha[0]=metodos3.calcYlinha(x0, y0, z0)
    zLinha[0]=metodos3.calcZlinha(x0, y0, z0, arraysAlfa[i])

    x, y, z=metodos3.eulerExplicito(x, y, z, xLinha, yLinha, zLinha, t, arraysAlfa[i])

    if i==5:
        print(1)
    # plot Euler explicito
    fig=plt.figure()
    ax=fig.add_subplot(1, 1, 1)
    ax.plot(t, x, label="População de Coelhos", color="blue")
    ax.plot(t, y, label="População de Lebres", color="black")
    ax.plot(t, z, label="População de Raposas", color="red")

    plt.title("Clássico modelo presa-predador com Euler Explícito")
    plt.figtext(.5, .9, 'tf={}, alfa={}'.format(arrayTf[i],arraysAlfa[i]), fontsize=10, ha='center')
    fig.subplots_adjust(top=0.85)
    plt.legend(loc="upper left")
    ax.set(xlabel='Tempo', ylabel='População')
    fig.tight_layout()
    plt.show()

    fig2=plt.figure()
    ax=fig2.add_subplot(projection='3d')
    ax.plot(x, y, z, label="Retrato de fase", color="black")

    plt.title(" Retrato de Fase do Clássico modelo presa-predador com Euler Explícito")
    plt.figtext(.5, .9, 'tf={}, alfa={}'.format(arrayTf[i],arraysAlfa[i]), fontsize=10, ha='center')
    fig2.subplots_adjust(top=0.85)
    plt.legend(loc="upper right")
    # ax.set(xlabel='Tempo', ylabel='População')
    fig2.tight_layout()
    plt.show()

# parte 3
#
# arrayN=[250, 500, 1000, 2000, 4000]
# for n in arrayN:
#     t=np.linspace(t0, tf, n)
#     x=np.zeros(n)
#     y=np.zeros(n)
#     x[0]=x0
#     y[0]=y0
#
#     xLinha=np.zeros(n)
#     yLinha=np.zeros(n)
#     xLinha[0]=metodos2.calcXlinha(x0, y0)
#     yLinha[0]=metodos2.calcYlinha(x0, y0, z0)
#
#     xE, yE=metodos2.eulerExplicito(x, y, xLinha, yLinha, t)
#     xI, yI=metodos2.eulerImplicito(x, y, xLinha, yLinha, t)
#
#     eX=xI - xE
#     eY=yI - yE
#
#     # plot do erro
#     fig=plt.figure()
#     ax=fig.add_subplot(1, 1, 1)
#     ax.plot(t, eX, label="População de Coelhos", color="blue")
#     ax.plot(t, eY, label="População de Raposas", color="red")
#
#     plt.title("Clássico modelo presa-predador comparação de métodos de Euler n={}".format(n))
#     plt.legend(loc="upper left")
#     ax.set(xlabel='Tempo', ylabel='População')
#     plt.show()
#
# # parte 4
# # RK4
# n=500
#
# t=np.linspace(t0, tf, n)
# x=np.zeros(n)
# y=np.zeros(n)
# x[0]=x0
# y[0]=y0
#
# xLinha=np.zeros(n)
# yLinha=np.zeros(n)
# xLinha[0]=metodos2.calcXlinha(x0, y0)
# yLinha[0]=metodos2.calcYlinha(x0, y0, z0)
#
# x, y=metodos2.RK4(x, y, xLinha, yLinha, t)
#
# # plot RK4
# fig=plt.figure()
# ax=fig.add_subplot(1, 1, 1)
# ax.plot(t, x, label="População de Coelhos", color="blue")
# ax.plot(t, y, label="População de Raposas", color="red")
#
# plt.title("Clássico modelo presa-predador com RK4")
# plt.legend(loc="upper left")
# ax.set(xlabel='Tempo', ylabel='População')
# plt.show()
#
# fig2=plt.figure()
# ax=fig2.add_subplot(1, 1, 1)
# ax.plot(x, y, label="Retrato de fase", color="black")
#
# plt.title(" Retrato de Fase do Clássico modelo presa-predador com RK4")
# plt.legend(loc="upper right")
# # ax.set(xlabel='Tempo', ylabel='População')
# plt.show()
