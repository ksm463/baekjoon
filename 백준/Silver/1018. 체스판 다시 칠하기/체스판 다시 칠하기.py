n, m = map(int, input().split())
board = []
map = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range (m-7):
        status_black = 0
        status_white = 0
        
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x + y) % 2 == 0:
                    if board[x][y] != 'B':
                        status_black += 1
                    if board[x][y] != 'W':
                        status_white += 1
                        
                else:
                    if board[x][y] != 'W':
                        status_black += 1
                    if board[x][y] != 'B':
                        status_white += 1
        
        map.append(status_black)
        map.append(status_white)

print(min(map))
