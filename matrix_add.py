x = [[8,5,1],[9,3,2],[4,6,3]]
y = [[8,5,3],[9,5,7],[9,4,1]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
for k in result:
    print(k)