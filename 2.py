import math

board = [' ']*9
print(board)
PLAYER, AI = 'X', 'O'

def print_board():
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))
        if i < 6: print('-'*5)

def check_win(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i]==b[j]==b[k]==p for i,j,k in wins)

def evaluate():
    if check_win(board, AI): return 10
    if check_win(board, PLAYER): return -10
    return 0

def moves_left(): return ' ' in board

def a_star(depth, is_ai):
    score = evaluate()
    if score in [10, -10] or not moves_left(): return score - depth if is_ai else score + depth

    best = -math.inf if is_ai else math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI if is_ai else PLAYER
            val = a_star(depth+1, not is_ai)
            board[i] = ' '
            best = max(best, val) if is_ai else min(best, val)
    return best

def best_move():
    best_val, move = -math.inf, -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            val = a_star(0, False)
            board[i] = ' '
            if val > best_val: best_val, move = val, i
    board[move] = AI

def play():
    first = input("Who plays first? (1: Player, 2: Computer): ")
    print_board()
    while True:
        if first == '1':
            pos = int(input("Enter position (0-8): "))
            if board[pos] == ' ': board[pos] = PLAYER
            else: print("Taken!"); continue
        else:
            print("Computer is thinking...")
            best_move()

        print_board()
        if check_win(board, PLAYER): print("Player Wins!"); break
        if check_win(board, AI): print("Computer Wins!"); break
        if not moves_left(): print("Draw!"); break
        first = '1' if first == '2' else '2'

play()
