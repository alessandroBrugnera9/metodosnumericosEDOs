import numpy as np

B=np.array([1, 1, -1])
A=np.array([[0.001, 0.001, 0.015], [0.0015, 0.001, 0.001]])


def calcXlinha(x, y, z):
    xLinha=x*(B[0] - A[0, 0]*x - A[0, 1]*y - A[0, 2]*z)
    return xLinha


def calcYlinha(x, y, z):
    yLinha=y*(B[1] - A[1, 0]*x - A[1, 1]*y - A[1, 2]*z)
    return yLinha


def calcZlinha(x, y, z, alfa):
    Az=np.array([-alfa, -0.0005, 0])
    zLinha=z*(B[2] - Az[0]*x - Az[1]*y)
    return zLinha


def eulerExplicito(x, y, z, xLinha, yLinha, zLinha, t, alfa):
    h=t[1] - t[0]
    for passo in range(len(t) - 1):
        # utilizando metodo de newton
        x[passo + 1]=x[passo] + h*xLinha[passo]
        y[passo + 1]=y[passo] + h*yLinha[passo]
        z[passo + 1]=z[passo] + h*zLinha[passo]

        xLinha[passo + 1]=calcXlinha(x[passo + 1], y[passo + 1], z[passo + 1])
        yLinha[passo + 1]=calcYlinha(x[passo + 1], y[passo + 1], z[passo + 1])
        zLinha[passo + 1]=calcZlinha(x[passo + 1], y[passo + 1], z[passo + 1], alfa)
    return x, y, z


def jacobiano(h, x, y):
    jac=(np.zeros((2, 2)))

    # jac[0][0]=1 - h*(lambdaa - alfa*y)
    # jac[0][1]=- h*(alfa*x)
    # jac[1][0]=- h*(beta*y)
    # jac[1][1]=1 - h*(beta*x - gama)
    return jac


def RK4(x, y, z, xLinha, yLinha, zLinha, t, alfa):
    h=t[1] - t[0]
    for passo in range(len(t) - 1):
        # k para varivavel x
        # l para varivavel y
        # m para varivavel z
        k1=xLinha[passo]
        l1=yLinha[passo]
        m1=zLinha[passo]
        k2=calcXlinha(x[passo] + h/2*k1, y[passo] + h/2*l1, z[passo] + h/2*m1)
        l2=calcYlinha(x[passo] + h/2*k1, y[passo] + h/2*l1, z[passo] + h/2*m1)
        m2=calcZlinha(x[passo] + h/2*k1, y[passo] + h/2*l1, z[passo] + h/2*m1, alfa)
        k3=calcXlinha(x[passo] + h/2*k2, y[passo] + h/2*l2, z[passo] + h/2*m2)
        l3=calcYlinha(x[passo] + h/2*k2, y[passo] + h/2*l2, z[passo] + h/2*m2)
        m3=calcZlinha(x[passo] + h/2*k2, y[passo] + h/2*l2, z[passo] + h/2*m2, alfa)
        k4=calcXlinha(x[passo] + h*k3, y[passo] + h*l3, z[passo] + h*m3)
        l4=calcYlinha(x[passo] + h*k3, y[passo] + h*l3, z[passo] + h*m3)
        m4=calcZlinha(x[passo] + h*k3, y[passo] + h*l3, z[passo] + h*m3, alfa)

        # realizando integracao e appendeando na array f
        xLinha[passo]=(k1 + 2*k2 + 2*k3 + k4)/6
        yLinha[passo]=(l1 + 2*l2 + 2*l3 + l4)/6
        zLinha[passo]=(m1 + 2*m2 + 2*m3 + m4)/6

        # utilizando metodo de newton
        x[passo + 1]=x[passo] + h*xLinha[passo]
        y[passo + 1]=y[passo] + h*yLinha[passo]
        z[passo + 1]=z[passo] + h*zLinha[passo]

    return x, y, z
