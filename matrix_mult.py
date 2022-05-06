x = [[8,5,1],[9,3,2],[4,6,3]]
y = [[8,5,3],[9,5,7],[9,4,1]]
result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for k in range(len(y[0])):
        result[i][j] += x[i][k]*[k][j]
for x in result:
    print(x)