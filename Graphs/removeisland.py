def removeIslands(matrix):
    r = len(matrix)
    c = len(matrix[0])
    nei = [[1,0],[-1,0],[0,1],[0,-1]]
    visited = set()

    for i in range(0,r):
        for j in range(0,c):
            if( i == 0 or i ==  r-1 or j  == 0 or j == c-1 )and matrix[i][j] == 1 and (i,j) not in visited:
                queue = [(i,j)]
                visited.add((i,j))
                while(queue):
                    x,y = queue.pop(0)
                    print(x,y)
                    for ni,nj in nei:
                        if x+ni >= 0 and x+ni < r and y + nj >= 0 and y + nj < c and matrix[x+ni][y+nj] == 1 and (x+ni,y+nj) not in visited:
                            queue.append((x+ni,y+nj))
                            visited.add((x+ni,y+nj))
 
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1 and (i,j ) not in visited:
                matrix[i][j] = 0

    return matrix
