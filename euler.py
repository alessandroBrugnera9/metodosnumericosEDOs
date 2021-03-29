import math
import numpy as np


def euler(t, x, xLinha, passo, h):
    eps = 1E-15
    limiteContador = 7
    while (passo < len(t) - 1):
        # utilizando metodo de newton
        ul = x[passo] + h * xLinha[passo]
        ulProx = math.inf

        contador = 0
        convergiu = False
        while (contador < limiteContador and not convergiu):
            # montando o sistema para resolver problema da inversa do jacobiano
            A = jacobiano(h, ul, t[passo + 1])
            B = A * ul - (ul - h * calcXLinha(t[passo + 1], ul) - x[passo])
            ulProx = B / A
            if (np.abs(ulProx - ul) < eps):
                convergiu = True
            else:
                ul=ulProx
            contador += 1

        # appendeando na array x
        x = np.append(x, ul)

        # calculando fLinha para proxima iteracao
        xLinha = np.append(xLinha, calcXLinha(t[passo + 1], x[passo + 1]))

        # proximo passo
        passo += 1

    return x, xLinha


def jacobiano(h, x, t):
    derivadaEmX = 2 * (x - t ** 2)
    return 1 - h * derivadaEmX


def calcXLinha(t, x):
    xLinha = 2 * t + (x - t ** 2) ** 2
    return xLinha


def calculaErro(x, xEstrela):
    size = len(x)
    erro = np.zeros(size)

    # calcula os erros de todoo o dominio
    for i in range(size):
        erroParcial = xEstrela[i] - x[i]
        erro[i] = erroParcial

    return erro


def calcVetorXEstrela(t):
    xEstrela=np.zeros(len(t))
    for i in range(len(t)):
        xEstrela[i]=t[i] ** 2 + 1 / (1 - t[i])
    return xEstrela