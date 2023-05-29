from sys import stdin


def board_game(rows):
    board = []
    for i in range(int(rows)):
        board.append(input())
    game = []
    for i in range(len(board)):
        row = []
        for j in range(len(board[i])):
            if board[i][j] == "*":
                row.append(9)
            else:
                row.append(0)
        game.append(row)
    row_zeros = [0] * (len(game[0]) + 2)
    for i in range(len(game)):
        game[i].insert(0, 0)
        game[i].insert(len(game[i]), 0)
    game.insert(0, row_zeros)
    game.insert(len(game), row_zeros)
    return game


def numbers(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 8:
                board[i][j + 1] += 1
                board[i][j - 1] += 1
                board[i + 1][j] += 1
                board[i + 1][j + 1] += 1
                board[i + 1][j - 1] += 1
                board[i - 1][j] += 1
                board[i - 1][j + 1] += 1
                board[i - 1][j - 1] += 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] > 8:
                board[i][j] = "*"
    board.pop(0)
    board.pop(-1)
    for i in range(len(board)):
        board[i].pop(0)
        board[i].pop(-1)
    return board


def main():
    rows, columns = stdin.readline().strip().split()
    cont = 1
    while rows != "0" and columns != "0":
        if cont > 1:
            print()
        board = board_game(rows)
        game = numbers(board)
        print("Field #" + str(cont) + ":")
        for i in range(len(game)):
            for j in range(len(game[i]) - 1):
                print(game[i][j], end="")
            print(game[i][-1])
        cont += 1
        rows, columns = input().split()


main()
