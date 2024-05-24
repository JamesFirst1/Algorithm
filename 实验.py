import random
import copy
import matplotlib.pyplot as plt
#initialization of genes in each individual for each generation(initial population and offspring pop)
#00000000000
class individual:
    def __init__(self):
        self.gene = [0]*N
        self.fitness = 0
            
N=10
P=50
population = []
offspring=[]
MUTRATE = 0.5
MUTSTEP=0.8
MAX=2
MIN=-1
generation=10
 
def test_function( ind ):
 
    utility=0
    for i in range(N):
        utility = utility + ind.gene[i]
    return utility
 
for x in range (0, P):
        tempgene=[]
        for y in range (0, N):
            tempgene.append( random.randint(0,1))
        newind = individual()
        newind.gene = tempgene.copy()
        population.append(newind)   
for i in range (0, P):
        population[i].fitness = test_function(population[i])
        #print(population[i].fitness)
 
for idx in range(generation):
    offspring=[]
    for i in range (0, P):
        parent1 = random.randint( 0, P-1 )
        off1 = copy.deepcopy(population[parent1])
        #print('off1\n',off1.fitness)
        parent2 = random.randint( 0, P-1 )
        off2 = copy.deepcopy(population[parent2])
        #print('off2\n',off2.fitness)
        if off1.fitness > off2.fitness:
            offspring.append( off1 )
        else:
            offspring.append( off2 )
    #for i in offspring:
        
        #print('offspring\n',i.gene)
            
        
 
 
    toff1 = individual()
    toff2 = individual()
    temp = individual()
    for i in range( 0, P, 2 ):
        toff1 = copy.deepcopy(offspring[i])
        toff2 = copy.deepcopy(offspring[i+1])
        temp = copy.deepcopy(offspring[i])
        crosspoint = random.randint(1,N)
        for j in range (crosspoint, N):
            toff1.gene[j] = toff2.gene[j]
            toff2.gene[j] = temp.gene[j]
        offspring[i] = copy.deepcopy(toff1)
        offspring[i+1] = copy.deepcopy(toff2)
     
        
    #flips each gene in all individuals in the population    
    # for i in range( 0, P ):
    #     newind = individual()
    #     newind.gene = []
    #     for j in range( 0, N ):
    #        gene = offspring[i].gene[j]
    #        mutprob = random.random()
    #        if mutprob < MUTRATE:
    #             if( gene == 1):
    #                 gene = 0
    #             else:
    #                 gene = 1
    #        newind.gene.append(gene)
    #     offspring=copy.deepcopy(newind)
    #you must then append new individual or overwrite offspring
    #IF MUTPROOB>MUTRATE THERE IS NO MUTATION
 
    #new stuff------------------------------------------------------------
    for i in range( 0, P ):
        newind = individual() #create template for the genes initialized at 0
        newind.gene = [] #empty container for genes
        for j in range( 0, N ):
           gene = offspring[i].gene[j]
        
           mutprob = random.random() #generate float between 0 and 1 for each gene in each individual
           if mutprob < MUTRATE: #mutation proceeds and starts
                alter = random.uniform(-MUTSTEP,MUTSTEP) #adds either -or+mutstep to each gene in individual
                gene = gene + alter # adds the mutstep to the gene if mutprob<mutrate
                if gene > MAX:  #rounding the gene
                        gene = MAX
                if gene < MIN:
                        gene = MIN
           newind.gene.append(gene)
        offspring[i]=copy.deepcopy(newind)
    #append new individual or overwrite offspring
    print(offspring)