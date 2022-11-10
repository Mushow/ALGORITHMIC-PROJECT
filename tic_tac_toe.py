board = [" " for _ in range(9)]


def print_board(player, winner=None):
    print(" " + player[0] + " | " + player[1] + " | " + player[2] + " ")
    print("---+---+---")
    print(" " + player[3] + " | " + player[4] + " | " + player[5] + " ")
    print("---+---+---")
    print(" " + player[6] + " | " + player[7] + " | " + player[8] + " ")
    if winner:
        print(f"""* Game over: {winner} won. *""")


def morpion():
    player = "X"
    tour = 0
    while True:
        print_board(board)

        while True:
            print(player + " turn. Enter a digit from 1 to 9.")
            move = input()

            if move.isdigit():
                move = int(move)
            else:
                print("> Enter a digit from 1 to 9.")
                continue

            if 1 <= move <= 9:
                move -= 1
                break

        if board[move] == " ":
            board[move] = player
            tour += 1
        else:
            print("! Case is already in use, please choose another one.")
            continue

        if board[0] == board[1] == board[2] != " " \
                or board[3] == board[4] == board[5] != " " \
                or board[6] == board[7] == board[8] != " " \
                or board[0] == board[3] == board[6] != " " \
                or board[1] == board[4] == board[7] != " " \
                or board[2] == board[5] == board[8] != " " \
                or board[0] == board[4] == board[8] != " " \
                or board[2] == board[4] == board[6] != " ":
            print_board(board, player)
            break

        if tour == 9:
            print("Tie!")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"


if __name__ == "__main__":
    morpion()
