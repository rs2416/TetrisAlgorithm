
# NOTE: Tetris pieces can have 19 types of shape, each shape has an identification number, called shapeID. A placed piece should also be denoted as a tuple: (shapeID, pieceID), PieceID ranges from 1 to 𝑛, where 𝑛 is the total number of Tetris pieces used in the tiling solution, while shapeID ranges from 1 to 19.* 

from copy import deepcopy
from numpy import size

def Tetris(target):
    
##----MAKING SOLUTION MATRIX

    nrows = len(target)                    
    ncols = len(target[0])                                       

    solution = []               
    for i in range(nrows):
        row = []                          
        for j in range(ncols):
            row.append((0, 0))             
        solution.append(row)

##----MAKING ANOTHER TARGET USEFUL FOR ADJACENCY LIST

    target2 = deepcopy(target)

    replace = 0
    index = []
    coordinates = [[]]   
    
#list of coordinates of values, corresponding with value of index - filling list with, one empty sublist - so the indexes match up with the values of the nodes

    for i in range(nrows):
        for j in range(ncols):
            if target[i][j] == 1:
                coordinates.append([i,j])
                replace = replace + 1         #re-numbering all the 1s in the target matrix
                target2[i][j] = replace
                index.append(replace)         #making a list of target values

##----MAKING ADJACENCY LIST

    adnodes = [(0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)]

    adlist = [[]]    
    #filling list with, one empty sublist - so the indexes match up with the values of the nodes
    numberofneighbours = []                                      
                                                                  
    for i in range(nrows):
        for j in range(ncols):
            neighbours = []
            for k in adnodes: 
                y = i + k[1]   #ref coordinates of each tuple
                x = j + k[0]
                if y < 0 or y >= nrows or x < 0 or x >= ncols:
                    continue
                else:
                    neigh = target2[y][x]
                    if neigh > 0:
                        neighbours.append(neigh)


            center = target2[i][j]
            if center != 0:
                adlist.append(neighbours)

##----MAKING A LIST OF NUMBERS OF NEIGHBOURS FOR EACH NODE, NODE = INDEX 

    numneighbours = []   #making a list of numbers of neighbours for each node, node is the index
    for i in adlist:
        if size(i) > 0:
          numneighbours.append(size(i))
          
##----SORTING THE LIST OF NEIGHBOURS FOR EACH NODE FROM LOWEST NEIGHBOURS TO HIGHEST, WITH NODES SORTED IN SAME WAY

    orderedlengths, orderedneighboursqueue = (list(c) for c in zip(*sorted(zip(numneighbours,index))))   
#sorting the nodes the same way the number of neighbours for each nodes are sorted - therefore a list of nodes, with least neighbours to most neighbours

    squares = [] #list for 4 coordinates to fill
    piece = 0  #piece count

##----PICKING FOUR COORDINATES FOR A SHAPE, WITH PRIORITY FOR LOWEST NEIGHBOURS
 
    while len(orderedneighboursqueue) > 0:      

        squares = []
        set_of_neighbours = set()
        current_square = orderedneighboursqueue[0]
        squares.append(coordinates[current_square])                 
        set_of_neighbours.update(adlist[current_square])                                                                                         #making a set of each neighbour's neighbours so when get to an edge you don't miss the fourth square
        orderedneighboursqueue.remove(current_square)                                                                                           #removing the current used square from the 'queue'
        
        for neigh in adlist[current_square]:                                                                                                         #removing the current used square from the adjacency list, so it is no longer a neighbour to others
            adlist[neigh].remove(current_square)
        
                 
        while len(squares) < 4:                                                                                                                     #making sure 'squares' (coordinate list) is filled with only 4 coordinates
            best_neighbour = None                          
            low_neighbours = None
            for neighbour in set_of_neighbours:                                                         
                number_neighbours = len(adlist[neighbour])
                if coordinates[neighbour] not in squares:                                                                                                   # making sure I don't repeat coordinates         
                    if low_neighbours is None or number_neighbours < low_neighbours: 
                        best_neighbour = neighbour
                        low_neighbours = number_neighbours        
            if best_neighbour is not None:                                                                                                               #ranking neighbours                                 
                squares.append(coordinates[best_neighbour])          
                set_of_neighbours.update(adlist[best_neighbour])
                current_square = best_neighbour
                orderedneighboursqueue.remove(current_square)

                for neigh in adlist[current_square]:
                    adlist[neigh].remove(current_square)
                             
 
            else:                                                                                                                                       #breaking incase can't find 4 coordinates to fill  
                break
            
