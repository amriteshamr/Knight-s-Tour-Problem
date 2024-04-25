pathRow1 = [2, 1, -1, -2, -2, -1, 1, 2]
pathCol1 = [1, 2, 2, 1, -1, -2, -1, 1]

def FindKnightTour(visited, row, col, move):
    if move == 64:
        for i in range(8):
            for j in range(8):
                print(f"{visited[i][j]:2d}", end=" ")  # Format the output
            print()
        return True
    else:
        for index in range(len(pathRow1)):
            rowNew = row + pathRow1[index]
            colNew = col + pathCol1[index]
            if ifValid(visited, rowNew, colNew):
                move += 1
                visited[rowNew][colNew] = move
                if FindKnightTour(visited, rowNew, colNew, move):
                    return True
                move -= 1
                visited[rowNew][colNew] = 0
        return False

def ifValid(visited, rowNew, colNew):
    if 0 <= rowNew < 8 and 0 <= colNew < 8 and visited[rowNew][colNew] == 0:
        return True
    return False

visited = [[0 for _ in range(8)] for _ in range(8)]

visited[0][0] = 1
FindKnightTour(visited, 0, 0, 1)

