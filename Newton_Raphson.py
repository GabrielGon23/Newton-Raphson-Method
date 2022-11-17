import matplotlib.pyplot as plt
from math import e

#Funcao exemplo
def f(x):
    return(((x**2 + x -1)**11)/(1 + e**-x))

#Derivada da funcao
def df(x):
    return(((22*x*e**(2*x) + 22*x*e**x + 11*e**(2*x) + 11*e**x) * ((x**2+x-1)**10) + ((x**2 + x -1)**11) * (e**x)) / ((e**x + 1)**2))

#Aproximacao inicial
x0 = -0.5

#Precisao do erro
precisao = 1e-6

k = 1
#Armazena erros e iteracoes
errors = []
k_graph = []

#Aproximacao de newton
x0_newton = x0
x0_newton = x0_newton - (f(x0_newton) / df(x0_newton))
print("\n\t\t\t >>>   Metodo de Newton - Tabela   <<<") 
print("\n\tIteracao \t    x0_newton \t\t\t     f(x[k]) \t\tErro absoluto aproximado\n")
while((abs((f(x0_newton) / df(x0_newton))) > precisao)):
    x0_newton = x0_newton - (f(x0_newton) / df(x0_newton))
    errors.append((f(x0_newton) / df(x0_newton)))
    k_graph.append(k) 
    print('\t   ', k, '  \t', x0_newton, '   \t', f(x0_newton), '   ', (f(x0_newton) / df(x0_newton)))
    k = k+1
print("\n\tAproximacao final da Raiz:",round(x0_newton,6))
    
#Plota grafico de erro absoluto por iteracoes
plt.plot(k_graph , errors)
plt.title("Método de Newton - Gráfico do Erro absoluto aproximado")
plt.xlabel("Iterações")
plt.ylabel(["Erro aproximado"])
plt.show()
