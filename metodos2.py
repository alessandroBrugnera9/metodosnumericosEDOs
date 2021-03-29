lambdaa = 2 / 3
alfa = 4 / 3
beta = 1
gama = 1


def calcXlinha(x, y):
    xLinha = lambdaa * x - alfa * x * y
    return xLinha


def calcYlinha(x, y):
    yLinha = beta * x * y - gama * y
    return yLinha


def eulerExplicito(x, y, xLinha, yLinha, t):
    h=t[1]-t[0]
    for passo in range(len(t)-1):
        # utilizando metodo de newton
        x[passo+1] = x[passo] + h * xLinha[passo]
        y[passo+1] = y[passo] + h * yLinha[passo]

        xLinha[passo+1] = calcXlinha(x[passo+1],y[passo+1])
        yLinha[passo+1] = calcYlinha(x[passo+1],y[passo+1])
    return x, y
