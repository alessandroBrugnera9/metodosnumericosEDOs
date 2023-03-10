import math
import numpy as np
def RK4 (passo, x, xLinha, passos, h):
    #tamanho das arrays usado para indexar ultimo parametro para integracao
    sizeF = len(x[0])
    sizeFLinha = len(xLinha[0])

    #calculando parametros do runge Kutta "K"s

    k1= xLinha[:, sizeFLinha - 1]
    k2=calcXLinha(x[:, sizeF - 1] + h / 2 * k1)
    k3=calcXLinha(x[:, sizeF - 1] + h / 2 * k2)
    k4=calcXLinha(x[:, sizeF - 1] + h * k3)

    #realizando integracao e appendeando na array f
    x = np.append(x, np.reshape(x[:, sizeF - 1] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4),(4,1)), axis=1)

    #calculando fLinha para proxima iteracao
    xLinha = np.append(xLinha, np.reshape(calcXLinha(x[:, sizeF]),(4,1)),axis=1)

    #recursao
    if (passo<passos):
        x, xLinha = RK4(passo+1,x,xLinha,passos,h)

    return x,xLinha


def calcXLinha (x):
    A= np.array([[-2,-1,-1,-2],[1,-2,2,-1],[-1,-2,-2,-1],[2,-1,1,-2]])

    xLinha = np.dot(A, x)
    return xLinha

def calcXEstrela (t):
    xEstrela = np.zeros(4)
    xEstrela[0] = math.exp(-t)*math.sin(t) + math.exp(-3*t)*math.cos(3*t)
    xEstrela[1] = math.exp(-t)*math.cos(t) + math.exp(-3*t)*math.sin(3*t)
    xEstrela[2] = -math.exp(-t)*math.sin(t) + math.exp(-3*t)*math.cos(3*t)
    xEstrela[3] = -math.exp(-t)*math.cos(t) + math.exp(-3*t)*math.sin(3*t)

    return xEstrela.reshape(4,1)

def calculaErro (x,n,t0,tf):
    dominio = np.linspace(t0,tf,n)
    erro = np.zeros(n)

    #calcula os erros de todoo o dominio
    for i in range(n):
        erroParcial=np.max(calcXEstrela(dominio[i])-x[:,i].reshape(4,1))
        erro[i]=erroParcial

    return erro


