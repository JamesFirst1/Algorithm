import random
import copy
import math
import matplotlib.pyplot as plt

class individual:
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0
    def show(self):
        print('gene',self.gene)
        print('fitness',self.fitness)



population = []
N=20
P=50
MUTRATE=0.5
MUTSTEP=0.02
MAX=10
MIN=-5
offspring=[]

for x in range (0, P):
    tempgene=[]
    for y in range (0, N):
        tempgene.append( random.randint(0,1))
    newind = individual()
    newind.gene = tempgene.copy()
    population.append(newind)

ave_fit_table=[]
best_fit_table=[]
def test_function( ind ):
    gene=ind.gene
    n=len(gene)
    utility=0
    utility1=0
    for i in range (n):
        utility1+=0.5*i*gene[i]*0.5*i*gene[i]
    for j in range (n):
        utility+=gene[i]*gene[i]+utility1*utility1+utility1**4
    return utility

    


for idx in range(20):
    print('population')
    for j in  population:
        print(j.gene)
    
    toff1 = individual()
    toff2 = individual()
    temp = individual()
    for i in range(0, P, 2):
        toff1 = copy.deepcopy(population[i])
        toff2 = copy.deepcopy(population[i+1])
        temp = copy.deepcopy(population[i])
        crosspoint = random.randint(1,N)
        for j in range (crosspoint, N):
            toff1.gene[j] = toff2.gene[j]
            toff2.gene[j] = temp.gene[j]
        population[i] = copy.deepcopy(toff1)
        population[i+1] = copy.deepcopy(toff2)

    offspring=[]
    for i in range( 0, P ):
        newind1 = individual()
        newind1.gene = []
        for j in range( 0, N ):
            gene = population[i].gene[j]
            mutprob = random.random()
            if mutprob < MUTRATE:
                alter = random.uniform(-MUTSTEP,MUTSTEP)
                gene = gene + alter
            if gene > MAX:
                gene = MAX
            if gene < MIN:
                gene = MIN
            newind1.gene.append(gene)
        offspring.append(newind1)
    print('offspring')
    for j in offspring:
        print(j.gene)
    for i in range (0, P):
        offspring[i].fitness = test_function(offspring[i])
    population=[]
    for i in range (0, P):
        parent1 = random.randint( 0, P-1 )
        off1 = copy.deepcopy(offspring[parent1])
        parent2 = random.randint( 0, P-1 )
        off2 = copy.deepcopy(offspring[parent2])
        if off1.fitness < off2.fitness:
            population.append( off1 )
        else:
            population.append( off2 )
    
    fitnesses=[]
    for i in range (0, P):
        population[i].fitness = test_function(population[i])
        fitnesses.append(population[i].fitness)
    ave_fit=sum(fitnesses)/len(fitnesses)
    best_fit=min(fitnesses)
    ave_fit_table.append(ave_fit)
    best_fit_table.append(best_fit)

plt.plot(range(20),ave_fit_table,marker='o')
plt.plot(range(20),best_fit_table,marker='+',linestyle='dashed')
plt.legend(('ave_fitness', 'best_fitness'), loc='upper right') 
#plt.xticks(range(20))
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()


