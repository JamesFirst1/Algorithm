import random
import matplotlib.pyplot as plt

population = []
N = 10  # Replace with your desired value for N
LOOPS = 20  # Replace with your desired value for LOOPS
P=500
MAX=10
MIN=-10 # The range of x
offspring=[]
ave_fit_table=[]
best_fit_table=[]

class Solution:
    def __init__(self):
        self.gene = [0] * N
        self.fitness = 0

def test_function(ind):
    gene = ind.gene
    n = len(gene)
    a = (gene[0] - 1) ** 2
    b = 0

    for i in range(1, n):
        b += i * (2 * gene[i] ** 2 - gene[i - 1]) ** 2
    result = a + b
    return result


newind = Solution()
fitness_values = []

for x in range (0, P):
    tempgene=[]
    for y in range (0, N):
        tempgene.append( random.uniform(MIN,MAX))
    newind.gene = tempgene.copy()
    newind.fitness = test_function(newind)#get fitness for the old generation
    population.append(newind)

for x in range(LOOPS):
    for i in range( 0, P ): 
        newind1 = Solution()
        newind1.gene = newind.gene.copy()
        
        change_point = random.randint(0, N - 1)
        newind1.gene[change_point] = random.uniform(MIN, MAX)
        
        newind1.fitness = test_function(newind1)
        
        if newind.fitness >= newind1.fitness:
            newind.gene[change_point] = newind1.gene[change_point]
            newind.fitness = newind1.fitness
            fitness_values.append(newind.fitness)
       

            # Print the results
    ave_fit = sum(fitness_values) / len(fitness_values)
    best_fit =  min(fitness_values)
    ave_fit_table.append(ave_fit)
    best_fit_table.append(best_fit)

print('best_fitness',min(best_fit_table))
print('average_fitness',ave_fit)

# plt.plot(ave_fit_table)#marke='o' is just give mark for each point
plt.plot(best_fit_table,linestyle='dashed') 
plt.legend(('ave_fitness', 'best_fitness'), loc='upper right') 
plt.title('Optimization Progress')
# plt.xticks(range(40))
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()

