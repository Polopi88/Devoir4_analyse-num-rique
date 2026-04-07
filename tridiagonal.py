import numpy as np

def tridiagonal(N, D, I, S, b):
    D_algo = np.copy(D)
    b_algo = np.copy(b)
    x = np.zeros(N)
    
    for i in range(1, N):
        multiplicateur = I[i-1] / D_algo[i-1]
        D_algo[i] = D_algo[i] - multiplicateur * S[i-1]
        b_algo[i] = b_algo[i] - multiplicateur * b_algo[i-1]
        
    x[-1] = b_algo[-1] / D_algo[-1]
    
    for i in range(N-2, -1, -1):
        x[i] = (b_algo[i] - S[i] * x[i+1]) / D_algo[i]
        
    return x