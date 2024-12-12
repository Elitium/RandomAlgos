matrix = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[20,1,1]]

def findMax(x,y):
    if x == y == 0: return matrix[x][y]
    if x == 0:
        return matrix[x][y] + findMax(x,y-1)
    elif y == 0:
        return matrix[x][y] + findMax(x-1,y)
    else:
        return matrix[x][y] + max(findMax(x-1,y), findMax(x,y-1))

print(findMax(5,2))
