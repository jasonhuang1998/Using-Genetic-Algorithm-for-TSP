import random
import matplotlib.pyplot as plt
import time
def PrintArr():
    for i in range (node_num):
        for j in range (node_num):
            print(arr[i][j],end = " ")
        print("")
def PrintPopulation():
    for i in range (ps):
        for j in range (node_num):
            print(population[i][j],end = " ")
        print("")
    print("-----------------")
def PrintDistance():
    for i in range (ps):
        print(distance[i],end = " ")
    print("")
def InitializeDistance():
    for i in range (ps):
        distance[i] = 0
def swap(a,b):
    temp = a
    a = b
    b = temp
def BubbleSort():
    for i in range(ps):
        for j in range(ps-1):
            if distance[j] > distance[j+1]:
                temp = distance[j]
                distance[j] = distance[j+1]
                distance[j+1] = temp
                temp = population[j]
                population[j] = population[j+1]
                population[j+1] = temp
def Crossover1(a, b):
    #a is the id of the Elite
    #change rate about 40%
    head = random.randint(0, int(node_num/2))
    for i in range (int(node_num/2)):
        population[b].remove(population[a][head + i])
    for i in range (int(node_num/2)):
        population[b].append(population[a][head + i])
def Crossover2(a, b):
    #a is the id of the Elite
    #change rate about 40%
    head = random.randint(0, int(node_num/2))
    for i in range (int(node_num/2)):
        population[b].remove(population[a][head + i])
    for i in range (int(node_num/2)):
        population[b].insert(0, population[a][head + int(node_num/2)-i-1])
def Mutation1(a):
    #two elements to swap
    seq = [0] * node_num
    for i in range (node_num):
        seq[i] = i
    pick = random.sample(seq, 2)
    temp = population[a][pick[0]]
    population[a][pick[0]] = population[a][pick[1]]
    population[a][pick[1]] = temp
def Mutation2(a):
    #three elements to swap
    seq = [0] * node_num
    for i in range (node_num):
        seq[i] = i
    pick = random.sample(seq, 3)
    temp = population[a][pick[0]]
    population[a][pick[0]] = population[a][pick[1]]
    population[a][pick[1]] = population[a][pick[2]]
    population[a][pick[2]] = temp
def PrintAns(i):
    #PrintPopulation()
    start = time.clock()
    end = time.clock()
    print ()
    print("The ",i," generation" )
    BubbleSort()
    print("Best distance:" , distance[0])
    sum_distance = 0
    for j in range (ps):
        sum_distance = sum_distance + distance[j]
    print("Average distance:" , round(sum_distance/ps,2))
    print("Worst distance:" , distance[ps-1])
    print("Run Time:" , end-start)
    print("--------------------------")
    best.append(distance[0])
    average.append(round(sum_distance/ps,2))
    worst.append(distance[ps-1])
    
#----------------------------------------------------------------------------
#start UI
cp = int(input("Please input the crossover probability(1~100):"))
mp = int(input("Please input the mutation probability(1~100):"))
ps = int(input("Please input the population size:"))
generation = int(input("Please input the generation:"))
#end UI
#start put file into arr
f = open('test4.txt', 'r')
input_txt = f.read()
node_num = int(input_txt.split("\n")[0])#get number of nodes
arr = [[0]*node_num for i in range(node_num)]
for i in range (node_num):
    for j in range (node_num):
        arr[i][j] = int(input_txt.split("\n")[i+1].split( )[j])
#end put file into  arr
#start genarate population
population = [[0]*node_num for i in range(ps)]
for i in range (ps):
    for j in range (node_num):
        population[i][j] = j+1
for i in  range (ps):
    population[i] = random.sample(population[i], node_num)
#end generate population
#start crossover + mutation
distance = [0] * ps
crossover_num = int(cp * ps / 100)#Unconditional rounding
mutation_num = int(mp * ps / 100)#Unconditional rounding
best = []
average = []
worst = []
InitializeDistance()
for j in range (ps):
    for k in  range(node_num-1):#find all parents' distance
        distance[j] = distance[j] + arr[population[j][k]-1][population[j][k+1]-1]
PrintAns(1)
for i in range (generation):
    BubbleSort()
    #start crossover
    for j in range (crossover_num):
        if j % 2 == 0: 
            Crossover1(0, ps-j-1)#first way to crossover
        else:
            Crossover2(0, ps-j-1)#second way to crossover
    #end crossover
    #start mutation
    seq = [0] * ps
    for j in range (ps):
        seq[j] = j
    mutation_list = random.sample(seq, mutation_num)
    for j in range (mutation_num):
        if j % 2 == 0:
            Mutation1(mutation_list[j])#first way to muatate
        if j % 2 == 1:
            Mutation2(mutation_list[j])#first way to muatate
    InitializeDistance()
    for j in range (ps):
        for k in  range(node_num-1):#find all parents' distance
            distance[j] = distance[j] + arr[population[j][k]-1][population[j][k+1]-1]
    PrintAns(i+2)
    #end mutation
#end crossover + mutation    
plt.plot(best)
plt.plot(worst)
plt.plot(average)
plt.show()