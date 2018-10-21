#UFRN-DCA
#DCA0121 - Intelegencia Artificial Aplicada
#Questao 4 da prova da segunda unidade de IA - 2018.2
#Alunos: Deyvison Dantas, Elizabete Venceslau e Tereza Stephanny


import random
import math
LIMIT = 100000

def atualizar_temperatura(T): # Atualiza a Temperatura
	return T - 0.01

def vizinho(i, L): # Pega os pontos proximos essa função será chamada na funcao de SA
	if(L>1 and i>=0 and i<L):
		if i == 0:
			return [1]
		elif i == L - 1:
			return [L - 2]
		else:
			return [i - 1, i + 1]

def funcao(x): # Definindo a função  que usameremos para encontrar os minimos
	return (50 - sum(x - (10 * (math.cos(2 * math.pi *x)))))

def inicialize(L): # Inicializa 'mapemando' a funcao com cada resultado para a lista L(de temperaturas) que é passada como argumento
	return map(funcao, range(0, L))

def mover(x, A, T): # faz o movimento dos pontos na função onde x e o ponto que estamos testando se eh um minimo local ou global A eh a lista de pontos e  T eh a temperatura
    
	vizinho_novo = random.choice(range(0, len(A))) #escolhe um ponto aleatoriamente entre 0 e o tamanho de A

	diferenca = A[vizinho_novo] - A[x] # Calcula a diferença entre o novo ponto e o ponto que ja temos 

	if diferenca < 0:# se for menor que zero significa que o novo ponto eh menor que o que ja tinhamos
		return vizinho_novo
	else:
	        p = math.exp(-diferenca / T)
		if random.random() < p:
                        return vizinho_novo
		else:
			return x

def simulated_annealing(A): #função de simulated annealing
	L = len(A) #ver o tamanho da lista
	x0 = random.choice(range(0, L))#escolhe um minimo aleatorio
	T = 1.0 # valor escolhido porque a funcao cos(x) varia no intervalo (-1 , 1)
	k = 1 # numero de iteracoes

	x = x0 
	melhor_x = x0

	while T > 0.01:
        	x = mover(x, A, T)
        	if(A[x] < A[melhor_x]):
            		melhor_x = x
        	T = atualizar_temperatura(T)
        	k += 1

	print "Numero de interacao:", k
	return x, melhor_x, x0

def minimo_local(p, A): # verifica se o ponto eh um minimo local
    return all(A[p] < A[i] for i in vizinho(p, len(A)))

## main 
A = inicialize(LIMIT)

local_minimo = []
for i in range(0, LIMIT):
        if(minimo_local(i, A)):
            	local_minimo.append([i, A[i]])
x = 0
y = A[x]
for xi, yi in enumerate(A):
        if yi < y:
            	x = xi
            	y = yi
global_minimo = x

print "Numero de minimos locais: %d" % (len(local_minimo))
print "Minimo global %d = %0.2f" % (global_minimo, A[global_minimo])

x, melhor_x, x0 = simulated_annealing(A)
print "Para o valor %d a solucao eh %0.3f" % (x, A[x])
print "Para o valor %d melhor solucao eh %0.2f" % (melhor_x, A[melhor_x])
print "Para o valor %d solucao inicial foi %0.2f" % (x0, A[x0])

