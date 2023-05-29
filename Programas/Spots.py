from sys import stdin


def mapSpots(f_point, s_point, board):
    f_point = (f_point[0]- 1, f_point[1] - 1)
    s_point = (s_point[0] - 1, s_point[1] - 1)

    lower_bound_x, upper_bound_x = min(f_point[0], s_point[0]), max(f_point[0], s_point[0])
    lower_bound_y, upper_bound_y = min(f_point[1], s_point[1]), max(f_point[1], s_point[1])

    for i in range(lower_bound_x, upper_bound_x + 1):
        for j in range(lower_bound_y, upper_bound_y + 1):
            board[i][j] = 0

def countEmptySpots(board):
    sum_spots = 0
    for row in board:
        sum_spots += sum(row)

    if sum_spots == 0:
        print('There is no empty spots.')
    elif sum_spots == 1:
        print('There is one empty spot.')
    else:
        print('There are {0} empty spots.'.format(sum_spots))

def main():
    W, H, N = map(int, stdin.readline().strip().split())
    while not ( W == 0 and H == 0 and N == 0):
        empty_spots = [[1 for i in range(H)] for j in range(W)]
        for i in range(N):
            line = list(map(int, stdin.readline().strip().split()))
            f_point, s_point = (line[0], line[1]), (line[2], line[3])
            mapSpots(f_point, s_point, empty_spots)
        countEmptySpots(empty_spots)
        stdin.readline().strip()
        W, H, N = map(int, stdin.readline().strip().split())


main()

