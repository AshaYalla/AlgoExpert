def riverSizes(matrix):
    r = len(matrix)
    c = len(matrix[0])

    visited = set()
    nei = [[1,0],[0,1],[-1,0],[0,-1]]
    ans = []

    for i in range(r):
        for j in range(c):
            
            if (i,j) not in visited and matrix[i][j] == 1:
                
                queue = [(i,j)]
                river = 1
                visited.add((i,j))
                
                while queue:
                    ci,cj = queue.pop(0)
                    
                    for ni,nj in nei:
                        if ci+ni >= 0 and ci+ni < r and cj+nj >= 0 and cj+nj < c and (ci+ni,cj+nj) not in visited and matrix[ci+ni][cj+nj] == 1:
                            river+=1
                            queue.append((ci+ni,cj+nj))
                            visited.add((ci+ni,cj+nj))
                ans.append(river)
    return ans
                    
                        
                        
                        
                        
                        
                
            
