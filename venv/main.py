from pyevolve import G1DList
from pyevolve import GSimpleGA
from random import randint, random
from operator import add

def individual(lenght, min, max):
    return [randint(min, max) for x in xrange(lenght)]

def population(count, lenght, min, max):
    return [individual(lenght, min, max) for x in xrange(count)]

def fitness(individual, target):
    sum = reduce(add, individual, 0)
    return abs(target-sum)

def grade(pop, target):
    summed = reduce(add, (fitness(x, target) for x in pop), 0)
    return summed / (len(pop) * 1.0)

def evolve(pop, taget, retain=0.2, random_select=0.05, mutate=0.01):
    graded = [(fitness(x, target), x) for x in pop]
    graded = [x[1] for x in sorted(graded)]
    retain_length = int(len(graded)*retain)
    parents = graded[:retain_length]

    for individual in parents:
        if mutate > random():
            pos_to_mutate = randint(0, len(individual) -1)
            individual[pos_to_mutate] = randint(min(individual), max(individual))

    parents_length = len(parents)
    desired_length = len(pop) - parents_length
    children = []
    while len(children) < desired_length:
        male = randint(0, parents_length -1)
        female = randint(0, parents_length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) / 2
            child = male[:half] + female[half:]
            children.append(child)

    parents.extend(children)
    return parents

#print (individual(5, 0, 100))
#print (population(3, 5, 0, 100))

#x = individual(5, 0, 100)
#print(fitness(x, 200))

#x = population(3,5,0,100)
#target = 200
#print (grade(x, target))

target = 371
p_count = 100
i_length = 5
i_min = 0
i_max = 100
p = population(p_count, i_length, i_min, i_max)
fitness_history = [grade(p, target),]
for i in xrange(100):
    p = evolve(p, target)
    fitness_history.append(grade(p, target))

for datum in fitness_history:
    print datum
