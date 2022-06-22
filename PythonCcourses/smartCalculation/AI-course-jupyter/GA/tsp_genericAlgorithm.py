# To add a new cell, type '##'
# To add a new markdown cell, type '## [markdown]'
##
import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt


##
from IPython.display import Image
Image(filename='1.png')

# [markdown]
# <font size=5>每座城市仅访问一次（不重不漏）
# 必须返回起始城市</font>
# [markdown]
# <font size=3>
#
# gene: 一座城市（以(x, y)坐标表示）
#
# individual: 或染色体（chromosome）： 满足以上条件的一个路由
#
# population: 一组可能的路由（即，一组个体）
#
# parents: 两个路由相组合，创建一个新路由
#
# mating pool: 一组父母，用来创建下一代种群（即创建下一代路由）
#
# fitness: 一个告诉我们每个路由有多好的函数（在我们的例子中，也就是距离多短）
#
# mutation: 在种群中引入变化的方法，随机交换路由中的两个城市
#
# Elitism: 将最好的个体保留至下一代
# </font>
# [markdown]
# ## Create necessary classes and functions
# [markdown]
#
# [markdown]
# Create class to handle "cities"

##


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance

    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

# [markdown]
# Create a fitness function

##


class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(0, len(self.route)):
                fromCity = self.route[i]
                toCity = None
                if i + 1 < len(self.route):
                    toCity = self.route[i + 1]
                else:
                    toCity = self.route[0]
                pathDistance += fromCity.distance(toCity)
            self.distance = pathDistance
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())
        return self.fitness

# [markdown]
# ## Create our initial population
# [markdown]
# Route generator

##


def createRoute(cityList):
    route = random.sample(cityList, len(cityList))
    return route

# [markdown]
# Create first "population" (list of routes)

##


def initialPopulation(popSize, cityList):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(cityList))
    return population

# [markdown]
# ## Create the genetic algorithm
# [markdown]
# Rank individuals

##


def rankRoutes(population):
    fitnessResults = {}
    for i in range(0, len(population)):
        fitnessResults[i] = Fitness(population[i]).routeFitness()
    return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)

# [markdown]
# Create a selection function that will be used to make the list of parent routes
# [markdown]
# <font size=3>我们为每个个体计算相对适应度权重（创建轮盘），然后将这些权重与一个随机数比较，以选择交配池。同时，我们打算保留最佳的路由，因此引入了精英选择。最后，selection函数返回路由ID的列表，供matingPool函数使用。</font>

##


def selection(popRanked, eliteSize):
    selectionResults = []
    df = pd.DataFrame(np.array(popRanked), columns=["Index", "Fitness"])
    df['cum_sum'] = df.Fitness.cumsum()
    df['cum_perc'] = 100*df.cum_sum/df.Fitness.sum()

    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    for i in range(0, len(popRanked) - eliteSize):
        pick = 100*random.random()
        for i in range(0, len(popRanked)):
            if pick <= df.iat[i, 3]:
                selectionResults.append(popRanked[i][0])
                break
    return selectionResults

# [markdown]
# Create mating pool

##


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool

# [markdown]
# Create a crossover function for two parents to create one child
# [markdown]
# <font size=3>TSP要求每个位置出现且仅出现一次。为了遵循这条规则，我们将使用一种特殊的繁殖函数有序交叉（ordered crossover）。在有序交叉中，我们随机选择父字符串的一个子集，然后用母字符串中的基因填充路由的剩余空位。填充时，按照基因在母字符串中出现的次序依次填充，跳过选中的父字符串子集中已有的基因。</font>


##
Image(filename='2.jpeg')


##
def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child

# [markdown]
# Create function to run crossover over full mating pool

##


def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    for i in range(0, length):
        child = breed(pool[i], pool[len(matingpool)-i-1])
        children.append(child)
    return children

# [markdown]
# Create function to mutate a single route
# [markdown]
# <font size=3>变异在GA中起到了重要作用，它通过引入新路由让我们得以探索解答空间的其他部分，避免收敛到局部最优值。和交叉类似，TSP问题中的变异需要特殊考虑。同样，如果我们的染色体由0和1组成，变异不过是给基因分配一个较低的由0变为1（或由1变0）的概率。
#
# 然而，因为我们需要遵守TSP的规则，我们无法丢弃城市。我们将转而使用交换变异（swap mutation）。这意味着，我们指定一个较低的概率，两座城市会在我们的路由中交换位置。</font>

##


def mutate(individual, mutationRate):
    for swapped in range(len(individual)):
        if(random.random() < mutationRate):
            swapWith = int(random.random() * len(individual))

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1
    return individual

# [markdown]
# Create function to run mutation over entire population

##


def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop

# [markdown]
# Put all steps together to create the next generation

##


def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    return nextGeneration

# [markdown]
# Final step: create the genetic algorithm

##


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    print("Initial distance: " + str(1 / rankRoutes(pop)[0][1]))

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)

    print("Final distance: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    return bestRoute

# [markdown]
# ## Running the genetic algorithm
# [markdown]
# Create list of cities

##
# # test data1(randon data)

# cityList = []

# for i in range(0,25):
#     cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))
# # cityList.append(123,444)
# cityList


##
# test data2:location from TSP_data.csv file

cityList = pd.read_csv(
    "./TSP_data.csv", names=["location", "latitude", "longtitude"])
##
cityList = cityList[["latitude", "longtitude"]]
cityList = cityList.values.tolist()
# cityList=[tuple(list_item) for list_item in cityList]
cityList = [City(list_item[0], list_item[1]) for list_item in cityList]
# cityList.head(5)
cityList

# [markdown]
# Run the genetic algorithm

##
geneticAlgorithm(population=cityList, popSize=100,
                 eliteSize=20, mutationRate=0.01, generations=500)
