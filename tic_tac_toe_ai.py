import math
import random

# Print board with 1–3 indexing
def print_board(board):
    print("\n    1   2   3")
    print("  -------------")
    for idx, row in enumerate(board):
        print(f"{idx+1} | {' | '.join(row)} |")
        print("  -------------")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# Minimax AI
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Best move using Minimax
def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Easy AI: Random move
def random_move(board):
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty)

# Game starts
print("🎮 Welcome to Tic-Tac-Toe!")
print("You are 'X' and AI is 'O'. Enter row/col from 1 to 3.")

# Choose difficulty
while True:
    difficulty = input("Choose difficulty (Easy / Hard): ").strip().lower()
    if difficulty in ['easy', 'hard']:
        break
    print("Please choose 'Easy' or 'Hard'.")

# Scoreboard
player_score = 0
ai_score = 0
draw_score = 0
round_count = 0
max_rounds = 3

# Game loop (Best of 3)
while round_count < max_rounds:
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print(f"\n🎲 Round {round_count + 1}")
    print_board(board)

    while True:
        # Player move
        while True:
            try:
                row = int(input("Enter row (1-3): ")) - 1
                col = int(input("Enter col (1-3): ")) - 1
                if row in range(3) and col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = 'X'
                        break
                    else:
                        print("🚫 Cell already taken.")
                else:
                    print("❌ Please enter numbers from 1 to 3.")
            except ValueError:
                print("⚠ Invalid input. Numbers only.")

        print_board(board)

        if check_winner(board) == 'X':
            print("🎉 You win this round!")
            player_score += 1
            break
        elif is_board_full(board):
            print("😐 It's a draw!")
            draw_score += 1
            break

        # AI Move
        print("💻 AI is thinking...")
        if difficulty == 'hard':
            move = best_move(board)
        else:
            move = random_move(board)
        board[move[0]][move[1]] = 'O'
        print_board(board)

        if check_winner(board) == 'O':
            print("🤖 AI wins this round!")
            ai_score += 1
            break
        elif is_board_full(board):
            print("😐 It's a draw!")
            draw_score += 1
            break

    round_count += 1
    print(f"📊 Score: You: {player_score} | AI: {ai_score} | Draws: {draw_score}")
    if round_count < max_rounds:
        input("👉 Press Enter to continue to next round...")

# Final result
print("\n🏁 Game Over!")
print(f"Final Score ➤ You: {player_score} | AI: {ai_score} | Draws: {draw_score}")

if player_score > ai_score:
    print("👑 You win the series!")
elif ai_score > player_score:
    print("💻 AI wins the series!")
else:
    print("🤝 It's a tie series!")