n = int(input("Enter matrix size: "))

matrix = []

for i in range(n):
    matrix.append([])
    for j in range(n):
        matrix[i].append(0)
total = 1
direc = 1
sign = 1
currenti = 0
currentj = 0
maxi = n
maxj = n
mini = -1
minj = -1
while total <= n*n:
    if direc and sign:
        for j in range(currentj, maxj):
            matrix[currenti][j] = total
            total += 1
            currentj = j
        direc = 0
        mini = currenti
        currenti+=1
    elif not direc and sign:
        for i in range(currenti, maxi):
            matrix[i][currentj] = total
            total += 1
            currenti = i
        direc = 1
        sign = 0
        maxj = currentj
        currentj-=1
    elif direc and not sign:
        for j in range(currentj, minj, -1):
            matrix[currenti][j] = total
            total += 1
            currentj = j
        direc = 0
        maxi = currenti
        currenti-=1
    else:
        for i in range(currenti, mini, -1):
            matrix[i][currentj] = total
            total += 1
            currenti = i
        direc = 1
        sign = 1
        minj = currentj
        currentj+=1



for mat in matrix:
    print(mat)
