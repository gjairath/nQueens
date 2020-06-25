#!/usr/bin/env python
# coding: utf-8

# In[85]:


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

    print(f'Time Taken: {time.time() - start}')
        
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
    
    for i in range(0,N):
        print('\t')
        print (( ('    ' + '-') * N))
    
    for d in chessBoard.decls():
        print ("%s = %s" % (d.name(), chessBoard[d]))
        
def main():
    nQueens(4)

main()


# In[ ]:




