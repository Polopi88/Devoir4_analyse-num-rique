import numpy as np
import matplotlib.pyplot as plt
from problimite import problimite

L = 6.0
Ta = 20.0
T = 350.0
k = 1.2
a = 0.0
b_borne = L
alpha = T
beta = Ta

beta2 = (T - Ta) / (1 - np.exp(-2 * k * L))
beta1 = -beta2 * np.exp(-2 * k * L)

def solution_exacte(x):
    return Ta + beta1 * np.exp(k * x) + beta2 * np.exp(-k * x)

def q_func(N_size):
    return (k**2) * np.ones(N_size)

def r_func(N_size):
    return (-k**2 * Ta) * np.ones(N_size)

h_vals_a = [2.0, 1.0]
couleurs = ['blue', 'red']

plt.figure(1, figsize=(10, 6))

x_exact = np.linspace(a, b_borne, 200)
y_exact = solution_exacte(x_exact)
plt.plot(x_exact, y_exact, 'k-', linewidth=2, label='Solution exacte (Analytique)')

for i, h in enumerate(h_vals_a):
    N = int(round((b_borne - a) / h)) - 1
    
    Q = q_func(N)
    R = r_func(N)
    
    y_approx = problimite(N, Q, R, a, b_borne, alpha, beta)
    
    x_complet = np.linspace(a, b_borne, N + 2)
    plt.plot(x_complet, y_approx, marker='o', linestyle='--', color=couleurs[i], 
             label=f'Différences finies (h={h})')

plt.xlabel('Position dans la barre x')
plt.ylabel('Température y(x)')
plt.title('Figure 1 : Distribution de température dans la barre métallique')
plt.legend()
plt.grid(True)

h_vals_b = [L/3, L/6, L/100, L/10**3, L/10**4]
erreurs = []

for h in h_vals_b:
    N = int(round((b_borne - a) / h)) - 1
    
    Q = q_func(N)
    R = r_func(N)
    
    y_approx = problimite(N, Q, R, a, b_borne, alpha, beta)
    
    x_complet = np.linspace(a, b_borne, N + 2)
    y_exact_noeuds = solution_exacte(x_complet)
    
    erreur_max = np.max(np.abs(y_approx - y_exact_noeuds))
    erreurs.append(erreur_max)

plt.figure(2, figsize=(10, 6))
plt.loglog(h_vals_b, erreurs, 'mo-', linewidth=2, label='Erreur maximale E(h)')

h_ref = np.array(h_vals_b)
constante = erreurs[0] / (h_ref[0]**2)
plt.loglog(h_ref, constante * h_ref**2, 'k--', label='Pente 2 (Référence $O(h^2)$)')

plt.xlabel('Pas de discrétisation h (échelle log)')
plt.ylabel('Erreur maximale E(h) (échelle log)')
plt.title('Figure 2 : Comportement de l\'erreur en fonction du pas h')
plt.legend()
plt.grid(True, which="both", ls="--")

plt.show()