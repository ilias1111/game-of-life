import numpy as np
import copy

rules = input().split(";")
N, Generations = input().split()
N = int(N)
Generations = int(Generations)

init_grid = [[0 for i in range(N)] for k in range(N)]#np.zeros((N,N), dtype=np.uint8)
#print(init_grid)
for i in range(0, N):
    t = input()
    init_grid[i] = [int(i) for i in t]

#print(init_grid)


def create_rules(string):
    
    lista = []
    
    for i,v in enumerate(string):
        
        if v == '1':
            
            lista.append(i)
            
    return set(lista)

rules_list = [create_rules(rules[0]),create_rules(rules[1])]
#print(rules_list)

def update(grid, N, rule): 
  
  
    newGrid = copy.deepcopy(grid)
    for i in range(N): 
        for j in range(N): 

            total = int(grid[i][(j-1)%N] + grid[i][(j+1)%N] + grid[(i-1)%N][j] + grid[(i+1)%N][j])
            # apply Conway's rules 
            if grid[i][j]  == 0:
                if total in rule[0]:
                    newGrid[i][j] = 1
            else:
                if total not in rule[1]: 
                    newGrid[i][j] = 0
  
    return newGrid


grid = copy.deepcopy(init_grid)

for i in range(0,Generations):
    
    grid = update(grid,N, rules_list)


for row in grid:
    
        print("".join([str(i) for i in row]))

    
    
    
    
