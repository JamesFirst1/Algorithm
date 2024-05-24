import random
import copy
import math #not using math at this moment
import matplotlib.pyplot as plt

class individual: #初始化类，用于临时调用此规格的类的数组，并给此数组array赋予此类的格式
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0
    def show(self):
        print('gene',self.gene)
        print('fitness',self.fitness)

'''def test_function( ind ):
    
        gene=ind.gene
        n=len(gene)
        utility=0

        for i in range(n-1):
            utility+=100*(gene[i+1]-gene[i]*gene[i])*(gene[i+1]-gene[i]*gene[i])+(1-gene[i])*(1-gene[i])

        return utility'''

def test_function( ind ):
   
    gene = ind.gene
    n = len(gene)
    a = (gene[0]-1)**2
    b = 0

    for i in range(1,n):#all the operation should be inside the range
        b += i*(2*gene[i]**2-gene[i-1])**2
    result = a+b
    return result

''' def test_function(ind):

    gene = ind.gene
    n = len(gene)
    a = 0
    b = 0
    c = 0
    for i in range(n):#all the operation should be inside the range
        a += gene[i]**2

    for i in range(n):
        b += (0.5*i*gene[i])**2

    for i in range(n):
        c += (0.5*i*gene[i])**4

    result = a+b+c
    return result
'''
    



population = []
N=20 # d value
P=500
MUTRATE=0.05
MUTSTEP=0.7
MAX=10
MIN=-10 # The range of x
GEN=20
offspring=[]
ave_fit_table=[]
best_fit_table=[]
for x in range (0, P):
    tempgene=[]
    for y in range (0, N):
        tempgene.append( random.uniform(MIN,MAX))
    newind = individual()
    newind.gene = tempgene.copy()
    newind.fitness = test_function(newind)#get fitness for the old generation
    population.append(newind)




    


for idx in range(GEN):#try small range at the beginning to see the diagram is correct
    # print('population')
    # for j in  population:
    #     print(j.gene)

    offspring=[]
    
    for i in range (0, P):
        parent1 = random.randint( 0, P-1 )
        off1 = copy.deepcopy(population[parent1])
        parent2 = random.randint( 0, P-1 )
        off2 = copy.deepcopy(population[parent2])
        if off1.fitness < off2.fitness: #python list comparihension
            offspring.append( off1 )
        else:
            offspring.append( off2 )

    toff1 = individual()
    toff2 = individual()
    temp = individual()
    for i in range(0, P, 2):
        toff1 = copy.deepcopy(offspring[i])
        toff2 = copy.deepcopy(offspring[i+1])
        temp = copy.deepcopy(offspring[i])
        crosspoint = random.randint(1,N)
        for j in range (crosspoint, N):
            toff1.gene[j] = toff2.gene[j]
            toff2.gene[j] = temp.gene[j]
        offspring[i] = copy.deepcopy(toff1)
        offspring[i+1] = copy.deepcopy(toff2)
    
   

    fitnesses=[]

    
    for i in range( 0, P ):
        newind1 = individual()
        newind1.gene = []
        for j in range( 0, N ):
            gene = offspring[i].gene[j]
            mutprob = random.random()
            if mutprob < MUTRATE:
                alter = random.uniform(-MUTSTEP,MUTSTEP)
                gene = gene + alter
                if gene > MAX:
                    gene = MAX
                if gene < MIN:
                    gene = MIN 
            newind1.gene.append(gene)
        newind1.fitness  = test_function(newind1)        
        offspring[i] = newind1#覆盖
    '''print('offspring')
    for j in offspring:
        print(j.gene)'''

    # '''for i in range (0, P):
    #     offspring[i].fitness = test_function(offspring[i])# get the fitness of offspring'''

    best_individual = individual()
    best_individual=population[0]
    bestfit = population[0].fitness
    for i in range (0,P):

        if  population[i].fitness < bestfit:

            bestfit = population[i].fitness# update bestfit
            best_individual = population[i]
            
    ''' worst_individual=offspring[0]
    worstfit = offspring[0].fitness
    index_of_worst_individual = 0
    for i in range (0,P):

        if  offspring[i].fitness > worstfit:

            worstfit = offspring[i].fitness# update bestfit
            worst_individual = offspring[i]
            index_of_worst_individual = i
    
    offspring[index_of_worst_individual] = copy.deepcopy(best_individual) '''



    population=copy.deepcopy(offspring)

    '''worst_individual=individual()
    worstfit = population[0].fitness
    index_of_worst_individual = 0
    for i in range (0,P):

        if  population[i].fitness > worstfit:

            worstfit = population[i].fitness# update bestfit
            worst_individual = population[i]
            index_of_worst_individual = i'''
            
    for i in range (0, P):
        population[i].fitness = test_function(population[i])# get the fitness of population

    
    worst_fitnesses = [ind.fitness for ind in population]# it is an array

    index_of_worst_individual = worst_fitnesses.index(max(worst_fitnesses))#index method can only work for the array

    worst_individual = population[index_of_worst_individual]


    population[index_of_worst_individual] = copy.deepcopy(best_individual) 
    ''' make sure it has been replaced, get the minimum fitness value from old generation
     and replace the maximum fitness value from offspring'''

    
    

    fitnesses=[]
    for i in range (0, P):
        
        fitnesses.append(population[i].fitness)
    ave_fit=sum(fitnesses)/len(fitnesses)
    best_fit=min(fitnesses)
    ave_fit_table.append(ave_fit)
    best_fit_table.append(best_fit)

print('best_fitness',min(best_fit_table))
print('average_fitness',ave_fit)
 



plt.plot(range(GEN),ave_fit_table)#marke='o' is just give mark for each point
plt.plot(range(GEN),best_fit_table,linestyle='dashed') 
plt.legend(('ave_fitness', 'best_fitness'), loc='upper right') 
# plt.xticks(range(40))
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()



