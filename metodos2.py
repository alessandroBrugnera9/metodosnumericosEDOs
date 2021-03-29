import numpy as np

lambdaa=2/3
alfa=4/3
beta=1
gama=1


def calcXlinha(x, y):
    xLinha=lambdaa*x - alfa*x*y
    return xLinha


def calcYlinha(x, y):
    yLinha=beta*x*y - gama*y
    return yLinha


def eulerExplicito(x, y, xLinha, yLinha, t):
    h=t[1] - t[0]
    for passo in range(len(t) - 1):
        # utilizando metodo de newton
        x[passo + 1]=x[passo] + h*xLinha[passo]
        y[passo + 1]=y[passo] + h*yLinha[passo]

        xLinha[passo + 1]=calcXlinha(x[passo + 1], y[passo + 1])
        yLinha[passo + 1]=calcYlinha(x[passo + 1], y[passo + 1])
    return x, y


def jacobiano(h, x, y):
    jac=(np.zeros((2, 2)))

    jac[0][0]=1 - h*(lambdaa - alfa*y)
    jac[0][1]=- h*(alfa*x)
    jac[1][0]=- h*(beta*y)
    jac[1][1]=1 - h*(beta*x - gama)
    return jac


def eulerImplicito(x, y, xLinha, yLinha, t):
    h=t[1] - t[0]

    eps=1E-15
    limiteContador=20
    passo=0
    while (passo<len(t) - 1):
        # utilizando metodo de newton
        xl=x[passo] + h*xLinha[passo]
        yl=y[passo] + h*yLinha[passo]
        ul=np.array([xl, yl]).reshape(2, 1)
        ulProx=np.array([np.inf, np.inf]).reshape(2, 1)

        contador=0
        convergiu=False
        while (contador<limiteContador and not convergiu):
            # montando o sistema para resolver problema da inversa do jacobiano
            jacobiandoInvertido=np.linalg.inv(jacobiano(h, ul[0][0], ul[1][0]))
            vetorDerivada=np.array([calcXlinha(ul[0][0], ul[1][0]), calcYlinha(ul[0][0], ul[1][0])]).reshape(2, 1)
            G=ul - h*vetorDerivada - np.array([x[passo], y[passo]]).reshape(2, 1)
            ulProx=ul - np.dot(jacobiandoInvertido, G)
            if (np.average(np.abs(ulProx - ul))<eps):
                convergiu=True
            else:
                ul=ulProx
            contador+=1

        # appendeando na array x
        x[passo + 1]=ul[0, 0]
        y[passo + 1]=ul[1, 0]

        # calculando fLinha para proxima iteracao
        xLinha[passo + 1]=calcXlinha(x[passo + 1], y[passo + 1])
        yLinha[passo + 1]=calcYlinha(x[passo + 1], y[passo + 1])

        # proximo passo
        passo+=1
    return x, y


def RK4(x, y, xLinha, yLinha, t):
    h=t[1] - t[0]
    for passo in range(len(t) - 1):
        # k para varivavel x
        # l para varivavel y
        k1=xLinha[passo]
        l1=yLinha[passo]
        k2=calcXlinha(x[passo] + h/2*k1, y[passo] + h/2*l1)
        l2=calcYlinha(x[passo] + h/2*k1, y[passo] + h/2*l1)
        k3=calcXlinha(x[passo] + h/2*k2, y[passo] + h/2*l2)
        l3=calcYlinha(x[passo] + h/2*k2, y[passo] + h/2*l2)
        k4=calcXlinha(x[passo] + h*k3, y[passo] + h*l3)
        l4=calcYlinha(x[passo] + h*k3, y[passo] + h*l3)

        # realizando integracao e appendeando na array f
        xLinha[passo]=(k1 + 2*k2 + 2*k3 + k4)/6
        yLinha[passo]=(l1 + 2*l2 + 2*l3 + l4)/6

        # utilizando metodo de newton
        x[passo + 1]=x[passo] + h*xLinha[passo]
        y[passo + 1]=y[passo] + h*yLinha[passo]

    return x, y
