from random import *
import string
tam_pop = 10 #Número maximo de geracao  
funcao=[1,2,4,5,3]

def individuo():# criando individuo

	aux=[]
	for i in range (5):
		aux.append(randint(1,5))
	return aux 

def populacao():# criando a populacao

	aux=[]
	
	for i in range(tam_pop):
		aux.append(individuo())   
	return aux

def calcular_fitness(pop):  # Calculando a aptidao de cada individuo  
	aux2=[]
	aux3=[]
	aux4=[]
	for i in range(len(pop)):
		aux1=pop[i]
		aux2.append(aux1.count(1))
		aux2.append(aux1.count(2))
		aux2.append(aux1.count(3))
		aux2.append(aux1.count(4))
		aux2.append(aux1.count(5))
		aux3.append(aux2)
		aux2=[]
	
	for i in range(len(aux3)):
		aux2.append(sorted(aux3[i]))
	
	for i in range(len(pop)):

		aux4.append([pop[i],aux2[i][4]])
	return(aux4)	

def  selecionados(pop): # Seleciona para fazer a reproducao
	aux=[]
	for i in range(len(pop)):
		if pop[i][1] >= 1 and pop[i][1]<3:
			aux.append(pop[i][0])

	return(aux)
def crossover(pop):
	gerados=[]
	cont=0
	cont1=1
	
#deixando um numero par de seleciconados
	if len(pop)%2 != 0: 
#removendo a ultima posicao da lista caso seja um numero impar de selecionados
		del(pop[len(pop)-1])

	while cont <= (len(pop)/2):
		mae=pop[cont]
		pai=pop[cont1]
		filho1=mae
		filho2=pai
		aux1=pai[4]
		aux2=pai[0]
		aux3=mae[4]
		aux4=mae[0]
		filho1[0]=aux1
		filho1[4]=aux2
		filho2[0]=aux3
		filho2[4]=aux4
		gerados.append(filho1)
		gerados.append(filho2)
		cont=cont+2
		cont1=cont1+2
	return (gerados)
def mutacao(pop):
	pop[0][0]=1
	return(pop)
def checagem(func,pop):
	for i in range(len(pop)):
		if pop[i]==func:
			return "A rota foi encontrada."
	return "A rota nao foi encontrada."	
			
		
	
populacao = populacao()
fitness = calcular_fitness(populacao)
escolhidos=selecionados(fitness)
cruzamento=crossover(escolhidos)
pop_mutada=mutacao(cruzamento)
resposta=checagem(funcao,pop_mutada)

print(resposta)	
if resposta == False:
	
	populacao = populacao()
	fitness = calcular_fitness(populacao)
	escolhidos=selecionados(fitness)
	cruzamento=crossover(escolhidos)
	pop_mutada=mutacao(cruzamento)
	resposta=checagem(funcao,pop_mutada)	


	
