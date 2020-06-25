#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from z3 import *

import sys

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nQueens.py
#  
#  Copyright 2020 Garvit <Garvit@DESKTOP-QUE5L52>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

# TODO
    # fix repo
    # seperate functions
    # document better
    # create utility file


def nQueens(N):
    import time
    start = time.time()

    genericSolver = Solver()
    # An nQueens problem is when we place queens on a board such that it can attack any other queen
    
    # Encoding: Encode chess-board such that it's mapped as index:value. Index being coloumn and value being row.
    # If a queen is on the top left most tile, it will be the first element in the array. 
    
    #create N variable elements
    queenArray = [Int('x%i' %i) for i in range(N)] 
    
    #Create the value array each row has a value
    valuesArray = [And(queenArray[i] >= 1, queenArray[i] <= N) for i in range(N)]
    

    #Constraint 1: Each row must have only one queen
    genericSolver.add(Distinct(queenArray))
    
    #Constraint 2: Each diagnol must not contain a queen. 
    diagArray = [If(i == j, True, And(queenArray[i] - queenArray[j] != i - j, queenArray[i] - queenArray[j] != j - i)) 
                 for i in range(N) for j in range(i)]
    
    genericSolver.add(diagArray)
    genericSolver.add(valuesArray)
    
    print ('Finding solution')
    
    if (N > 25):
        print ('This may take a while for large inputs')
    
    genericSolver.check()
    
    for i in progressbar(range(N), "Finding: ", 40): 
        time.sleep(0.1)
        Solutions = genericSolver.model()

    print(f'Time Taken: {time.time() - start}', end = ' seconds')
        
    display(Solutions, N)

def progressbar(progressVal, prefix="", size=60, file=sys.stdout):
    
    count = len(progressVal) #number queens
    def show(j):
        x = int(size * j / count)
        file.write("%s%s%s %i/%i\r" % (prefix, "."*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(progressVal):
        yield item
        show(i+1)
        
    file.write("\n")
    file.flush()


def display(chessBoard, N):
    print('\n' * 4)
    

    sortedList = [0] * N
    for d in chessBoard.decls():
        sortedList[int(d.name()[1:])] = chessBoard[d]
    #print(sortedList)
    if (N <= 16):
        print('\n\n\n')
        for i in range(1,N+1):

            for j in range(1,N+1):
                if i == sortedList[j-1]:
                    print('\tQ\t', end = '')
                else:
                    print('\t-\t', end = '')

            print('\n')
        
    else:
        print('Warning: Your input is too large')
        print('Showing in key:mapping form instead!\n')
        i = 1
        for item in sortedList:
            print('Coloumn ', end = '')
            print(i, end = '\t') 
            i+=1
            print(item)

def main():
    inputChoice = input('Enter number of queens: ')
    assert(int(inputChoice) > 3), 'Enter a number of queens greater than 3!'
    
    nQueens(int(inputChoice))

    print('Try again?')
    inputChoice2 = input('1 for Yes \n2 for No \n Enter choice:')
    print ('\n')
    if (int(inputChoice2) == 1):
        main()
    else:
        exit()
main()


# In[ ]:




