# Greeting
print("""
Welcome to Tic Tac Toe game
========================================
             GAME RULES:
Each player can plase one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal
* vertical or
* diagonal row
========================================
""")
# Player Sign in
p_one = input("Input your name Player one: ")
p_two = input("Input your name Player two: ")
# Board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# Print board function
def print_board():
    print(f"""
  -------------
3 | {board[0][2]} | {board[1][2]} | {board[2][2]} |
---------------
2 | {board[0][1]} | {board[1][1]} | {board[2][1]} |
---------------
1 | {board[0][0]} | {board[1][0]} | {board[2][0]} |
  -------------
  | a | b | c |
""")


# Input to index function
def input_to_index(inpt):
    char_to_number = {"a": "0", "b": "1", "c": "2"}
    inpt = inpt.lower()
    indexes = [int(char_to_number[inpt[0]]), (int(inpt[1]) - 1)]
    return indexes


# Victory check function
def victory_check(stone):
    if board[0][0] == stone and board[0][1] == stone and board[0][2] == stone:
        return True
    elif board[1][0] == stone and board[1][1] == stone and board[1][2] == stone:
        return True
    elif board[2][0] == stone and board[2][1] == stone and board[2][2] == stone:
        return True
    elif board[0][0] == stone and board[1][0] == stone and board[2][0] == stone:
        return True
    elif board[0][1] == stone and board[1][1] == stone and board[2][1] == stone:
        return True
    elif board[0][2] == stone and board[1][2] == stone and board[2][2] == stone:
        return True
    elif board[0][0] == stone and board[1][1] == stone and board[2][2] == stone:
        return True
    elif board[0][2] == stone and board[1][1] == stone and board[2][0] == stone:
        return True


# Tie check function
def tie_check():
    if tie_count == 9 and not end_of_game:
        return True


# Game
end_of_game = False
tie_count = 0
print_board()
while not end_of_game:

    p_one_input = input(f"Make your move {p_one} (b2 for example): ")
    while not p_one_input in ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"):
        print("Incorrect coordinates!")
        print("You have to input a letter followed by number in range of field.")
        print("For example \"a1\" or \"c2\".")
        p_one_input = input(f"Make your move again {p_one}: ")
    p_one_move = input_to_index(p_one_input)
    board[p_one_move[0]][p_one_move[1]] = board[p_one_move[0]][p_one_move[1]].replace(" ", "X")
    print_board()
    if victory_check("X"):
        print(f"Great, you have won {p_one}!!!")
        end_of_game = True
        break
    tie_count += 1
    if tie_check():
        print("It is a tie!")
        end_of_game = True
        break

    p_two_input = input(f"Make your move {p_two} (b2 for example): ")
    while not p_two_input in ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"):
        print("Incorrect coordinates!")
        print("You have to input a letter followed by number in range of field.")
        print("For example \"a1\" or \"c2\".")
        p_two_input = input(f"Make your move again {p_two}: ")
    p_two_move = input_to_index(p_two_input)
    board[p_two_move[0]][p_two_move[1]] = board[p_two_move[0]][p_two_move[1]].replace(" ", "O")
    print_board()
    if victory_check("O"):
        print(f"Great, you have won {p_two}!!!")
        end_of_game = True
    tie_count += 1
    if tie_check():
        print("It is a tie!")
        end_of_game = True
