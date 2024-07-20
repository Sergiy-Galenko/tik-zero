def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def play_game():
    board = [[" " for _ in range(3)] for _ in  range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Гравець {current_player}, введіть номер рядка (0, 1, 2): "))
        col = int(input(f"Гравець {current_player}, введіть номер рядка (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
        else: 
            print("Ця клітинка занята для іншим гравцем")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Гавець {current_player} Виграв")
            break
        if is_draw(board):
            print_board(board)
            print("Нічья")
            break

        current_player = "0" if current_player == "X" else "X"

play_game()
        
