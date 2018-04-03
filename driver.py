# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 23:25:41 2017

@author: jc4730/JiadaChen/CS4701/HW4
"""
import sys
import itertools
import operator

char = 'ABCDEFGHI'
num = range(1,10)


class csp:
    
    def __init__(self,board):
        self.variables = [x + str(y) for x in char for y in num]
        self.domain = self.get_domain(board)
        self.constraints = self.get_constraints()
        
    def get_domain(self,board):
        domain = {}
        
        for i,x in enumerate(self.variables):
            if board[i] == '0':
                domain[x] = range(1,10)
            else:
                domain[x] = [int(board[i])]
        
        return domain
        
        
    def get_constraints(self):
        constraints = []

        alldiffs = [[x + str(y) for y in num] for x in char] + [[x + str(y) for x in char] for y in num] +\
            [[x + y for y in e_num for x in e_char] for e_num in ('123','456','789') for e_char in ('ABC','DEF','GHI')]

        for alldiff in alldiffs:
            constraints = constraints + list(itertools.combinations(alldiff,2))

        constraints = list(set(constraints))

        return constraints
    
    
    def get_neighbors(self,var):
        neighbors = []
        
        for constraint in self.constraints:
            if constraint[0] == var:
                neighbors.append(constraint[1])
            elif constraint[1] == var:
                neighbors.append(constraint[0])
        
        return list(set(neighbors))
    
    
    def satisfy(self,x,y):
        return x != y
    
    
    def fwd_check(self,assignment,var,x):
        neighbors = self.get_neighbors(var)
        fwd_del = dict.fromkeys(neighbors)
        
        for i in fwd_del:
            fwd_del[i] = []
        
        for neighbor in neighbors:
            if neighbor not in assignment:
                if (len(self.domain[neighbor])>1) and (x in self.domain[neighbor]):
                    self.domain[neighbor].remove(x)
                    fwd_del[neighbor].append(x)
                    
        return fwd_del
    
    
    def complete(self,assignment):
        if len(assignment) == len(self.variables):
            return True
        return False
    
    
    def consistent(self,assignment,var,x):
        neighbors = self.get_neighbors(var)
        
        for neighbor in neighbors:
            if (neighbor in assignment.keys()) and (x == assignment[neighbor]):
                return False
        
        return True
    
    
    def solved(self):
        for x in self.domain.keys():
            if len(self.domain[x]) <> 1:
                return False
        return True
    
    
    def to_string(self,assignment):
        result_string = ''
        
        for var in self.variables:
            result_string = result_string + str(assignment[var])
            
        return result_string
    
    
def ac3(csp):
    
    queue = csp.constraints[:]
    
    while queue:
        (x_i, x_j) = queue.pop()
        
        if revise(csp,x_i,x_j):
            if len(csp.domain[x_i]) == 0:
                return False
            for x_k in csp.get_neighbors(x_i):
                queue.append((x_k,x_i))
            for x_k in csp.get_neighbors(x_j):
                queue.append((x_k,x_j))
    
    return True


def revise(csp,x_i,x_j):
    
    revised = False
    
    for x in csp.domain[x_i]:
        if not any([csp.satisfy(x,y) for y in csp.domain[x_j]]):
            csp.domain[x_i].remove(x)
            revised = True
    for x in csp.domain[x_j]:
        if not any([csp.satisfy(x,y) for y in csp.domain[x_i]]):
            csp.domain[x_j].remove(x)
            revised = True
            
    return revised


def backtracking_search(csp):
    return backtrack({},csp)

def backtrack(assignment,csp):
    if csp.complete(assignment):
        return assignment
    var = select_unassigned_variable(csp,assignment)
    #print var
    
    for x in order_domain_values(var, assignment, csp):
        if csp.consistent(assignment,var,x):
            assignment[var] = x
            fwd_del = csp.fwd_check(assignment,var,x)
            result = backtrack(assignment,csp)
            
            if result:
                return result
            del assignment[var]
            for del_var in fwd_del:
                csp.domain[del_var] = csp.domain[del_var] + fwd_del[del_var]
    return False

def select_unassigned_variable(csp,assignment):
    unassigned_var = {}
    for var in csp.variables:
        if var not in assignment:
            unassigned_var[var] = len(csp.domain[var])
    return sorted(unassigned_var, key=unassigned_var.__getitem__)[0]


def order_domain_values(var, assignment, csp):
    lcv_dic = {}
    domain_values = csp.domain[var]
    for x in domain_values:
        lcv = 0
        for neighbor in csp.get_neighbors(var):
            if len(csp.domain[neighbor]) > 1 and x in csp.domain[neighbor]:
                lcv += 1
        lcv_dic[x] = lcv
    return sorted(lcv_dic, key=lcv_dic.__getitem__)    

    
def main():
    sudoku = csp(sys.argv[1])
    ac3(sudoku)
    #print 'ac3 done'
    result = backtracking_search(sudoku)
    solution = ''
    if result:
        solution = sudoku.to_string(result)
    
    output = open('output.txt','w')
    output.write(solution)
    output.close()

    
if __name__ == "__main__":
    main()