##----TURNING COORDINATES INTO RELATIVE COORDINATES AND MATCHING THEM TO SHAPE IDS AND FILLING SOLUTION WITH TUPLES
            
            if len(squares) == 4:

                coords = sorted(squares)     #sorting the list of coordinates
                fill = deepcopy(coords)      #copying the sorted coordinates

                x = fill[0][0]               #making relative coordinates
                y = fill[0][1]

                fill[1][0] = fill[1][0] - x
                fill[1][1] = fill[1][1] - y

                fill[2][0] = fill[2][0] - x
                fill[2][1] = fill[2][1] - y

                fill[3][0] = fill[3][0] - x
                fill[3][1] = fill[3][1] - y

                fill[0][0] = 0
                fill[0][1] = 0


                if fill == [[0, 0], [0, 1], [1, 0], [1, 1]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (1,piece)
                    solution[coords[1][0]][coords[1][1]] = (1,piece)
                    solution[coords[2][0]][coords[2][1]] = (1,piece)
                    solution[coords[3][0]][coords[3][1]] = (1,piece)
                elif fill == [[0, 0],[1, 0],[2, 0],[3, 0]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (2,piece)
                    solution[coords[1][0]][coords[1][1]] = (2,piece)
                    solution[coords[2][0]][coords[2][1]] = (2,piece)
                    solution[coords[3][0]][coords[3][1]] = (2,piece)
                elif fill == [[0, 0],[0, 1],[0, 2],[0, 3]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (3,piece)
                    solution[coords[1][0]][coords[1][1]] = (3,piece)
                    solution[coords[2][0]][coords[2][1]] = (3,piece)
                    solution[coords[3][0]][coords[3][1]] = (3,piece)               
                elif fill == [[0, 0], [1, 0], [2, 0], [2, 1]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (4,piece)
                    solution[coords[1][0]][coords[1][1]] = (4,piece)
                    solution[coords[2][0]][coords[2][1]] = (4,piece)
                    solution[coords[3][0]][coords[3][1]] = (4,piece)
                elif fill == [[0, 0], [1, -2], [1, -1], [1, 0]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (5,piece)
                    solution[coords[1][0]][coords[1][1]] = (5,piece)
                    solution[coords[2][0]][coords[2][1]] = (5,piece)
                    solution[coords[3][0]][coords[3][1]] = (5,piece)
                elif fill == [[0, 0], [0, 1], [1, 1], [2, 1]] :
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (6,piece)
                    solution[coords[1][0]][coords[1][1]] = (6,piece)
                    solution[coords[2][0]][coords[2][1]] = (6,piece)
                    solution[coords[3][0]][coords[3][1]] = (6,piece)
                elif fill == [[0, 0], [0, 1], [0, 2], [1, 0]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (7,piece)
                    solution[coords[1][0]][coords[1][1]] = (7,piece)
                    solution[coords[2][0]][coords[2][1]] = (7,piece)
                    solution[coords[3][0]][coords[3][1]] = (7,piece)
                elif fill == [[0, 0], [1, 0], [2, -1], [2, 0]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (8,piece)
                    solution[coords[1][0]][coords[1][1]] = (8,piece)
                    solution[coords[2][0]][coords[2][1]] = (8,piece)
                    solution[coords[3][0]][coords[3][1]] = (8,piece)
                elif fill == [[0, 0], [0, 1], [0, 2], [1, 2]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (9,piece)
                    solution[coords[1][0]][coords[1][1]] = (9,piece)
                    solution[coords[2][0]][coords[2][1]] = (9,piece)
                    solution[coords[3][0]][coords[3][1]] = (9,piece)
                elif fill == [[0, 0], [0, 1], [1, 0], [2, 0]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (10,piece)
                    solution[coords[1][0]][coords[1][1]] = (10,piece)
                    solution[coords[2][0]][coords[2][1]] = (10,piece)
                    solution[coords[3][0]][coords[3][1]] = (10,piece)
                elif fill == [[0, 0], [1, 0], [1, 1], [1, 2]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (11,piece)
                    solution[coords[1][0]][coords[1][1]] = (11,piece)
                    solution[coords[2][0]][coords[2][1]] = (11,piece)
                    solution[coords[3][0]][coords[3][1]] = (11,piece)
                elif fill == [[0, 0], [1, 0], [1, 1], [2, 0]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (12,piece)
                    solution[coords[1][0]][coords[1][1]] = (12,piece)
                    solution[coords[2][0]][coords[2][1]] = (12,piece)
                    solution[coords[3][0]][coords[3][1]] = (12,piece)
                elif fill == [[0, 0], [1, -1], [1, 0], [1, 1]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (13,piece)
                    solution[coords[1][0]][coords[1][1]] = (13,piece)
                    solution[coords[2][0]][coords[2][1]] = (13,piece)
                    solution[coords[3][0]][coords[3][1]] = (13,piece)
                elif fill == [[0, 0], [1, -1], [1, 0], [2, 0]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (14,piece)
                    solution[coords[1][0]][coords[1][1]] = (14,piece)
                    solution[coords[2][0]][coords[2][1]] = (14,piece)
                    solution[coords[3][0]][coords[3][1]] = (14,piece)
                elif fill == [[0, 0], [0, 1], [0, 2], [1, 1]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (15,piece)
                    solution[coords[1][0]][coords[1][1]] = (15,piece)
                    solution[coords[2][0]][coords[2][1]] = (15,piece)
                    solution[coords[3][0]][coords[3][1]] = (15,piece) 
                elif fill == [[0, 0], [0, 1], [1, -1], [1, 0]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (16,piece)
                    solution[coords[1][0]][coords[1][1]] = (16,piece)
                    solution[coords[2][0]][coords[2][1]] = (16,piece)
                    solution[coords[3][0]][coords[3][1]] = (16,piece)
                elif fill == [[0, 0], [1, 0], [1, 1], [2, 1]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (17,piece)
                    solution[coords[1][0]][coords[1][1]] = (17,piece)
                    solution[coords[2][0]][coords[2][1]] = (17,piece)
                    solution[coords[3][0]][coords[3][1]] = (17,piece)
                elif fill ==[[0, 0], [0, 1], [1, 1], [1, 2]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (18,piece)
                    solution[coords[1][0]][coords[1][1]] = (18,piece)
                    solution[coords[2][0]][coords[2][1]] = (18,piece)
                    solution[coords[3][0]][coords[3][1]] = (18,piece)
                elif fill == [[0, 0], [1, -1],[1, 0],[2, -1]]:
                    piece = piece + 1
                    solution[coords[0][0]][coords[0][1]] = (19,piece)
                    solution[coords[1][0]][coords[1][1]] = (19,piece)
                    solution[coords[2][0]][coords[2][1]] = (19,piece)
                    solution[coords[3][0]][coords[3][1]] = (19,piece)

    return solution
