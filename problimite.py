import numpy as np
from tridiagonal import tridiagonal

def problimite(N, Q, R, a, b_borne, alpha, beta):
    h = (b_borne - a) / (N + 1)
    
    D = -2.0 - Q * (h**2)
    I = np.ones(N - 1)
    S = np.ones(N - 1)
    
    B = R * (h**2)
    
    B[0] = B[0] - alpha
    B[-1] = B[-1] - beta
    
    y_int = tridiagonal(N, D, I, S, B)
    
    y_complet = np.zeros(N + 2)
    y_complet[0] = alpha
    y_complet[-1] = beta
    y_complet[1:N+1] = y_int
    
    return y_complet