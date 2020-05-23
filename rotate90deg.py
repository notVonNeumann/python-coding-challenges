inputArray = [[1,2,3],[4,5,6],[7,8,9]]


def rotate90deg(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    
    # reflect with respect to diagonal
    for i in range(0,rows):
        for j in range(i,columns):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp      
    # reflect with respect to column
    for i in range(0,rows):
        for j in range(0,int(rows / 2)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][columns - 1 - j]
            matrix[i][columns - 1 - j] = temp
          
def printArray(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    
    for i in range(0,rows):
        for j in range(0,columns):
            print(matrix[i][j], end = " ")
        print(" ")
    print()

printArray(inputArray)

i = int(input("How many times do you want to rotate the matrix?: "))
print()

while i > 0:
    rotate90deg(inputArray)
    printArray(inputArray)
    i -= 1
