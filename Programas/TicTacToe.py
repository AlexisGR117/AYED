from sys import stdin


def tictactoe():
    game = []
    player_1 = 0
    player_2 = 0
    row = stdin.readline().strip()
    winner = 0
    cont = 0
    while row != "":
        game.append([row[0], row[1], row[2]])
        row = stdin.readline().strip()
    for i in range(3):
        if "O" not in game[i] and "." not in game[i]:
            winner = 1
            cont += 1
        elif "X" not in game[i] and "." not in game[i]:
            winner = 2
            cont += 1
        for j in range(3):
            if game[i][j] == "X":
                player_1 += 1
            elif game[i][j] == "O":
                player_2 += 1
            if i == 0:
                column = [game[0][j], game[1][j], game[2][j]]
                if "O" not in column and "." not in column:
                    winner = 1
                    cont += 1
                elif "X" not in column and "." not in column:
                    winner = 2
                    cont += 1
    diagonal_1 = [game[0][0], game[1][1], game[2][2]]
    if "O" not in diagonal_1 and "." not in diagonal_1:
        winner = 1
        cont += 1
    elif "X" not in diagonal_1 and "." not in diagonal_1:
        winner = 2
        cont += 1
    diagonal_2 = [game[2][0], game[1][1], game[0][2]]
    if "O" not in diagonal_2 and "." not in diagonal_2:
        winner = 1
        cont += 1
    elif "X" not in diagonal_2 and "." not in diagonal_2:
        winner = 2
        cont += 1
    if winner == 1 and cont == 1 and player_1 - player_2 == 1:
        return 0
    elif winner == 2 and cont == 1 and player_1 == player_2:
        return 0
    elif winner == 0 and (player_1 - player_2 == 1 or player_1 == player_2):
        return 0
    else:
        return 1


def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        verdict = tictactoe()
        if verdict == 1:
            print("no")
        else:
            print("yes")

        
main()
