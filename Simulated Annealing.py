import random
import math
import matplotlib.pyplot as plt
N=20 # d value
MAX=10
MIN=-10 # The range of x
MUTSTEP=0.7
class Individual:
    def __init__(self, gene):
        self.gene = gene

def test_function(ind):
    gene = ind.gene
    n = len(gene)
    a = (gene[0] - 1) ** 2
    b = 0
    
    for i in range(1, n):
        b += i * (2 * gene[i] ** 2 - gene[i - 1]) ** 2
    result = a + b
    return result

def generate_individual(size):
    genes = [random.uniform(MIN, MAX) for _ in range(size)]
    return Individual(genes)

def generate_neighbor(ind):
    new_gene = [gene + random.uniform(-MUTSTEP, MUTSTEP) for gene in ind.gene]
    return Individual(new_gene)

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    return math.exp((old_cost - new_cost) / temperature)

def simulated_annealing(initial_solution, max_iterations, initial_temperature, cooling_rate):
    current_solution = initial_solution
    current_cost = test_function(current_solution)
    temperature = initial_temperature

    solutions = [current_solution]
    costs = [current_cost]

    for iteration in range(max_iterations):
        neighbor_solution = generate_neighbor(current_solution)
        neighbor_cost = test_function(neighbor_solution)
        # print('C\n',current_cost)
        # print('N\n',neighbor_cost)
        if random.random() < acceptance_probability(current_cost, neighbor_cost, temperature):
            current_solution = neighbor_solution
            current_cost = neighbor_cost

        temperature *= cooling_rate

        solutions.append(current_solution)
        costs.append(current_cost)

    return solutions, costs
def simu():
# if __name__ == "__main__":
    initial_solution = generate_individual(N)
    max_iterations = 10000
    initial_temperature = 1.0
    cooling_rate = 0.95

    result_solutions, result_costs = simulated_annealing(initial_solution, max_iterations, initial_temperature, cooling_rate)

    # 计算并打印最终的平均值和最优值
    avg_costs = [sum(result_costs[:i+1]) / (i+1) for i in range(len(result_costs))]
    best_costs = [min(result_costs[:i+1]) for i in range(len(result_costs))]

    print("average_fitness:", avg_costs[-1])
    print("best_fitness:", best_costs[-1])

    # 绘制收敛过程
    # plt.plot(result_costs, label='Objective Function Value')
    # plt.plot(avg_costs, label='Average Fitness')
    plt.plot(best_costs, linestyle='dashed', label='Best Fitness')
    plt.xlabel("Iterations")
    plt.ylabel("Fitness")
    plt.legend()
    plt.title("Simulated Annealing Convergence")
    plt.show()
simu()
